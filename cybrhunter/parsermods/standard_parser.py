'''
 MODULE NAME: standard_parser.py | Version: 0.3
 CYBRHUNTER Version: 0.1
 AUTHOR: Diego Perez (@darkquasar) - 2018
 DESCRIPTION: This is the default module executed when no particular parser mod is passed to cybrhunter.py.
 It can be used as a template of how parser mods should be construed. The default module prints results back to stdout in json format.
'''

import logging
import parsermods.multiparser as mp
import outputmods.output as outmod

# *** Setup logging ***
logger = logging.getLogger('STANDARD_PARSER')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)

# All parsermods have a class called "mod" and define
# any initialization parameters inside.
# Parsermods can have any number of functions inside the "mod" class.
class mod:
  def __init__(self, xmlparsetype, logtype, filepath, **kwargs):
  
    # Initializing variables
    logger.info('Initializing {}'.format(__name__))
    self.xmlparsetype = xmlparsetype
    self.logtype = logtype
    self.filepath = filepath


  # All parsermods must contain an "init_output_pipe" function that will initialize the output pipe 
  # for the records processed by the mod.
  def init_output_pipe(self, output, kafka_broker=None, rabbitmq_broker=None, rabbitmq_credentials=None):
    
    self.output = output
    self.kafka_broker = kafka_broker.split(" ")
    self.rabbitmq_broker = rabbitmq_broker.split(" ")
    self.rabbitmq_credentials = rabbitmq_credentials.split(" ")

    self.outpipe = outmod.Output(self.output, self.logtype, kafka_broker=self.kafka_broker, rabbitmq_broker=self.rabbitmq_broker, rabbitmq_credentials=self.rabbitmq_credentials)

  # All parsermods must contain an "execute" function that will initiate the parsing action on each 
  # record. Other functions can be defined in this module that do the actual heavy lifting
  # whilst the "execute" function only calls them for code clarity. In the case of the current
  # module we call Multiparser (another parsermod) and use its results. The function should return
  # a generator back to the calling module (like cybrhunter.py) so that records can be iterated through.
  def execute(self):

    # Instantiating the MultiParser for plain parsing (no modules)
    self.fileparser = mp.MultiParser(self.xmlparsetype, self.logtype, self.filepath)
    self.results = self.fileparser.parser()

    return self.results
      
  def runpipe(self, results):
    logger.info('Running records through output pipe')
    try:
      while True:
        record = results.__next__()
        if record == None:
          continue
        self.outpipe.open_output_pipe(record)

    except StopIteration:
      pass

    finally:
      self.close()
      self.outpipe.close_output_pipe()
    
  def close(self):
    # Method that gets called by cybrhunter.py to close a pipe
    logger.info('Closing Module {}'.format(__name__))