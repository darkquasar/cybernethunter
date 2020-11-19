#!/usr/bin/env python3

'''
 NAME: multiparser.py | Version: 0.3
 CYBRHUNTER Version: 0.3
 AUTHOR: Diego Perez (@darkquasar) - 2018
 DESCRIPTION: This module will provide miscellaneous parsing capabilities for records.
 
 USAGE: 
    
 UPDATES: 
    v0.1: parse any XML to a flat dict.
    v0.2: parse any CSV to a flat dict.
    v0.3 - 03-09-2019 - added ability to parse multi-line CSV file into single-line CSV file. Kind of redundant since I discovered later that PANDAS can do it by default.
    v0.4 - 19-11-2020 - Cleaned up this parser, removed XML parsing routines to its own mod
    
 ToDo:
        1. make an argument that will call a shell script that will automagically run evtxexport and output parsed files to a folder

'''

import csv
import json
import logging
import os
import pandas as pd
import re
import sys
import time
import xml.etree.cElementTree as ET
from collections import defaultdict
from datetime import datetime as datetime
from pathlib import Path
from time import strftime


# *** Setup logging ***
logger = logging.getLogger('MULTIPARSER')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)


'''
# can't use until I fix kafka logging verbosity
try:
    import coloredlogs
    coloredlogs.install(fmt='%(asctime)s - %(name)s - %(message)s', level="DEBUG")
    
except ModuleNotFoundError:
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)
    logger.setLevel(logging.INFO)
'''

class MultiParser():

    def __init__(self, logtype, filepath):
        # initializing variables
        self.logtype = logtype
        self.filepath = filepath
      
    def parser(self):
        '''
        This function will allow us to add data to the main Dictionary. Thanks: https://stackoverflow.com/questions/32278823/iterating-over-children-of-a-particular-tag-using-elementtree
        '''

        if self.logtype == 'csv':
            row_iterator = pd.read_csv(self.filepath, engine="c", chunksize=1)
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
        row_2['log_src_pipe'] = "cybrhunter-dfir-csv"
    
        return dict(row_2)
    
    def convert_multilines_to_singlelines(self, file):
        # This function is not yet completed, idea is to convert multiline output from Kape RECmd files like OpenPIDMRU to single lines
        # KAPE's "batch" mkape module produces good output but with these caveats. Must convert to absolute single-line CSVs so that 
        # we can send to elasticsearch

        with open(file, newline='', encoding='utf-8') as csvfile:

            new_csv_file_name = file + "_cleaned_multilines"

            with open(new_csv_file_name, 'w+', encoding='utf-8') as newcsvfile:

                # Find columns whose values are wrapped within quotes and end in the same line
                pattern_1_quotes = re.compile('\".*?\",', re.MULTILINE)
                # Find columns whose values start with double quotes and DO NOT end in the same line
                # We use a negative lookahead
                pattern_2_quotes_no_end_same_line = re.compile('(?!,".*?",),".*?$', re.MULTILINE)
                # Find columns that start with '"' (double quotes)
                pattern_3_quotes_at_start = re.compile('^\",', re.MULTILINE)
                # Capture everything after '"' that doesn't have an ending '"'
                pattern_4_capture_unfinished_string = re.compile(',(\".*?)$')
    
                # Setup initial variables
                line_start = []
                line_end = []
                multiline_offsets = []
                line_number = 0
                line_offset_count = []
                lines_to_skip_total = []
                skip_next_line_from_new_file = False
    
                # Read one line from the file
                line = csvfile.readline()
    
                while line:
                    # Let's capture the line number
                    line_number = line_number + 1
        
                    # Appending byte offset of current line to a list
                    line_offset_count.append(csvfile.tell())
        
                    # Running RegEx patterns through line string
                    m1 = pattern_1_quotes.findall(line)
                    m2 = pattern_2_quotes_no_end_same_line.findall(line)
                    m3 = pattern_3_quotes_at_start.findall(line)
        
                    # If this condition is true, we are in the presence of an unfinished multi-line string
                    if len(m2) > 0:
                        # Let's capture the byte offset where the multi-line string starts
                        line_start = [csvfile.tell(), line_number]
                        # Let's setup a flag that indicates to the new "clean" file that next lines shouldn't
                        # be written
                        skip_next_line_from_new_file = True
        
                    # If this condition is true, then we have arrived to the end of the "multi-line" string in the file
                    elif len(m3) > 0:
                        # Let's capture the byte offset where the multi-line string ends
                        line_end = [csvfile.tell(), line_number]
        
                        # Appending all skipped lines numbers to a big list. Index position "1" for
                        # line_start and line_end contains the number of the line.
                        lines_to_skip = [x for x in range(line_start[1], line_end[1])]
                        for skippedlines in lines_to_skip:
                            lines_to_skip_total.append(skippedlines)
        
                        # Appending the byte offsets between which the multi-line string has been found to 
                        # a list for later processing
                        multiline_offsets.append([line_start, line_end])
        
                        # Resetting write to new file flag
                        skip_next_line_from_new_file = False
        
                        # *** Going to read multi-lines and write them to new file *** #
                        # Let's go back to the previous offset in the collected list of offsets,
                        # so as to get to the beginning of the line 
                        # and not wherever the anomalies were found by the RegEx logics
                        current_multiline_range = multiline_offsets.pop()
                        file_offset_start = line_offset_count[(line_offset_count.index(current_multiline_range[0][0]) - 1)]
                        file_offset_end = current_multiline_range[1][0]
                        csvfile.seek(file_offset_start)
                        multilines = (csvfile.read(file_offset_end - file_offset_start)).split("\r\n")
        
                        # Let's join back the split lines into a single one this time replacing the actual new lines with literal "\n" which
                        # can be interpreted by elasticsearch
                        converted_multiline = ""
                        list_len = len(multilines)
                        for i, item in enumerate(multilines):
                            # Skip last empty item (we don't need a "\n" at the end)
                            if i == (list_len - 1) and item == "":
                                break
                            if item == '':
                                converted_multiline = converted_multiline + '\r\n'
                            else:
                                converted_multiline = converted_multiline + item
            
                        newcsvfile.write(converted_multiline)
                        newcsvfile.write("\n")
        
                        # Finally, let's reset the byte offset position back to its original state
                        # which was the "end" line of the multi-line
                        csvfile.seek(current_multiline_range[1][0])
        
                    # If we get to this condition, then we are in the presence of a regular single-line CSV string
                    # safe to write to new file, only if not part of the multi-line string
                    elif skip_next_line_from_new_file == False:
                        #print(line.split("\r\n")[0])
                        newcsvfile.write(line.split("\r\n")[0])
                        newcsvfile.write("\n")
        
                    line = csvfile.readline()