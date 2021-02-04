#!/usr/bin/env python3

'''
 NAME: csv_parser.py | Version: 0.3
 CYBERNETHUNTER Version: 0.3
 AUTHOR: Diego Perez (@darkquasar) - 2018
 DESCRIPTION: This module will provide miscellaneous parsing capabilities for records.
 
 USAGE: 
    
 UPDATES: 
    v0.1 - parse any CSV to a flat dict.
    v0.2 - 03-09-2019 - added ability to parse multi-line CSV file into single-line CSV file. Kind of redundant since I discovered later that PANDAS can do it by default.
    v0.3 - 19-11-2020 - Cleaned up this parser, removed XML parsing routines to its own mod
    
 ToDo:
        1. ZZZZ
'''

import csv
import json
import logging
import os
import pandas as pd
import re
import sys

from pathlib import Path

class ParserMod():

    def __init__(self, file_path):

        # Setup logging
        # We need to pass the "logger" to any Classes or Modules that may use it 
        # in our script
        try:
            import coloredlogs
            self.logger = logging.getLogger('CYBERNETHUNTER.PARSERS.CSV')
            coloredlogs.install(fmt='%(asctime)s - %(name)s - %(message)s', level="DEBUG", logger=self.logger)

        except ModuleNotFoundError:
            self.logger = logging.getLogger('CYBERNETHUNTER.PARSERS.CSV')
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            console_handler.setLevel(logging.DEBUG)
            self.logger.addHandler(console_handler)
            self.logger.setLevel(logging.INFO)
        
        # initializing variables
        self.file_path = file_path

    def execute(self):
        '''
        This function will allow us to add data to the main Dictionary. Thanks: https://stackoverflow.com/questions/32278823/iterating-over-children-of-a-particular-tag-using-elementtree
        '''
        
        self.logger.info('Parsing data from {}'.format(self.file_path))

        row_iterator = pd.read_csv(self.file_path, engine="c", chunksize=1)
        for row in row_iterator:
            yield self.csv_to_json(row.to_dict(orient='records')[0])    

        '''
        # Using this method with the "csv" module is magnitudes faster than 
        # using Pandas, however I can't find a solution to the "null bytes" (\x00)
        # that can sometimes be mixed up in the row data

        if self.logtype == 'csv':
            with open(self.filepath, 'r') as csvfile:
                self.reader = csv.DictReader(csvfile)
                for row in self.reader:
                    try:
                        yield self.csv_to_json(row)
                    except:
                        pass
        '''

    def csv_to_json(self, row):

        # we are giving this action a function of its own in case we want to perform 
        # some pre-processing on the csv records before sending them to the output pipe

        # Let's cleanup keys with non-ascii characters
        # Making a copy of the dict since we can't iterate and modify it at the same time
        row_2 = row.copy()

        for key in row.keys():
            if re.match(r'[^\x00-\x7f]', key):
                clean_key = re.sub(r'[^\x00-\x7f]', r'', key)
                # Let's remove the non-ascii key from the copied object
                row_2.pop(key)
                row_2[clean_key] = row[key]
                row_2.move_to_end(clean_key, last=False)

        # Tagging
        row_2['log_src_pipe'] = "cybernethunter-dfir-csv"

        return dict(row_2)