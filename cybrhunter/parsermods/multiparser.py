#!/usr/bin/env python3

'''
 NAME: multiparser.py | Version: 0.3
 CYBRHUNTER Version: 0.3
 AUTHOR: Diego Perez (@darkquasar) - 2018
 DESCRIPTION: This is the central module for parsing files into individual "json" records that are consumable by other pipelines. It can also be used standalone for the moment.
 USAGE: 
 
 UPDATES: 
    v0.1: parse any XML to a flat dict.
    v0.2: parse any CSV to a flat dict.
    v0.3 - 03-09-2019: added ability to parse multi-line CSV file into single-line CSV file. Kind of redundant since I discovered later
    that PANDAS can do it by default.
    
 ToDo:
    1. make an argument that will call a shell script that will automagically
       run evtxexport and output parsed files to a folder

'''

import argparse
import csv
import json
import logging
import os
import pandas
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
        

        
class Help():
    '''
    When invoked from commandline, this class will return help
    '''
    
    '''
    PREPARE EVTX DATA WITH EVTXEXPORT
    for i in /mnt/ewf/Windows/System32/winevt/Logs/*.evtx ; do name=${i#"/mnt/ewf/Windows/System32/winevt/Logs/"} ; echo "Parsing $name" ; evtxexport "$i" -f xml | sed -e "s/.*evtxexport.*/<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<itemsList>/" > xmlevtx/"$name".xml ; done
    for i in xmlevtx/*.xml ; do if grep -q "No records to export" "$i" ; then rm "$i"; fi ; done
    
    Notes: this loop will create a .xml data inside [targetfolder] for each
    parsed .evtx file. It will also remove data that creates a malformed XML file thus making it easier for XMLTOJSON.PY to operate on the returned files. The 2nd line will remove any files that don't contain any records.
    '''

# The class that will handle all our arguments
class Arguments(object):
    
  def __init__(self, args):
    self.parser = argparse.ArgumentParser(
      description="XML to JSON Document Converter"
    )
    
    self.parser.add_argument(
      "-x", "--xmlparsetype",
      help="This option determines how the target file is parsed. When ""flat"" is selected, the XML will be output a flat dictionary. When ""nested"" is selected, the XML will be output as a nested dictionary. If two or more elements within the nested dictionary are equal, they will be embedded within a list.",
      type=str,
      choices=["nested", "flat"],
      default="flat",
      required=False
    )
        
    self.parser.add_argument(
      "-l", "--logtype",
      help="This option specifies the type of log being ingested. Type xml requires a file in XML format with proper wrapping (opening and closing top-level root node). Type csv requires a csv file in ASCII format.",
      type=str,
      choices=["xml", "csv", "other"],
      default="xml",
      required=False
    )
        
    self.parser.add_argument(
      "-f", "--file",
      help="File or folder (the script will list all files within it) to be converted",
      type=str,
      required=True
    )

    self.parser.add_argument(
      "-o", "--output",
      help="Type of output: stdout-csv, stdout-json, kafka, elasticsearch",
      type=str,
      choices=["stdout-csv", "stdout-json", "elasticsearch-rabbitmq", "elasticsearch-kafka"],
      default="stdout-json",
      required=False
    )            

    self.pargs = self.parser.parse_args()
      
  def get_args(self):
      return self.pargs


