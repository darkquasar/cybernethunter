#!/usr/bin/env python3

'''
 NAME: umbrella_connector.py | version: 0.1
 CYBRHUNTER Version: 0.3
 AUTHOR: Diego Perez (@darkquasar) - 2020
 DESCRIPTION: Connector that wraps some of Cisco Umbrella's API functionalities
    
 Updates: 
        v0.1 - 24-11-2020 - Created script
    
 ToDo:
        1. ----.

'''

import json
import logging
import numpy as np
import os
import pandas as pd
import re
import requests
import sys
import time

from cybrhunter.helpermods import utils
from datetime import datetime, timedelta
from enum import Enum

class Connector:
    
    def __init__(self):
        
        # Setup logging
        utilities = utils.HelperMod()
        self.logger = utilities.get_logger('CYBRHUNTER.CONNECTORS.UMBRELLA')
        self.logger.info('Initializing {}'.format(__name__))
        
    def increment_datetime_by_minutes(self, timestamp:str, minutes:int):
        dt = datetime.fromisoformat(timestamp) + timedelta(minutes=minutes)
        
        while True:
            yield dt.isoformat()
            dt = dt + timedelta(minutes=minutes)
        

    def timestamp_to_unixepoch_ms(self, timestamp:str):
        # Convert from ISO format first, then grab int64 representation and multiply by 1000 to get milliseconds
        dt = datetime.fromisoformat(timestamp).timestamp() * 1000

        return int(np.trunc(dt))

    class umbrella_api_activity_endpoint(Enum):
        allactivity = 'activity'
        dns = 'activity/dns'
        proxy = 'activity/proxy'
        firewall = 'activity/firewall'
        ip = 'activity/ip'

    def umbrella_authenticate(self, basic_auth_b64):
        
        url = "https://management.api.umbrella.com/auth/v2/oauth2/token"

        payload = {}
        headers = {
        'd': 'grant_type=client_credentials',
        'Authorization': 'Basic {}'.format(basic_auth_b64)
        }

        response = requests.request("POST", url, headers=headers, data = payload)
        bearer_token = json.loads(response.text)

        # We will store the token in a property and also store the 
        # time it was requested so that we can renew it before 
        # 3600s (1h) have elapsed
        self.umbrella_bearer_token = bearer_token['access_token']
        self.umbrella_bearer_token_start_time = datetime.now()
        self.basic_auth_b64 = basic_auth_b64

    def umbrella_api_activity_query(self, org_id:str, api_endpoint: umbrella_api_activity_endpoint, from_timestamp:str, to_timestamp:str, records_limit:int, domains_filter:list=[]):
        
        # Umbrella Activity API documentation: https://docs.umbrella.com/umbrella-api/reference#activity
        
        if len(domains_filter) > 0:
            url = "https://reports.api.umbrella.com/v2/organizations/{}/{}?from={}&to={}&limit={}&domains={}".format(org_id, api_endpoint.value, from_timestamp, to_timestamp, records_limit, ','.join(domains_filter))
        else:
            url = "https://reports.api.umbrella.com/v2/organizations/{}/{}?from={}&to={}&limit={}".format(org_id, api_endpoint.value, from_timestamp, to_timestamp, records_limit)

        payload = {}
        headers = {
            'Authorization': 'Bearer {}'.format(self.umbrella_bearer_token)
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        data_dict = json.loads(response.text)
        
        if re.match('.*error.*', response.text):
            self.logger.error(response.text, response.headers)
        else:
            return data_dict['data']
        
    def get_umbrella_api_activity_dataframe(self, start_time:str, end_time:str, time_window_minute_increments:int, org_id:str, api_endpoint: umbrella_api_activity_endpoint, records_limit:int, bearer_token:str=None, domains_filter:list=[], return_columns:list=['timestamp', 'externalip', 'domain'], time_zone:str='Australia/Melbourne'):
        
        # Example start_time = '2020-02-18T00:00:00'
        # Example end_time = '2020-03-18T00:00:00'
        # Example return_columns for the dataframe: ['timestamp', 'externalip', 'domain', 'verdict']
        # Example Time Zone value: 'Australia/Melbourne'

        '''
        Example calling this function from JupyterNotebooks
        
        from cybrhunter.connectors import umbrella_connector as cyh_umbrella
        umb = cyh_umbrella.Connector()
        umb.umbrella_authenticate("YOUR_BASE64_TOKEN_HERE")
        domains_filter = ["avsvmcloud.com", "digitalcollege.org", "freescanonline.com", "deftsecurity.com", "highdatabase.com", "thedoccloud.com", "virtualdataserver.com", "incomeupdate.com", "zupertech.com", "databasegalore.com", "panhardware.com", "websitetheme.com"]

        start_time = '2020-03-01T00:00:00'
        end_time = '2020-12-16T10:00:00'

        umb_df = umb.get_umbrella_api_activity_dataframe(
                    start_time=start_time,
                    end_time=end_time,
                    time_window_hourly_increments=6,
                    org_id=XXXXXXX,
                    api_endpoint=umb.umbrella_api_activity_endpoint.dns,
                    records_limit=5000,
                    domains_filter=domains_filter,
                    return_columns=['timestamp', 'externalip', 'domain'],
                    time_zone='Australia/Melbourne')
        '''

        if not self.umbrella_bearer_token and bearer_token == None:
            self.logger.error('Please provide a Base64 Encoded Bearer Token or run umbrella_authenticate before calling this function')
            sys.exit()
        
        elif not self.umbrella_bearer_token and bearer_token != None:
            self.umbrella_bearer_token = bearer_token
        
        time_incremental = self.increment_datetime_by_minutes(start_time, minutes=time_window_minute_increments)
        
        final_df = pd.DataFrame()

        while datetime.fromisoformat(start_time) <= datetime.fromisoformat(end_time):

            # Umbrella API rate limit: 3 requests per second
            for i in range(3):
                
                # first check bearer token validity and re-authenticate if required
                current_time = datetime.now()
                if (current_time - self.umbrella_bearer_token_start_time) >= timedelta(seconds=3600):
                    self.umbrella_authenticate(self.basic_auth_b64)

                start_timestamp = self.timestamp_to_unixepoch_ms(start_time)
                end_timestamp = time_incremental.__next__()
                
                umbrella_results = self.umbrella_api_activity_query(
                    org_id=org_id,
                    domains_filter=domains_filter,
                    api_endpoint=api_endpoint,
                    from_timestamp=start_timestamp,
                    to_timestamp=self.timestamp_to_unixepoch_ms(end_timestamp),
                    records_limit=records_limit
                )

                result = pd.DataFrame(umbrella_results, columns=return_columns)

                result['timestamp'] = pd.to_datetime(result['timestamp'], unit='ms')
                result['timestamp'] = result.timestamp.dt.tz_localize('UTC').dt.tz_convert(time_zone)
                
                final_df = final_df.append(result)
                start_time = end_timestamp

            time.sleep(1)
            
        return final_df