#!/usr/bin/env python3

'''
 NAME: notebook.py | version: 0.1
 CYBERNETHUNTER Version: 0.3
 AUTHOR: Diego Perez (@darkquasar) - 2020
 DESCRIPTION: Script to facilitate the conversion of YAML playbooks to iPython Notebooks
    
 Updates: 
        v0.1 - 05-10-2020 - Created script.
    
 ToDo:
        1. ----.

'''

import logging
import nbformat as nbf
import os
import pandas as pd
import re
import sys
import yaml
from pathlib import Path
from tomark import Tomark

from cybernethunter.helpermods import utils

class HelperMod:

    def __init__(self):
        
        # Setup logging
        utilities = utils.HelperMod()
        self.logger = utilities.get_logger('CYBERNETHUNTER.HELPERS.PLAYBOOK')
        
    def read_yaml(self, file_name):
        with open(file_name, encoding='utf-8') as yf:
            t = yaml.load(yf, Loader=yaml.FullLoader)
        return t
    
    def create_notebook(self, yaml_playbook):
        
        # Define notebook metadata
        nb_meta:    {
                        "metadata": {
                            "extensions": {
                            },
                            "kernelspec": {
                                "display_name": "Python 3",
                                "language": "python",
                                "name": "python3"
                            },
                            "language_info": {
                                "codemirror_mode": {
                                    "name": "ipython",
                                    "version": 3
                                },
                                "file_extension": ".py",
                                "mimetype": "text/x-python",
                                "name": "python",
                                "nbconvert_exporter": "python",
                                "pygments_lexer": "ipython3",
                                "version": "3.7.9"
                            }
                        }
                    }
        
        # Append other metadata stored in the playbook
        nb_meta['metadata']['playbook'] = yaml_playbook['playbook_meta']
        
        # Create notebook
        nb = nbf.v4.new_notebook(metadata=nb_meta)
        nb['cells'] = []
        
        # Add Title
        nb['cells'].append(nbf.v4.new_markdown_cell('# {}'.format(yaml_playbook['title'])))
        
        # Add Attack maps
        df = pd.DataFrame(yaml_playbook['attack']).T.rename(columns={0: ''})
        df_md_table = df.to_markdown()
        nb['cells'].append(nbf.v4.new_markdown_cell(df_md_table))
        
        # Add Timestamp
        df = pd.DataFrame([t['playbook_meta']['timestamp']]).T.rename(columns={0: ''})
        df_md_table = df.to_markdown()
        nb['cells'].append(nbf.v4.new_markdown_cell(df_md_table))
        
        # Add Preamble
        nb['cells'].append(nbf.v4.new_markdown_cell('# {}'.format(yaml_playbook['title'])))
        
        # Add Generic Sections
        
        # Add Analytics
        