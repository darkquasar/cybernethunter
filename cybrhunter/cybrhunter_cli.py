#!/usr/bin/env python3

'''
 NAME: cybrhunter.py | version: 0.1
 CYBRHUNTER Version: 0.2
 AUTHOR: Diego Perez (@darkquasar) - 2018
 DESCRIPTION: Main module that controls the behaviour of the CYBRHUNTER Hunting and IR framework 
    
 Updates: 
        v0.1: ---.
    
 ToDo:
        1. Split the "output" argument into two different ones: output_type (xml, json, csv, etc.) and output_pipe (kafka, rabbitmq, stdout, etc.)

'''

import argparse
import importlib
import logging
import os
import sys
import time

from datetime import datetime as datetime
from pathlib import Path
from time import strftime

# Ugly but workable importing solution so that the package can be 
# (1) imported as a package, (2) run from commandline with `python -m cybrhunter`
# or (3) from the source directory as `python cybrhunter.py`
if "cybrhunter" in sys.modules:
    from cybrhunter.helpermods import utils_mod
    from cybrhunter.outputmods import output as cyout
    from cybrhunter.parsermods import xml_parser as cyxml
    from cybrhunter.parsermods import csv_parser as cycsv
else:
    from helpermods import utils_mod
    from outputmods import output as cyout
    from parsermods import xml_parser as cyxml
    from parsermods import csv_parser as cycsv

class Arguments(object):
    
    def __init__(self, args):

        self.parser = argparse.ArgumentParser(
                description="CYBRHUNTER DFIR Framework"
                )
    
        self.parser.add_argument(
                "-a", "--action",
                help="This option determines what action will be executed by CYBRHUNTER: parse logs, collect logs, hunt (runs a particular data anlysis mod) or learn (ML)",
                type=str,
                choices=["collect", "hunt", "learn", "parse"],
                default="parse",
                required=False
                )
        
        self.parser.add_argument(
                "-f", "--file",
                help="File or folder (the script will list all files within it) to be processed",
                type=str,
                required=True
                )

        self.parser.add_argument(
                "-ht", "--hunt-template",
                help="Select the hunting template (YAML format) that will be applied to your data",
                type=str,
                default=None,
                required=False
                )

        self.parser.add_argument(
                "-kb", "--kafka-broker",
                help="Define the kafka broker options separated by a space as follows: IP PORT TOPIC. Example: ""127.0.0.1 9092 winlogbeat""",
                type=str,
                default="127.0.0.1 9092 logstash",
                required=False
                )

        self.parser.add_argument(
                "-l", "--log-type",
                help="This option specifies the type of log being ingested. Type ""xml"" requires a file in XML format with proper wrapping (opening and closing top-level root node). Type csv requires a ""csv"" file in ASCII format.",
                type=str,
                choices=["xml", "csv"],
                default="xml",
                required=False
                )

        self.parser.add_argument(
                "-m", "--module",
                help="Use a module to perform ETL operations on target files",
                type=str,
                choices=["standard_parser", "xml_parser", "csv_parser", "dns_debug_logs_parser"],
                default="standard_parser",
                required=False
                )

        self.parser.add_argument(
                "-of", "--output-file",
                help="Name for the output file if this output pipe is selected",
                type=str,
                default=None,
                required=False
                )

        self.parser.add_argument(
                "-op", "--output-pipe",
                help="Pipe of output: stdout, file, kafka, rabbitmq, elasticsearch",
                type=str,
                choices=["stdout", "file", "rabbitmq", "kafka", "elasticsearch"],
                default="stdout",
                required=False
                )

        self.parser.add_argument(
                "-ot", "--output-type",
                help="Type of output: csv, tsv, json, sqlite",
                type=str,
                choices=["tsv", "csv", "json", "sqlite"],
                default="json",
                required=False
                )

        self.parser.add_argument(
                "-rb", "--rabbitmq-broker",
                help="Define the rabbit-mq broker options separated by a space as follows: ""IP PORT"". Example: ""127.0.0.1 9501""",
                type=str,
                default="127.0.0.1 9501",
                required=False
                )

        self.parser.add_argument(
                "-rc", "--rabbitmq-credentials",
                help="Define the rabbit-mq broker credentials separated by a space as follows: ""user password"". Example: ""admin P@ssword123""",
                type=str,
                default="127.0.0.1 9501",
                required=False
                )

        self.parser.add_argument(
                "-x", "--xmlparsetype",
                help="This option determines how the target XML file is parsed. When ""flat"" is selected, the XML will be converted to a flat json. When ""nested"" is selected, the XML will be converted to a nested json resembling the structure of the original XML. If two or more elements within the nested dictionary are equal, they will be embedded within a list.",
                type=str,
                choices=["nested", "flat"],
                default="flat",
                required=False
                )

        self.pargs = self.parser.parse_args()

    def get_args(self):
        return self.pargs

