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

import json
import logging
import pika
import re
import socket
import sqlite3
import sys
import unicodedata

from kafka import KafkaProducer
from pprint import pprint
from tabulate import tabulate

# Setup logging

class Output:

    def __init__(self, output_type, logtype, kafka_broker=None, rabbitmq_broker=None, rabbitmq_credentials=None, hostname=None):
        
        # Setup logging
        # We need to pass the "logger" to any Classes or Modules that may use it 
        # in our script
        try:
            import coloredlogs
            logger = logging.getLogger('CYBRHUNTER.OUTPUT')
            coloredlogs.install(fmt='%(asctime)s - %(name)s - %(message)s', level="DEBUG", logger=logger)

        except ModuleNotFoundError:
            logger = logging.getLogger('CYBRHUNTER.OUTPUT')
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            console_handler.setLevel(logging.DEBUG)
            logger.addHandler(console_handler)
            logger.setLevel(logging.INFO)
    
        # To be used in sqlite/elasticsearch output
        self.hostname = hostname
        # To determine whether output should be stdout
        self.logtype = logtype
        self.output_type = output_type

        if self.output_type in "sqlite3":
            # No implemented
            print("SQLite3 Output Not Implemented yet")
            self.output_type = "stdout"

        if self.output_type == "kafka":
            self.HOST = kafka_broker[0]
            self.PORT = kafka_broker[1]
            self.kafka_topic = kafka_broker[2]
            self.KAFKAS = self.HOST+':'+str(self.PORT)
            self.kafka_producer = KafkaProducer(bootstrap_servers=self.KAFKAS, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

        if self.output_type == "rabbitmq":
            self.HOST = rabbitmq_broker[0]
            self.PORT = rabbitmq_broker[1]
            credentials = pika.PlainCredentials(rabbitmq_credentials[0], rabbitmq_credentials[1])
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.HOST,credentials=credentials))
            self.channel = connection.channel()

    def send(self, record):
        
        if self.output_type == "sqlite":
            self.send_to_sqlite(record)

        elif self.output_type in ["kafka", "rabbitmq"]:
            self.send_to_elasticsearch(record, ampq=self.output_type)

        elif self.output_type == "stdout-json":
            self.send_to_stdout(record)
            
        elif self.output_type == "stdout-csv":
            self.send_to_stdout(record)
        
    def close_output_pipe(self):

        if self.output_type == "stdout-tsv":
            self.outfilepointer.close()
    
        elif self.output_type == "sqlite":
            self.conn.commit()
            self.conn.close()

        elif self.output_type == "rabbitmq":
            self.channel.close()
    
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
            if self.logtype == 'xml':
                dictobj['log_name'] = dictobj['Channel']
                dictobj['log_src_pipeline'] = "cybrhunter"

            if self.logtype == 'csv':
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
    
    def send_to_stdout(self, data_dict, output_type='csv', nested=False):

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
                # If ingested Log is CSV
                if self.logtype == 'csv':
                    dictobj['log_src_pipeline'] = "cybrhunter"
                    print(ascii(dictobj), file=sys.stdout, flush=True)
        
            # If ingested Log is XML
            # Adding required fields for tagging / compatibility purposes
                elif self.logtype == 'xml':
                    dictobj['log_name'] = dictobj['Channel']
                    dictobj['log_src_pipeline'] = "cybrhunter"
        
                    try:
                        print(ascii(dictobj), file=sys.stdout, flush=True)
                
                    except (AttributeError, TypeError, IOError) as err: 
                        #log error here
                        print("Error, could not print to stdout \n [-] %s" % str(err))
                        sys.exit(1)
            except:
                print(ascii(dictobj), file=sys.stdout, flush=True)
                