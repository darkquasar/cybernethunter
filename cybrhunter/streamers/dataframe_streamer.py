#!/usr/bin/env python3

'''
 NAME: dataframe_streamer.py | version: 0.1
 CYBRHUNTER Version: 0.3
 AUTHOR: Diego Perez (@darkquasar) - 2020
 DESCRIPTION: Streamer for Pandas DataFrames
    
 Updates: 
        v0.1 - 25-11-2020 - Created script
    
 ToDo:
        1. ----.

'''

import json
import numpy as np
import os
import pandas as pd
import sys
import time

from cybrhunter.helpermods import utils
from streamz import Stream

class Streamer:
    
    def __init__(self):
        
        # Setup logging
        self.utilities = utils.HelperMod()
        self.logger = self.utilities.get_logger('CYBRHUNTER.STREAMER.DATAFRAME')
        self.logger.info('Initializing {}'.format(__name__))
        
    def stream_to_dataframe_by_key(self, value_list:list, key_selector:list) -> dict:

        # value_list: the list of values to filter by, a different stream filter will be created
        # based off these values
        # key_selector: in a dict, whether nested or flat, this is the key or nested key that is used
        # to retrieve the values against which the value_list will be compared to break off the different
        # streams

        # Setup Stream Pipeline
        self.source_pipe = Stream()
        df_dict = {}

        for value in value_list:
            key_name = '{}_df'.format(value)
            df_dict[key_name] = pd.DataFrame()
            
            self.source_pipe.filter(
                lambda record: self.utilities.get_value_from_nested_dict(
                    record,
                    nested_keys_list=key_selector
                ) == value
            ).map(self.append_dataframe)


    def append_dataframe(self, record:dict) -> pd.DataFrame:
        
        df = pd.DataFrame().from_dict([record])
        return pd.DataFrame().append(df)
    
    def stream_from_dataframe_to_csv(self, dataframe:pd.core.frame.DataFrame, target_file:str):
        # this function will essentially append dataframes to a CSV file
        
        dataframe.to_csv(target_file, mode='a', index=False)