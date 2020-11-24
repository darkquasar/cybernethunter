#!/usr/bin/env python3

'''
MODULE NAME: output.py | Version: 0.2
CYBRHUNTER Version: 0.2
AUTHOR: Diego Perez (@darkquassar) - 2018
DESCRIPTION: main module to handle outputs
    
 Updates: 
        v0.1 - 15-01-2018 - output to elasticsearch-kafka.
        v0.2 - 29-08-2019 - adding ability to control kakfa broker settings
    
 ToDo:
        1. always something to do

'''

import csv
import json
import logging
import pika
import re
import socket
import sqlite3
import sys
import unicodedata

from cybrhunter.helpermods import utils_mod
from kafka import KafkaProducer
from pprint import pprint
from tabulate import tabulate

# Setup logging

class Output:

    def __init__(self, output_type='json', output_pipe='stdout', output_file=None, log_type=None, kafka_broker=None, rabbitmq_broker=None, rabbitmq_credentials=None, host_name=None):
        
        # Setup logging
        utils = utils_mod.HelperMod()
        self.logger = utils.get_logger('CYBRHUNTER.OUTPUT')
        self.logger.info('Initializing {}'.format(__name__)) 
    
        # To be used in sqlite/elasticsearch output
        self.host_name = host_name
        
        # To determine which pipe to send the output to
        self.log_type = log_type
        self.output_type = output_type
        self.output_pipe = output_pipe
        self.output_file = output_file
        
        self.kafka_broker = kafka_broker
        self.rabbitmq_broker = rabbitmq_broker
        self.rabbitmq_credentials = rabbitmq_credentials
        
        self.logger.info("Will send data to output pipeline in {} format".format(self.output_type))

    
    def define_output_workflow(self):
        
        # Determine allowed combinations
        
        output_flow = (self.output_pipe, self.output_type)
        allowed_flows = [
            ('kafka', 'json'),
            ('rabbitmq', 'json'),
            ('stdout', 'json'),
            ('stdout', 'csv'),
            ('stdout', 'tsv'),
            ('file', 'json'),
            ('file', 'csv'),
            ('file', 'tsv'),
        ]
        
        if not output_flow in allowed_flows:
            self.logger.error('Output Flow {} not implemented or available'.format(output_flow))
            sys.exit()
        
        # First initialize output pipes

        if self.output_pipe == 'kafka':
            self.HOST = self.kafka_broker[0]
            self.PORT = self.kafka_broker[1]
            self.kafka_topic = self.kafka_broker[2]
            self.KAFKAS = self.HOST+':'+str(self.PORT)
            self.kafka_producer = KafkaProducer(bootstrap_servers=self.KAFKAS, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

        if self.output_pipe == 'rabbitmq':
            self.HOST = self.rabbitmq_broker[0]
            self.PORT = self.rabbitmq_broker[1]
            credentials = pika.PlainCredentials(self.rabbitmq_credentials[0], self.rabbitmq_credentials[1])
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.HOST,credentials=credentials))
            self.channel = connection.channel()

        # Second define output type if needed

        if self.output_pipe == 'stdout':
            pass

        if self.output_pipe == 'file':

            if self.output_type in 'sqlite3':
                # No implemented
                print("SQLite3 Output Not Implemented yet")
                self.output_type = "stdout"

    def send(self, record):

        if self.output_pipe == 'stdout':

            if self.output_type == "json":
                self.send_to_stdout(record, output_type='json')

            elif self.output_type == "csv":
                self.send_to_stdout(record, output_type='csv')

            elif self.output_type == "tsv":
                self.send_to_stdout(record, output_type='tsv')

        elif self.output_pipe == 'file':

            if self.output_type == "sqlite":
                self.send_to_sqlite(record)

            elif self.output_type == "csv":
                
                # Routine to initialize the file if it does not exist
                try:
                    if self.tabular_file_created == True:
                        self.send_to_tabular_file(record)
                except AttributeError:
                    self.tabular_file_created = True
                    self.tabular_output_file = open(self.output_file, mode='a+', newline='')
                    self.tabular_writter = csv.writer(self.tabular_output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    self.tabular_writter.writerow([header for header in record.keys()])
                    self.send_to_tabular_file(record)
                        
            elif self.output_type == "tsv":
                
                # Routine to initialize the file if it does not exist
                try:
                    if self.tabular_file_created == True:
                        self.send_to_tabular_file(record)
                except AttributeError:
                    self.tabular_file_created = True
                    self.tabular_output_file = open(self.output_file, mode='a+', newline='')
                    self.tabular_writter = csv.writer(self.tabular_output_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    self.tabular_writter.writerow([header for header in record.keys()])
                    self.send_to_tabular_file(record)

            elif self.output_type == "json":

                # Routine to initialize the file if it does not exist
                try:
                    if self.json_file_created == True:
                        self.send_to_json_file(record)
                except AttributeError:
                    self.json_file_created = True
                    self.json_output_file = open(self.output_file, mode='a+')
                    self.send_to_json_file(record)

        elif self.output_pipe in ["kafka", "rabbitmq"]:
            self.send_to_elasticsearch(record, ampq=self.output_type)

    def send_to_tabular_file(self, record):
            self.tabular_writter.writerow([values for values in record.values()])

    def send_to_json_file(self, record):
        self.json_output_file.write(json.dumps(record))
        self.json_output_file.write('\n')

    def close_output_pipe(self):

        if "stdout" in self.output_type:
            pass

        elif self.output_type == "sqlite":
            self.conn.commit()
            self.conn.close()

        elif self.output_type == "rabbitmq":
            self.channel.close()
            
        elif self.output_pipe == 'file':
            if self.output_type in ['tsv', 'csv']:
                self.tabular_output_file.close()
            elif self.output_type == 'json':
                self.json_output_file.close()

    def send_to_sqlite(self, data):

            data.pop(0)
            data.insert(0, self.hostname)

            try:
                self.cur.executemany("INSERT INTO StateAgentInspector (" + self.fields_asOneString + ") VALUES (" + self.fields_number + ");", [data])

            except Exception as e:
                print(e)

    def send_to_elasticsearch(self, data_dict, nested=False, ampq="kafka"):
            # store non-empty keys in a list so as to only display those keys with actual values for each event category to stdout
            nonemptykey = []
            timestamp_fields = ['timestamp', 'Time']

            # Preparing the Data
            try:    
                if nested == False:
                        # ensuring we tag empty keys
                        for x in data_dict.keys():
                                if data_dict[x] == '':
                                        data_dict[x] == 'null'
                                        #nonemptykey.append(x)
                        #dictobj = dict({key : data_dict[key] for key in nonemptykey})
                else: 
                        dictobj = data_dict

            except:
                    pass

            # Pre-Processing Data
            # (1) We need to capture the field that designates 
            # the timestamp in each processed log so that we can
            # rename it for ELK mappings
            for field in timestamp_fields:
                    time_field = dictobj.get(field,0)
                    if time_field != 0:
                            dictobj['@timestamp'] = dictobj.pop(field)
                            break

            # (2) We need to enrich the logs with a "log_name" field
            # so that Logstash can identify it in the Filter/Output plugins
            # We also need to include the hostname of the collection as an 
            # added field for all records so that we can filter by hostname
            # in ELK.
    
            # Assigning a name to the log according to their collector source
            # make sure to lowercase the string and replace any (/,\,+,[space]),
            # otherwise elasticsearch cannot create the index
            if self.log_type == 'windows-event':
                dictobj['log_name'] = dictobj['Channel']
                dictobj['log_src_pipeline'] = "cybrhunter"

            if self.log_type == 'csv':
                dictobj['log_src_pipeline'] = "cybrhunter"          
    
            # Assigning the value of the source host where the logs were collected
            dictobj['log_hostname'] = self.hostname
            
            # Sending Data
            try: 
                    # Sending the data to ELK
                    if ampq == "kafka":
                            self.kafka_producer.send(self.kafka_topic, dictobj)
        
                    elif ampq == "rabbitmq":
                            self.channel.basic_publish(exchange='logstash-rabbitmq',routing_key='',body=(json.dumps(dictobj)).encode())
            except: 
                    #log error here
                    print("Error 2, could not connect to socket")
                    sys.exit(1)
    
    def send_to_stdout(self, data_dict, output_type='tsv', nested=False):

            # store non-empty keys in a list so as to only display those keys with actual values for each event category to stdout
            nonemptykey = []

            # Preparing the Data
            try:    
                if nested == False:
                    # ensuring we get rid of empty keys
                    for x in data_dict.keys():
                        if data_dict[x] != '':
                            nonemptykey.append(x)
                    dictobj = dict({key : data_dict[key] for key in nonemptykey})
                else:
                    dictobj = data_dict

            except:
                pass
    
    
            # *** SENDING DATA TO STDOUT ***
            # ******************************
            try:
        
            # If ingested Log is XML
            # Adding required fields for tagging / compatibility purposes
                if self.log_type == 'windows_event':
                    dictobj['log_name'] = dictobj['Channel']
                    dictobj['log_src_pipeline'] = "cybrhunter"
                
            except (AttributeError, TypeError, IOError) as err: 
                #log error here
                self.logger.error("Error, could not print to stdout \n [-] %s" % str(err))
                sys.exit(1)

            try:
                if output_type == 'tsv':
                    tsv_record_raw = [ str(value).replace('\n','').replace('  ', ' ') for value in dictobj.values() ]
                    tsv_record = '\t'.join(tsv_record_raw)
                    print(tsv_record, file=sys.stdout, flush=True)
                    
                elif output_type == 'csv':
                    csv_record_raw = [ str(value).replace('\n','').replace('  ', ' ') for value in dictobj.values() ]
                    csv_record = ','.join(csv_record_raw)
                    print(csv_record, file=sys.stdout, flush=True)
                    
                elif output_type == 'json':
                    print(ascii(dictobj), file=sys.stdout, flush=True)

            except (AttributeError, TypeError, IOError) as err: 
                #log error here
                self.logger.error("Error, could not print to stdout \n [-] %s" % str(err))
                sys.exit(1)
                    
            except Exception as err:
                self.logger.error("Error, could not print to stdout \n [-] %s" % str(err))
                sys.exit(1)