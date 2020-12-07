#!/usr/bin/env python3

'''
 NAME: utils.py | version: 0.2
 CYBRHUNTER Version: 0.3
 AUTHOR: Diego Perez (@darkquasar) - 2018
 DESCRIPTION: Collection of helper modules to facilitate specific tasks in CYBRHUNTER like: downloading the tools required for artefact acquisition, copying a file using raw disk access, etc.
    
 Updates: 
        v0.2: Added tools download function.
    
 ToDo:
        1. ----.

'''

import logging
import os
import re
import shutil
import subprocess
import sys
import wget
import yaml
import zipfile

from pathlib import Path


class HelperMod:
    
    def __init__(self):
        
        # Setup logging
        # We need to pass the "logger" to any Classes or Modules that may use it 
        # in our script
        try:
            import coloredlogs
            
            FIELD_STYLES = dict(
                asctime=dict(color='green'),
                levelname=dict(color='cyan'),
                name=dict(color='cyan')
            )

            self.logger = logging.getLogger('CYBRHUNTER.HELPERS.COMMON')
            coloredlogs.install(
                fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                level="DEBUG",
                field_styles=FIELD_STYLES,
                logger=self.logger
            )

        except ModuleNotFoundError:
            self.logger = logging.getLogger('CYBRHUNTER.HELPERS.COMMON')
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            console_handler.setLevel(logging.DEBUG)
            self.logger.addHandler(console_handler)
            self.logger.setLevel(logging.INFO)

        # Initializing variables        
        config_file_path = Path.cwd() / "cyberhunt-config.yml"
        
    def get_logger(self, logger_name:str):
        # Setup logging 
        # We need to pass the "logger" to any Classes or Modules that may use it 
        # in our script
        try:
            import coloredlogs
            
            FIELD_STYLES = dict(
                asctime=dict(color='green'),
                levelname=dict(color='cyan'),
                name=dict(color='cyan')
            )

            self.logger = logging.getLogger(logger_name)
            coloredlogs.install(
                fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                level="DEBUG",
                field_styles=FIELD_STYLES,
                logger=self.logger
            )

        except ModuleNotFoundError:
            self.logger = logging.getLogger(logger_name)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            console_handler.setLevel(logging.DEBUG)
            self.logger.addHandler(console_handler)
            self.logger.setLevel(logging.INFO)
            
        return self.logger

    def get_cyberhunt_tools(self):

        CYBRHUNTER_base_dir = Path.cwd()

        # Download Tools
        # tools = self.extract_key_dict("tools", self.CYBRHUNTER_config).__next__()
        tools_dict = self.CYBRHUNTER_config['tools']

        for kitem, vitem in tools_dict.items():
            # tool: ex. "RawCopy", "AppCompatCacheParser", etc.
            for ktool, vtool in tools_dict[kitem].items():
                target_path = Path.cwd() / tools_dict[kitem][ktool]['ExtractDir']
                self.logger.info('Downloading [{}] from {} to {}'.format(ktool, tools_dict[kitem][ktool]['SourceUrl'], str(target_path)))
                self.create_dir(target_path)
                try:
                    wget.download(tools_dict[kitem][ktool]['SourceUrl'], str(target_path))
                except ValueError:
                    continue

                # Now let's unzip the tools if they should be unzipped
                extracted_tool_name = Path(tools_dict[kitem][ktool]['SourceUrl'])
                extracted_tool_path = target_path / extracted_tool_name.name
                if "zip" in extracted_tool_name.suffix:
                    self.unzip(extracted_tool_path, target_path, extract_all=True)

    def create_dir(self, target_dir, return_handle=False, erase_contents=False):
            # This function will create a new folder at the specified location
            # relative to CYBRHUNTER's base dir. If the folder already exists, it will do nothing, 
            # unless "erase_contents" is set to True. In both cases it will return a string 
            # with the absolute path to the folder.

            # Get CYBRHUNTER framework base dir which should be at the same level as commonmods.py
            CYBRHUNTER_base_dir = Path.cwd()
            target_dir = Path(target_dir)
            target_dir = CYBRHUNTER_base_dir / target_dir

            if not Path.exists(target_dir):
                self.logger.info('Directory [' + str(target_dir) + '] does not exist, creating it...')
                os.makedirs(target_dir)
        
                if return_handle == False:
                    return
                else:
                    return target_dir

            else: 
                self.logger.info('Directory [' + str(target_dir) + '] already exists')

                if erase_contents == True: 
                    self.logger.info('Erasing contents of Directory [' + str(target_dir) + ']')
                    for fileobj in target_dir.iterdir():
                        try:
                            if os.path.isfile(fileobj):
                                    os.unlink(fileobj)
                            # Uncomment in the future adding an option to erase the directory as well
                            #elif os.path.isdir(fileobj): 
                            # shutil.rmtree(fileobj)
                        except Exception as e:
                                print(e)

                if return_handle == False:
                    return
                else:
                    return target_dir

    def list_files(self, path):
        # Helper function to return list of files inside a directory
        # If the parameter passed as "path" is a path to a file, return the file path itself back
        # to the calling function, otherwise, if the path is a directory, return the list of all files
        # (only the files)

        # Converting the path string to pathlib.Path() object
        path = Path(path)

        if Path.is_file(path):
            return path
        else:
            return [f for f in path.iterdir() if f.is_file]

    def copy_raw_file(self, src, dst):

        # Get a handle to the RawCopy app
        app_rawcopy = self.get_bin_path("RawCopy")
        self.logger.info('Loading RawCopy at {}'.format(app_rawcopy))

        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags = subprocess.CREATE_NEW_CONSOLE | subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE

        try:
            self.logger.info('Copying file {} to {}'.format(src, dst))
            subprocess.run([str(app_rawcopy), '/FileNamePath:{}'.format(src), '/OutputPath:{}'.format(dst)], startupinfo=startupinfo)
        except:
            self.logger.info('Could not copy file {}'.format(src))

    def extract_key_dict(self, key, dictionary):
            # This helper function iterates over the "n" depth structure of a dict 
            # in search for a Key specified in the "key" parameter, then
            # returns all values associated with that Key.

            if hasattr(dictionary, 'items'):
                for k, v in dictionary.items():
                    if k == key:
                        yield v
                    if isinstance(v, dict):
                        for result in self.extract_key_dict(key, v):
                            yield result
                    elif isinstance(v, list):
                        for d in v:
                            for result in self.extract_key_dict(key, d):
                                yield result

    def get_bin_path(self, app):
        # This function will return the absolute path to the tool specified in the "app" parameter
        # as a Pathlib.Path() object

        # Get CYBRHUNTER framework base dir which should be at the same level as commonmods.py
        CYBRHUNTER_base_dir = Path.cwd()

        cfg = self.CYBRHUNTER_config

        # Loading CYBRHUNTER.yml will return a list of 3 elements, the first one [0] represents
        # the folder where the tool will be extracted relative to CYBRHUNTER's base directory, 
        # the second one [1] represents the name of the executable and finally the 
        # third one [2] represents the download URL.
        # The names give to the executables are extracted from [1]

        binary_path = self.extract_key_dict(app, cfg).__next__()

        bin_path = Path() / CYBRHUNTER_base_dir / binary_path[0] / binary_path[1]

        return bin_path

    def load_cybrhunter_config(self, config_path):
        # This function will load cyberhunt-config.yml
        
        self.logger.info('Loading CYBRHUNTER Config at {}'.format(config_path))

        with open(config_path, 'r') as conf:
            try:
                self.CYBRHUNTER_config = yaml.load(conf)
            except yaml.YAMLError as e:
                print(e)

    def unzip(self, src, dst, extract_all=False, name_filter=None, type_filter=None):
        # Helper function to unzip files. It accepts two filters:
        # 1. name_filter: it will only extract a file matching this name pattern
        # 2. type_filter: it will only extract a file that matches a particular type (like PE)

        # TODO: improve this function by collecting all file names at the beginning
        # so as to not have to iterate over each file for a simple string match

        # Open the ZIP file
        self.logger.info('Accessing Zip file {}'.format(src))
        with zipfile.ZipFile(src, 'r') as zipf:
            if extract_all == True:
                self.logger.info('Extracting files to {}'.format(dst))
                zipf.extractall(dst)

            if name_filter != None:
                files_list = [f.filename for f in zipf.infolist()]

                for filen in files_list:
                    if re.match(name_filter, filen):
                        self.logger.info('Extracting file {}'.format(filen))
                        zipf.extract(filen, dst)
                        break
                    else:
                        file_in_zip = False
        
                if file_in_zip == False:
                    self.logger.info('No file found inside [{}] matching pattern {}'.format(src, name_filter))

            else:  
                for zfile in zipf.infolist():
                    if type_filter != None:
                        with zipf.open(zfile.filename) as fileitem: 
                            if type_filter == "registry_hive":
                                # NT Registry Hive Magic Number:
                                # 72 65 67 66 => regf
                                NT_MAGIC_DAT = b'\x72\x65\x67\x66'
                                if NT_MAGIC_DAT == fileitem.read(4):
                                    zipf.extract(zfile, dst)
                                    
    def get_value_from_nested_dict(self, record:dict, nested_keys_list:list):
        
        # This function will return the value of a nested key in a dictionary
        # when the depth of nested keys nor their names is known

        for key in nested_keys_list:

            # Get the record, zoom into it
            record = record.get(key)
            # Get rid of the first key since we have already used it to slice the record
            nested_keys_list.pop(0)
            # If we get to the end of the nested list of keys, break
            if len(nested_keys_list) == 0:
                break
            
            # Recursively call the function again, this time with a more targeted record slice
            partial_results = self.get_value_from_nested_dict(nested_keys_list, record)
            
            return partial_results
        
        return record