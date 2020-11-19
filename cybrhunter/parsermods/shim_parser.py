'''
 MODULE NAME: shimparser.py | Version: 0.1
 CYBRHUNTER Version: 0.1
 AUTHOR: Diego Perez (@darkquasar) - 2018
 DESCRIPTION: This module will invoke Eric Zimmerman's "AppCompatCacheParser.exe" to parse the contents of a SYSTEM hive and return a CSV. It requires that AppCompatCacheParser is configured in CYBRHUNTER.conf.
'''

import commonmods
import json
import logging
import os.path
import parsermods.default as dp
import subprocess
import yaml
import zipfile

# *** Configure Logging ***
logger = logging.getLogger('SHIM_PARSER')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)

class mod:
  def __init__(self, xmlparsetype, logtype, filepath, output, collect=False, **kwargs):
  
    # Initializing variables
    logger.info('Initializing {}'.format(__name__))
    self.xmlparsetype = xmlparsetype
    self.logtype = logtype
    self.filepath = filepath
    self.output = output
    self.cm = commonmods.common()
      
  def parse_shim(self, systemhive):
    # Get CYBRHUNTER framework base dir (one level above .\parsermods)
    # CYBRHUNTER_base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))
    
    AppCompatParserBin = self.cm.get_bin_path("AppCompatCacheParserPath")

    for file in systemhive:
      if ".csv" not in file:
        filepath = self.shim_tmp_dir + "\\" + file
        subprocess.run([AppCompatParserBin, '-f', filepath, '--csv', self.shim_tmp_dir])
    
  def execute(self, run_output_pipe=True):
    # 1. Unzip SYSTEM Hive files
    # 2. Execute AppCompatCacheParser on extracted files that match Hive magic number
    # 3. Call default parser mod to parse extracted csv(s)

    # Create TMP directory for file extraction
    # if "./CYBRHUNTERhunter/data/shim_tmp" doesn't exist
    logger.info('Checking whether temp directory for extracted SYSTEM Hives exists')
    self.shim_tmp_dir = self.cm.create_dir("shim_tmp")

    # Need to check if the SYSTEM Hive is contained within a ZIP or standalone
    # Until I implement python-magic, this is kind of manual and weird...
    try:
      self.cm.unzip(self.filepath, self.shim_tmp_dir, filter="registry_hive") # unzip only those files that are Hives
      hives_files_list = self.cm.list_files(self.shim_tmp_dir) # list files in folder where hives have been unzipped
    except:
      logger.warn('SYSTEM Hive is not zipped')
      hives_files_list = self.filepath

    # Parse all SYSTEM Hives
    self.parse_shim(hives_files_list)

    # List files in shim_tmp_dir so that we can then process the CSVs
    # TODO: once python_magic is implented the list_files function
    # should have a parameter that specifies which file types to return
    files_list = self.cm.list_files(self.shim_tmp_dir)
    
    for file in files_list:
      if ".csv" in file:
        abs_file_path = self.shim_tmp_dir + "\\" + file
        self.parser = dp.mod(self.xmlparsetype, self.logtype, abs_file_path, self.output, collect=False)
        self.results = self.parser.execute(run_output_pipe=False)
        self.fileparser = self.parser.fileparser
        
        # A parsermod output pipe can be run or only a pointer
        # to the "results" generator returned to the calling module
        if run_output_pipe == True:
          self.runpipe(self.results)
        else:
          return self.results
          
  def runpipe(self, results):
    logger.info('Running records through output pipe')
    try:
      while True:
        record = results.__next__()
        if record == None:
          continue
        self.fileparser.outpipe.open_output_pipe(record)

    except StopIteration:
      pass

    finally:
      self.close()
      self.fileparser.outpipe.close_output_pipe()
          
  def close(self):
    # Method that gets called by runpipe to 
    # perform any closing actions on it
    logger.info('Closing Module {}'.format(__name__))