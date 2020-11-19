#!/usr/bin/env python3

'''
 NAME: multiparser.py | Version: 0.3
 CYBRHUNTER Version: 0.3
 AUTHOR: Diego Perez (@darkquasar) - 2018
 DESCRIPTION: This module will parse XML records into JSON
 USAGE: 
    
 UPDATES: 
    v0.1: 19-11-2020 - Created file from initial multiparser
    
 ToDo:
        1. 

'''

import json
import logging
import os
import pandas as pd
import re
import sys
import xml.etree.cElementTree as ET
from collections import defaultdict
from pathlib import Path

# *** Setup logging ***
logger = logging.getLogger('XMLPARSER')
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
    parsed .evtx file. It will also remove data that creates a malformed XML file thus making it easier for MULTIPARSER.PY to operate on the returned files. The 2nd line will remove any files that don't contain any records.
    '''

class parsermod():

    def __init__(self, filepath, xmlparsetype='flat'):
        # initializing variables
        # xmlparsetype identifies whether the resulting json record should be flat or nested
        self.xmlparsetype = xmlparsetype
        self.filepath = filepath

    def execute(self):

        ''' 
        This function will allow you to parse an XML of n-depth to a dict object. The results won't be exportable to a TSV or sqlite3 file due to the nested nature of it, but they will be ready for ELK! The function has been optimized so that it consumes the same (negligent) amount of RAM and will log to stdout by default. 
        '''
        
        logger.info('Parsing data from {}'.format(self.filepath))
    
        # compiling a RegEx that will aid in the removal of badly configured schema leftovers
        self.schema_info = re.compile('{.*?}')
    
        xmltree = ET.iterparse(self.filepath, events=('start', 'end'))
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

                if self.xmlparsetype == "flat":
                    yield self.flat_recursive_xml_parser(xmltree, elem.tag, {})
                else:
                    yield (self.flatten_lists_on_dict(self.nested_recursive_xml_parser(xmltree, elem.tag, None)))
          
        except ET.ParseError:
            pass
        
    def parser(self):
        '''
        This function will allow us to add data to the main Dictionary. Thanks: https://stackoverflow.com/questions/32278823/iterating-over-children-of-a-particular-tag-using-elementtree
        '''
        for record in self.execute():
            yield record
              
    def counter(self, n):
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
                    if elem.attrib.get('Name') and elem.text != None:
                        result_dict[elem.attrib['Name']] = elem.text
              
                    # CASE: EVTXEXPORT if multiple <Data> tags under <EventData> 
                    # without any differentiating attributes inside the elem
                    elif len(elem.attrib) == 0 and elem.text != None:
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
                    if elem.tag == "Data" and len(elem.attrib) > 0:
                        result_dict[elem.attrib['Name']] = elem.text
              
                    # this 2nd block will, by default, not collect any elements
                    # that don't have attributes and are empty
                    elif len(elem.attrib) == 0 and elem.text == None:
                        continue
              
                    else:
                        result_dict[elem.tag] = elem.text
        
            elif event == "start":
                continue
      
            if event == "end":
                
                if elem.tag == first_level_node:
                    self.root.clear()
                    return
                
                elif len(elem.getchildren()) > 0:
                    self.flat_recursive_xml_parser(xmltree, first_level_node, result_dict)
                    return result_dict
                
                else:
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