#!/usr/bin/env python3

'''
 NAME: evtx_parser.py | Version: 0.1
 CYBERNETHUNTER Version: 0.3
 AUTHOR: Diego Perez (@darkquasar) - 2019
 DESCRIPTION: This module will parse EVTX records into JSON using pyevtx-rs
 REFERENCE: https://github.com/omerbenamram/evtx
 USAGE: 

 UPDATES: 
    v0.1: 18-12-2019 - Created initial script
    
 ToDo:
        1. 

'''

import fsspec
import json
import logging
import sys

from cybernethunter.helpermods import utils
from evtx import PyEvtxParser
from pathlib import Path

class ParserMod():

    def __init__(self, file_path):
        
        # Setup logging
        utilities = utils.HelperMod()
        self.logger = utilities.get_logger('CYBERNETHUNTER.PARSERS.EVTX')
        self.logger.info('Initializing {}'.format(__name__))

        # initializing variables
        self.file_path = file_path

    def execute(self):

        self.logger.info('Parsing data from {}'.format(self.file_path))

        with fsspec.open(self.file_path, 'rb') as evtx_file:
            evtx_parser = PyEvtxParser(evtx_file)
            for record in evtx_parser.records_json():
                yield json.loads(record['data'])