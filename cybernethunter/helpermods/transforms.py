#!/usr/bin/env python3

'''
 NAME: transforms.py | version: 0.1
 CYBERNETHUNTER Version: 0.3
 AUTHOR: Diego Perez (@darkquasar) - 2019
 DESCRIPTION: Collection of helper modules to facilitate some data transformation tasks.
    
 Updates: 
        v0.1 - 17-06-2019 - Created script.
    
 ToDo:
        1. ----.

'''

import logging
import numpy as np
import os
import pandas as pd
import re
import sys
import yaml
from pathlib import Path

from cybernethunter.helpermods import utils
from urllib.parse import urlparse

class HelperMod:

    def __init__(self):
        
        # Setup logging
        utilities = utils.HelperMod()
        self.logger = utilities.get_logger('CYBERNETHUNTER.HELPERS.TRANSFORM')

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
                    
    def normalize_url(self, url, return_string=True):
        # This function will apply some normalization to URL strings
        
        parsed_url_dict = urlparse(url)
        
        if return_string == True:

            if 'github' in parsed_url_dict.netloc and not 'raw=true' in parsed_url_dict.query:
                parsed_url = '{}://{}{}?raw=true'.format(parsed_url_dict.scheme, parsed_url_dict.netloc, parsed_url_dict.path)

            else:
                parsed_url = parsed_url_dict.geturl()
                
            return parsed_url
        
        else: 
            return parsed_url_dict
                
            
    def convert_json_record(self, json_record: dict, to_type: str ='csv'):
        # This function will convert json records to other types like CSV, TSV
        
        if to_type == 'tsv':
            tsv_record_raw = [ str(value).replace('\n','').replace('  ', ' ') for value in json_record.values() ]
            tsv_record = '\t'.join(tsv_record_raw)
            return tsv_record
                    
        elif to_type == 'csv':
            csv_record_raw = [ str(value).replace('\n','').replace('  ', ' ') for value in json_record.values() ]
            csv_record = ','.join(csv_record_raw)
            return csv_record     
        
    def tag_json_record(self, json_record: dict, tags_dict_list: list):
        # This function will allow us to add extra keys to a json record for tagging purposes
        # Example:
        #   json_record['log_name'] = json_record['Channel']
        #   json_record['log_src_pipeline'] = 'cybernethunter'
        
        for dict_element in tags_dict_list:
            for tag in dict_element:
                json_record[tag] = dict_element[tag]