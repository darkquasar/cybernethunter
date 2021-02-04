'''
 MODULE NAME: huntmod_template.py | Version: 0.1
 CYBERNETHUNTER Version: 0.1
 AUTHOR: Diego Perez (@darkquasar) - 2018
 DESCRIPTION: This module will load hunting templates and execute them against an ElasticSearch database via Apache Spark. It should be called from within CYBERNETHUNTER-jupyter
'''

import logging
import pyspark
import sys

# Ugly but workable importing solution so that the package can be both 
# imported as a package, run from commandline with `python -m cyberhunter`
# or from the source directory as `python cyberhunter.py`
if "cybernethunter" in sys.modules:
    from cybernethunter.parsermods import multiparser as mp
else:
    from parsermods import multiparser as mp
    


# All parsermods have a class called "mod" and define
# any initialization parameters inside.
# Parsermods can have any number of functions inside the "mod" class.
class mod:
    def __init__(self, xmlparsetype, logtype, filepath, output, **kwargs):
        
        # Setup logging
        # We need to pass the "logger" to any Classes or Modules that may use it 
        # in our script
        try:
            import coloredlogs
            self.logger = logging.getLogger('CYBERNETHUNTER.HUNTMOD')
            coloredlogs.install(fmt='%(asctime)s - %(name)s - %(message)s', level="DEBUG", logger=self.logger)

        except ModuleNotFoundError:
            self.logger = logging.getLogger('CYBERNETHUNTER.HUNTMOD')
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            console_handler.setLevel(logging.DEBUG)
            self.logger.addHandler(console_handler)
            self.logger.setLevel(logging.INFO)
  
        # Initializing variables
        self.xmlparsetype = xmlparsetype
        self.logtype = logtype
        self.filepath = filepath
        self.output = output

    # All parsermods must contain an "execute" function that will: 
    # a. initialize the output pipe via de MultiParser "init_output" func.
    # b. return a generator back to CYBERNETHUNTER.py so that records can be iterated through.
    def execute(self):
        # Instantiating the MultiParser for plain parsing (no modules)
        self.fileparser = mp.MultiParser(self.xmlparsetype, self.logtype, self.filepath)
        results = self.fileparser.parser()
        self.fileparser.init_output(self.output, self.logtype)
    
        return results