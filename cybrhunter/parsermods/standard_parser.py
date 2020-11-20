'''
MODULE NAME: standard_parser.py | Version: 0.3
CYBRHUNTER Version: 0.3
AUTHOR: Diego Perez (@darkquassar) - 2018
DESCRIPTION: This is the default module executed when no particular parser mod is passed to cybrhunter.py.
It can be used as a template of how parser mods should be construed. The default module prints results back to stdout in json format.
'''

import logging

# All parsermods have a class called "parsermod" and define
# any initialization parameters inside.
# Parsermods can have any number of functions inside the "parsermod" class.
class ParserMod():

    def __init__(self, log_type, file_path=None, **kwargs):

        # Setup logging
        # We need to pass the "logger" to any Classes or Modules that may use it 
        # in our script
        try:
            import coloredlogs
            self.logger = logging.getLogger('CYBRHUNTER.PARSERS.CSV')
            coloredlogs.install(fmt='%(asctime)s - %(name)s - %(message)s', level="DEBUG", logger=self.logger)

        except ModuleNotFoundError:
            self.logger = logging.getLogger('CYBRHUNTER.PARSERS.CSV')
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            console_handler.setLevel(logging.DEBUG)
            self.logger.addHandler(console_handler)
            self.logger.setLevel(logging.INFO)

        # Initializing variables
        self.logger.info('Initializing {}'.format(__name__))
        self.log_type = log_type
        self.file_path = file_path

    # All parsermods must contain an "execute" function that will initiate the parsing action on each 
    # record. Other functions can be defined in this module that do the actual heavy lifting
    # whilst the "execute" function only calls them for code clarity. In the case of the current
    # module we call Multiparser (another parsermod) and use its results. The function should return
    # a generator back to the calling module (like cybrhunter.py) so that records can be iterated through.
    def execute(self):

        # Instantiating the Parser
        self.parser = "some mod instance"
        self.results = "stuff"

        return self.results