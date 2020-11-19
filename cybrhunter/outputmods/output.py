#!/usr/bin/env python3

'''
 Name: maya-output.py
 Version: 0.1
 MAYA Version: 0.1
    
 Author: Diego Perez (@darkquasar) - 2018
 Usage: 
    
 Updates: 
        v0.1: output to elasticsearch-kafka.
        v0.1 - 29-08-2019: adding ability to control kakfa broker settings

    
 ToDo:
        1. always something to do

'''

import json
from kafka import KafkaProducer
import logging
import pika
import re
import socket
import sqlite3
import sys
import unicodedata

# Setup logging


class Output:

    def __init__(self, outtype, logtype, kafka_broker=None, rabbitmq_broker=None, rabbitmq_credentials=None, hostname=None):
        
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
        self.outtype = outtype

        if self.outtype in "sqlite3":
            # No implemented
            print("SQLite3 Output Not Implemented yet")
            self.outtype = "stdout"

        if self.outtype == "kafka":
            self.HOST = kafka_broker[0]
            self.PORT = kafka_broker[1]
            self.kafka_topic = kafka_broker[2]
            self.KAFKAS = self.HOST+':'+str(self.PORT)
            self.kafka_producer = KafkaProducer(bootstrap_servers=self.KAFKAS, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

        if self.outtype == "rabbitmq":
            self.HOST = rabbitmq_broker[0]
            self.PORT = rabbitmq_broker[1]
            credentials = pika.PlainCredentials(rabbitmq_credentials[0], rabbitmq_credentials[1])
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.HOST,credentials=credentials))
            self.channel = connection.channel()

    def open_output_pipe(self, record):
        
        if self.outtype == "sqlite":
            self.send_to_sqlite(record)

        elif self.outtype in ["kafka", "rabbitmq"]:
            self.send_to_elasticsearch(record, ampq=self.outtype)

        elif self.outtype == "stdout-json":
            self.send_to_stdout(record)   
        
    def close_output_pipe(self):

        if self.outtype == "stdout-tsv":
            self.outfilepointer.close()
    
        elif self.outtype == "sqlite":
            self.conn.commit()
            self.conn.close()

        elif self.outtype == "rabbitmq":
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
    
    def send_to_stdout(self, data_dict, parse_w32event=False, nested=False):

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
                        if (parse_w32event == True) and (dictobj.get('message') != None):
                                dictobj['message'] = dictobj['message'].replace('\n\t', ' ').replace('\t\t', ' ').replace('\n\n', ' ').replace('\t', ' ').replace('\n', ' ').replace('&amp;quot;', '"')
                
                                try:
                                        evt_rgx = self.win32event_parsers(dictobj.get('EID'), dictobj['message'])
                                except: 
                                        evt_rgx = None
                    
                                if evt_rgx != None:
                                        dictobj['message'] = evt_rgx

                                print(ascii(dictobj), file=sys.stdout, flush=True)
                
                        else:
                                print(ascii(dictobj), file=sys.stdout, flush=True)
            
                except (AttributeError, TypeError, IOError) as err: 
                        #log error here
                        print("Error, could not print to stdout \n [-] %s" % str(err))
                        sys.exit(1)    

    def win32event_parsers(self, eid, message):
            eid = int(eid)
            # Windows Event Parsing RegEx

            if eid == 4769:
                    # 4769: A Kerberos service ticket was requested
                    # Pass the Ticket
                    evt_rgx = re.compile('Account Name: (?P<AccountName>.*?) Account Domain: (?P<AccountDomain>.*?) Logon GUID: (?P<LogonGUID>.*?) .* Service Name: (?P<ServiceName>.*?) Service ID: (?P<ServiceID>.*?) .* Client Address: (?P<ClientAddress>.*?) Client Port: (?P<ClientPort>.*?) .* Ticket Options: (?P<TicketOptions>.*?) Ticket Encryption Type: (?P<TicketEncryption>.*?) Failure Code: (?P<FailureCode>.*?) Transited Services: (?P<TransitedServices>.*?) ')
        
                    for x in re.finditer(evt_rgx, message):
                            m = [x.group('AccountName'), x.group('AccountDomain'), x.group('LogonGUID'), x.group('ServiceName'), x.group('ServiceID'), x.group('ClientAddress'), x.group('ClientPort'), x.group('TicketOptions'), x.group('TicketEncryption'), x.group('FailureCode'), x.group('TransitedServices')]
    
            elif eid == 4776:
                    # 4776: The computer attempted to validate the credentials for an account
                    # Uses NTLM, local account logon. Pass the Hash. It will get logged on the DC even when the target server
                    # for the logon is not the DC
                    evt_rgx = re.compile('Authentication Package: (?P<AuthenticationPackage>.*?) Logon Account: (?P<LogonAccount>.*?) Source Workstation: (?P<SourceHost>.*?) Error Code: (?P<ErrorCode>.*?) ')
        
                    for x in re.finditer(evt_rgx, message):
                            m = [x.group('AuthenticationPackage'), x.group('LogonAccount'), x.group('SourceHost'), x.group('ErrorCode')]
        
            elif eid == 4625:
                    # 4625: An account failed to log on
                    # Pass the Hash / Ticket
                    evt_rgx = re.compile('Logon ID: (?P<LogonID>.*?) Logon Type:  (?P<LogonType>.*?) .* Security ID: (?P<SecurityID>.*?) Account Name: (?P<AccountName>.*?) Account Domain: (?P<AccountDomain>.*?) .* Failure Reason: (?P<FailureReason>.*?) Status:  (?P<Status>.*?) Sub Status: (?P<SubStatus>.*?) .* Caller Process Name: (?P<CallerProcessName>.*?) .* Workstation Name: (?P<SourceHost>.*?) Source Network Address: (?P<SourceIP>.*?) Source Port: (?P<SourcePort>.*?) .* Logon Process: (?P<LogonProcess>.*?)  Authentication Package: (?P<AuthenticationPackage>.*?) Transited Services: (?P<TransitedServices>.*?) Package Name \(NTLM only\): (?P<PackageName>.*?) Key Length: (?P<KeyLength>.*?) ')
        
                    for x in re.finditer(evt_rgx, message):
                            m = [x.group('AccountName'), x.group('AccountDomain'), x.group('LogonType'), x.group('SourceHost'), x.group('SourceIP'), x.group('FailureReason'), x.group('Status'), x.group('SubStatus'), x.group('LogonProcess'), x.group('AuthenticationPackage'), x.group('TransitedServices'), x.group('PackageName'), x.group('KeyLength')]
            
            elif eid == 4648:
                    # 4648: A logon was attempted using explicit credentials
                    # Pass the Hash / Ticket
                    # Look for suspicious processes involving psexec, cmd, powershell.
                    # This can be triggered when using "runas" (either cmd or GUI click)
                    # Heuristics: (1) source domain different than destination domain
                    # (2) where lsass.exe is the logon processing process and network information
                    # is present since it usually indicates RDP
                    evt_rgx = re.compile('Subject: Security ID: (?P<SourceAccountID>.*?) Account Name: (?P<SourceAccountName>.*?) Account Domain: (?P<SourceAccountDomain>.*?) .* Account Whose Credentials Were Used: Account Name: (?P<DestinationAccountName>.*?) Account Domain: (?P<DestinationAccountDomain>.*?) Logon GUID: (?P<DestinationLogonID>.*?) .* Target Server Name: (?P<DestinationServer>.*?) Additional Information: (?P<Info>.*?) .* Process ID: (?P<ProcessID>.*?) Process Name: (?P<ProcessName>.*?) Network Information:(?P<PlaceHolder>.*?)Network Address: (?P<SourceIP>.*?) Port:')

                    for x in re.finditer(evt_rgx, message):
                            m = [x.group('SourceAccountID'), x.group('SourceAccountName'), x.group('SourceAccountDomain'), x.group('SourceIP'), x.group('DestinationServer'), x.group('DestinationAccountName'), x.group('DestinationAccountDomain'), x.group('DestinationLogonID'), x.group('ProcessName'), x.group('ProcessID')]
    
            elif eid == 4720:
                    # 4720: New Account Created 
                    # Must provide parsing
                    print("Not implemented")
        
            elif eid == 4672:
                    # 4672: Special privileges assigned to new logon
                    # Privileged Account Usage. This event triggers when an 
                    # account is assigned "administrator equivalent" rights.
                    # This event also gets logged for any server or application
                    # accounts with high privileges via batch job (schedule task)
                    # or system services.
                    print("Not implemented")
    
            else:
                    evt_rgx = None
    
            if evt_rgx == None:
                    return evt_rgx
    
            return m