class MultiParser():

  def __init__(self, xmlparsetype, logtype, filepath):
    # initializing variables
    self.xmlparsetype = xmlparsetype
    self.logtype = logtype
    self.filepath = filepath
      
  def parser(self):
    '''
    This function will allow us to add data to the main Dictionary. Thanks: https://stackoverflow.com/questions/32278823/iterating-over-children-of-a-particular-tag-using-elementtree
    '''
    if self.logtype == 'xml':
      for record in self.recursive_xml_parser(self.xmlparsetype, self.logtype, self.filepath):
        yield record

    if self.logtype == 'csv':
      row_iterator = pd.read_csv(self.filepath, engine="c", chunksize=1)
      for row in row_iterator:
        yield self.csv_to_json(i.to_dict(orient='records')[0])    

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
            
    # Appending tag
    row_2['log_src_pipe'] = "dfir-csv"
    
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

  def recursive_xml_parser(self, xmlparsetype, logtype, filepath):

    ''' 
        This function will allow you to parse an XML of n-depth to a dict object. The results won't be exportable to a TSV or sqlite3 file due to the nested nature of it, but they will be ready for ELK! The function has been optimized so that it consumes the same (negligent) amount of RAM and will log to stdout by default. 
    '''
    logger.info('Parsing data from {}'.format(filepath))
    
    # compiling a RegEx that will aid in the removal of badly configured schema leftovers
    self.schema_info = re.compile('{.*?}')
    
    xmltree = ET.iterparse(filepath, events=('start', 'end'))
    xmltree = iter(xmltree)
    event, self.root = xmltree.__next__()
    
    try:
    
      for event, elem in xmltree:
        self.count = self.counter(1)
        
        # Dealing with the leftovers of exporting all logs to 
        # a file using evtxexport. The added "schema" info could be removed by
        # iterating through the files before parsing but this would add extra
        # overhead to the process
        schema_tag = re.findall(self.schema_info, elem.tag)
        if len(schema_tag) > 0:
          elem.tag = elem.tag.split(schema_tag[0])[1]
        
        
        if xmlparsetype == "flat":
          yield self.flat_recursive_xml_parser(xmltree, elem.tag, {})
        else:
          yield (self.flatten_lists_on_dict(self.nested_recursive_xml_parser(xmltree, elem.tag, None)))
          
    except ET.ParseError:
      pass
      #print("XML Error found")
          
              
  def counter(self,n):
    while True:
      n = n + 1
      yield n

  def flat_recursive_xml_parser(self, xmltree, first_level_node, result_dict):
      
    for event, elem in xmltree:
      # Dealing with the leftovers of executing evtxexport
      schema_tag = re.findall(self.schema_info, elem.tag)
      if len(schema_tag) > 0:
        elem.tag = elem.tag.split(schema_tag[0])[1]

      if event == "end" and len(elem.getchildren()) == 0:
            
        if self.logtype == 'xml':
          # Preventing evtxparse metadata <Execution ProcessID="488" ThreadID="3220"/>
          # from appending another "ProcessID" key
          if elem.tag == 'Execution':
            continue
        
        # CASE: elem does not contain any text but elem attributes do
        # Ex: <Key SomeKey="SomeValue"></Key>
        if len(elem.attrib) > 0 and elem.text == None:
          for attr in elem.attrib:
            if elem.tag == 'Provider':
              result_dict['Provider'] = elem.attrib['Name']
              break
            else:
              result_dict[attr] = elem.attrib[attr]
                    
        '''
        if the "tag" has already been seen (like in the above
        example of multiple "Data" tags, we must make sure that
        (a) we add them if the elem.attrib value is unique
        (b) we exclude them if already present
        (c) we add a counter value to the name if the elem.attrib value
        (not the name of the attribute like "Key" but rather
        its value like "SubjectUserSid") is 
        repeated [<-- not handled yet]
        CASE: elem.tag already in result_dict.keys()
        '''
        
        if elem.tag in result_dict.keys():
          # CASE: EVTXEXPORT don't add the first child of <EventData> as "Data"
          if self.logtype == 'xml' and elem.attrib.get('Name') and elem.text != None:
            result_dict[elem.attrib['Name']] = elem.text
              
          # CASE: EVTXEXPORT if multiple <Data> tags under <EventData> 
          # without any differentiating attributes inside the elem
          elif self.logtype == 'xml' and len(elem.attrib) == 0 and elem.text != None:
            result_dict[elem.tag+str(self.count.__next__())] = elem.text
      
      # CASE: elem.tag NOT IN result_dict.keys()
        else:
          ''' 
          Handling duplicate tags with duplicate 
          attribute names, like cases where you have:
              <Data Name="SubjectUserSid">S-1-5-18</Data>
              <Data Name="SubjectUserName">-</Data>
              <Data Name="SubjectDomainName">-</Data>
              <Data Name="SubjectLogonId">0x00000000000003e7</Data>
          In this example, the elem.tag is the same ('Data'), as are
          the attribute keys ('Name').
          NOTE: The code below DOES NOT handle cases where 
          an elem.tag has multiple elem.attrib
          ''' 
          
          # Handling exceptions for evtxexport
          if self.logtype == 'xml' and elem.tag == "Data" and len(elem.attrib) > 0:
            result_dict[elem.attrib['Name']] = elem.text
              
          # this 2nd block will, by default, not collect any elements
          # that don't have attributes and are empty
          elif len(elem.attrib) == 0 and elem.text == None:
            continue
              
          else:
            result_dict[elem.tag] = elem.text
        
      elif event == "start":
        continue
      
      if event == "end" and elem.tag == first_level_node:
        self.root.clear()
        return

      elif event == "end":
        if len(elem.getchildren()) > 0:
          self.flat_recursive_xml_parser(xmltree, first_level_node, result_dict)
          return result_dict
              
  def nested_recursive_xml_parser(self, xmltree, first_level_node, new_elem=None):
    # https://stackoverflow.com/questions/19286118/python-convert-very-large-6-4gb-xml-files-to-json?newreg=1f34414a077a4ed5a951054f7859b7d8
        
    items = defaultdict(list)

    '''
    elem.attrib appends the attributes found within the same tag; not required here
    if new_elem:
        items.update(new_elem.attrib)
    '''
    
    text = ""
    
    for event, elem in xmltree:
      # Dealing with the leftovers of executing evtxexport
      if 'schemas.microsoft.com' in elem.tag:
        elem.tag = elem.tag.split('{http://schemas.microsoft.com/win/2004/08/events/event}')[1]            
      
      if event == "end" and elem.tag == first_level_node:
        self.root.clear()
  
      if event == 'start':
        items[elem.tag].append(self.nested_recursive_xml_parser(xmltree, elem))
          
      elif event == 'end':
        
        text = elem.text.strip().replace('"','') if elem.text else ""
        elem.clear()
        self.root.clear()
        break
    
    if len(items) == 0:
      return text

    return { k: v if len(v) == 1 else v for k, v in items.items() }

  def flatten_lists_on_dict(self, d):
    '''
        This function takes a nested dict as outputted by "nested_recursive_xml_parser" and recursively removes any lists whose content is a single item (regardless of this item being a string or a dict). 
    '''
    if isinstance(d, dict):
      return {a:b[0] if len(b) == 1 and isinstance(b[0], str) else (self.flatten_lists_on_dict(b[0]) if len(b) == 1 and isinstance(b[0], dict) else [self.flatten_lists_on_dict(c) for c in b]) for a, b in d.items()}    
        