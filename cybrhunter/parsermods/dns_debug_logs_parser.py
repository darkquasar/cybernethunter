#!/usr/bin/env python3

'''
 NAME: dns_debug_logs_parser.py | Version: 0.2
 CYBRHUNTER Version: 0.3
 AUTHOR: Diego Perez (@darkquasar) - 2018
 DESCRIPTION: This module will allow the analyst to parse Windows DNS Debug logs on demand.
 REF: Simplified and heavily adapted from https://github.com/nerdiosity/DNSplice
 
 USAGE: 
    
 UPDATES: 
    v0.1 - 19-10-2018 - Created script
    v0.2 - 24-11-2020 - Fixed domain parsing issues, integrated tldextract package, improved logging.
    
 ToDo:
        1. Null
'''

import logging
import os
import pandas as pd
import re
import sys
import tldextract

from cybrhunter.helpermods import utils
from datetime import datetime
from pathlib import Path

class ParserMod():

    def __init__(self, file_path):

        # Setup logging
        utilities = utils.HelperMod()
        self.logger = utilities.get_logger('CYBRHUNTER.PARSERS.DNSDEBUGLOG')
        self.logger.info('Initializing {}'.format(__name__))
        
        # initializing variables
        self.file_path = file_path

    def execute(self):
      
        # Initialize list for Final Dataframe
        dns_df_rows_list = []

        # Open the dns log file given as input   
        with open(self.file_path, 'r') as dns_file:
            
            for line in dns_file:
                
                # Look for lines in Windows 2003-2008R2 DNS debug files with "PACKET" in them
                if re.search( r'(.*) PACKET (.*?) .*', line, re.M|re.I): 

                    # Windows 2003
                    # For Windows 2003 type files, look for lines that start with date style YYYYMMDD
                    if re.match('^\d\d\d\d\d\d\d\d', line):
                        # Split the line into fields         
                        log_fields = line.split()

                        # put together the date and time indexes into datetime
                        dns_date = log_fields[0] + ' ' + log_fields[1]
                        dns_datetime = datetime.strptime(dns_date, '%Y%m%d %H:%M:%S')
                        # Client IP
                        dns_client = str(log_fields[7]).strip('[]')
                        # Record Type
                        dns_rtype = str(log_fields[-2]).strip('[]')

                        # create variable to hold the value of dns_uriquery with the leading and trailing '.' stripped off
                        dns_uriquery = re.sub(r"\(\d+\)", r".", str(log_fields[-1]).strip('[]'))
                        dns_uriquery = dns_uriquery.rstrip('.').lstrip('.')

                        # Determine domain based off tld
                        tld_extract = tldextract.extract(dns_uriquery)
                        if re.match('\d+', tld_extract.domain):
                            dns_domain = tld_extract.suffix
                        else:
                            dns_domain = tld_extract.domain + '.' + tld_extract.suffix
                        
                        # Remove any response records as we are only looking for DNS queries
                        if log_fields[9] != 'R':
                            # This limits the client IPs to only RFC1918 addresses                                                      
                            if re.match('^(10\.\d{1,3}|192\.168|172\.1[6-9]|172\.2[0-9]|172\.3[0-1]|127\.0\.0\.1)', dns_client):
                                dns_dict = { 'DateTime': dns_datetime, 'ClientIP': dns_client, 'URIQuery': dns_uriquery, 'Domain': dns_domain, 'RecordType': dns_rtype }

                                yield dns_dict
                                
                    # For Windows 2008R2 type files, look for lines that start with date style MM/DD/YYYY
                    elif re.match('^\d{1,2}\/\d{1,2}\/\d{4}', line):
    
                        log_fields = line.split()
                        dns_date = log_fields[0] + ' ' + log_fields[1] + ' ' + log_fields[2]
                        dns_datetime = datetime.strptime(dns_date, '%d/%m/%Y %I:%M:%S %p')
                        dns_sndrcv = str(log_fields[7]).strip('[]')
                        dns_client = str(log_fields[8]).strip('[]')
                        dns_rtype = str(log_fields[-2]).strip('[]')
                        
                        dns_uriquery = re.sub(r"\(\d+\)", r".", str(log_fields[-1]).strip('[]'))
                        dns_uriquery = dns_uriquery.rstrip('.').lstrip('.')

                        # Determine domain based off tld
                        tld_extract = tldextract.extract(dns_uriquery)
                        if re.match('\d+', tld_extract.domain):
                            dns_domain = tld_extract.suffix
                        else:
                            dns_domain = tld_extract.domain + '.' + tld_extract.suffix

                        if log_fields[10] != 'R':

                            if re.match('^(10\.\d{1,3}|192\.168|172\.1[6-9]|172\.2[0-9]|172\.3[0-1]|127\.0\.0\.1)', dns_client):
                                dns_dict = { 'DateTime': dns_datetime, 'ClientIP': dns_client, 'URIQuery': dns_uriquery, 'Domain': dns_domain, 'RecordType': dns_rtype }

                                yield dns_dict

                    # For Windows 2012R2-2016 type files, look for lines that start with Microsoft-Windows-DNS-Server
                    elif re.match('^Microsoft-Windows-DNS-Server', line): 

                        log_fields = line.split()
                        # Extract Event ID
                        dns_eventID = str(log_fields[3]).strip(",")
                        # create a variable to hold the value the date, convert to string to remove a comma, then convert to int    
                        dns_date = int(str(log_fields[17]).strip(","))
                        dns_datetime = datetime.fromtimestamp((dns_date - 116444736000000000) // 10000000)
                        
                        dns_client = str(re.sub(r'"', r'',log_fields[22])).strip(',')
                        dns_uriquery = str(re.sub(r'\.\"\,', r'', log_fields[24])).strip('"')
                        dns_uriquery = dns_uriquery.rstrip('.').lstrip('.')

                        # Determine domain based off tld
                        tld_extract = tldextract.extract(dns_uriquery)
                        if re.match('\d+', tld_extract.domain):
                            dns_domain = tld_extract.suffix
                        else:
                            dns_domain = tld_extract.domain + '.' + tld_extract.suffix

                        # DNS Analytical log event 256 is for DNS Queries
                        if re.match(r"256",dns_eventID):                     

                            if re.match('^(10\.\d{1,3}|192\.168|172\.1[6-9]|172\.2[0-9]|172\.3[0-1]|127\.0\.0\.1)', dns_client): 

                                dns_dict = { 'DateTime': dns_datetime, 'ClientIP': dns_client, 'URIQuery': dns_uriquery, 'Domain': dns_domain }

                                yield dns_dict
                                
                    elif re.match('^Information',line):

                        log_fields = re.split(';|,',line)

                        dns_eventID = str(log_fields[3])

                        dns_date = log_fields[1]
                        dns_datetime = datetime.strptime(dns_date, '%m/%d/%Y %I:%M:%S %p')

                        dns_client = re.sub(r'Source=|Destination=', r'',log_fields[7])

                        dns_uriquery = re.sub(r'Zone=|QNAME=', r'',log_fields[9].strip("."))
                        dns_uriquery = dns_uriquery.rstrip('.').lstrip('.')

                        # Determine domain based off tld
                        tld_extract = tldextract.extract(dns_uriquery)
                        if re.match('\d+', tld_extract.domain):
                            dns_domain = tld_extract.suffix
                        else:
                            dns_domain = tld_extract.domain + '.' + tld_extract.suffix

                        if re.match(r"256", dns_eventID):
                            dns_dict = { 'DateTime': dns_datetime, 'ClientIP': dns_client, 'URIQuery': dns_uriquery, 'Domain': dns_domain }
                            
                            yield dns_dict

        dns_df = pd.DataFrame(dns_df_rows_list)
        
        # return final dataframe
        return dns_df