class cyh_helpers:

    def __init__(self):

        # Setup logging
        utils = utils_mod.HelperMod()
        self.logger = utils.get_logger('CYBRHUNTER')

    # Define an "init_output_pipe" function that will initialize the output pipe for the records processed by the parsermods.
    def init_output_pipe(self, output_pipe, output_type, output_file=None, log_type=None, kafka_broker=None, rabbitmq_broker=None, rabbitmq_credentials=None):
        # Helper function to initialize an output pipe

        self.kafka_broker = kafka_broker.split(" ")
        self.rabbitmq_broker = rabbitmq_broker.split(" ")
        self.rabbitmq_credentials = rabbitmq_credentials.split(" ")

        self.output_pipe = cyout.Output(output_pipe=output_pipe, output_type=output_type, output_file=output_file, log_type=log_type, kafka_broker=self.kafka_broker, rabbitmq_broker=self.rabbitmq_broker, rabbitmq_credentials=self.rabbitmq_credentials)

    def send_to_optput_pipe(self, data):
        # Helper function to iterate over a generator and send each record through the output pipe

        self.logger.info('Running records through output pipe')
        print('\n')

        try:
            while True:
                record = data.__next__()
                if record == None:
                    continue
                self.output_pipe.send(record)

        except StopIteration:
            pass

        finally:
            self.output_pipe.close_output_pipe()

    def list_targetfiles(self, pargs):
        # Checking to see if a directory or only one file was passed in as argument
        # to "--file"
        filepath = Path(pargs.file)

        # If a single file
        if Path.is_dir(filepath) == False:
            targetfiles = [filepath]
        else:
            # We need to capture any exceptions when collecting files within a folder
            # to avoid having to clean the list of files inside a folder later on. 
            # CASE 1: logtype is "csv", we only want to keep a list of files that 
            # are csv files
            if pargs.log_type == "csv":
                file_type_filter = ".csv"
            elif pargs.log_type == "xml":
                file_type_filter = ".xml"
            else:
                file_type_filter = ""
        
            try:
                targetfiles = [f for f in filepath.iterdir() if Path.is_file(f) and file_type_filter in f.suffix]    
            except FileNotFoundError:
                self.logger.Error('Please select a valid filename or directory')

        return targetfiles

def main():

    helpers = cyh_helpers()

    # Capture arguments    
    args = Arguments(sys.argv)
    pargs = args.get_args()

    # Capturing start time for debugging purposes
    st = datetime.now()
    start_time = strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    helpers.logger.info("Starting CYBRHUNTER Hunting Framework")

    # CYBRHUNTER ACTION: PARSE
    if pargs.action == "parse":
        helpers.logger.info("Starting CYBRHUNTER Parsers")

        # Obtain a list of all target files
        targetfiles = helpers.list_targetfiles(pargs)

        # Iterating over the results and closing pipe at the end    
        for file in targetfiles:
            
            # Running a check to determine whether we have a file name for the output if a file pipe is selected
            if pargs.output_pipe == 'file' and pargs.output_file == None:
                helpers.logger.error("You must specify a --output-file parameter if you are choosing a file output pipe")
                sys.exit()

            # Start an output pipe
            helpers.init_output_pipe(
                output_pipe=pargs.output_pipe,
                output_type=pargs.output_type,
                output_file=pargs.output_file,
                log_type=pargs.log_type,
                kafka_broker=pargs.kafka_broker,
                rabbitmq_broker=pargs.rabbitmq_broker,
                rabbitmq_credentials=pargs.rabbitmq_credentials
            )

            # Load the required parsermod
            load_parser_mod = importlib.import_module("." + pargs.module, "parsermods")
            parsermod = load_parser_mod.ParserMod(file)
            # Execute parsermod
            results = parsermod.execute()
            # Send records to output pipe
            helpers.send_to_optput_pipe(results)

            '''
            try:
                while True:
                    record = results.__next__()
                    if record == None:
                            continue
                    parsermod.fileparser.outpipe.open_output_pipe(record)

            except StopIteration:
                pass

            finally:
                parsermod.close()
                parsermod.fileparser.outpipe.close_output_pipe()
            '''

    # CYBRHUNTER ACTION: COLLECT
    if pargs.action == "collect":
        helpers.logger.info("Initiating CYBRHUNTER DFIR Collector")
        helpers.logger.info("Starting CYBRHUNTER MultiParser")

        # Obtain a list of all target files
        targetfiles = helpers.list_targetfiles(pargs)

        # Iterating over the results and closing pipe at the end    
        for file in targetfiles:
            parsermod = importlib.import_module("." + pargs.module, "parsermods")
            parsermod = parsermod.ParserMod(pargs.logtype, file, pargs.output, collect=True)
            parsermod.execute()
            parsermod.runpipe(parsermod.results)

    # CYBRHUNTER ACTION: HUNT
    elif pargs.action == "hunt":
        # TBD: idea is to load the hunt-template and pass execution of the template
        # to the "jaguarhunter" (imports PySpark) module inside huntmods. This module(s) will load the template
        # and produce an ElasticSearch Index as output
        print("TBD")

    # Capturing end time for debugging purposes
    et = datetime.now()
    end_time = strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    hours, remainder = divmod((et-st).seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    helpers.logger.info("Finished Parsing")
    helpers.logger.info('Took: \x1b[47m \x1b[32m{} hours / {} minutes / {} seconds \x1b[0m \x1b[39m'.format(hours,minutes,seconds))

if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print("\n" + "My awesome awesomeness has been interrupted by the gods. Returning to the depths of the earth" + "\n\n")