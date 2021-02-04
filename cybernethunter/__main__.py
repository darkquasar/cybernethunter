from __future__ import absolute_import

import os
import sys

# If we are running with `python -m cybernethunter`
# Add the current dir to the PATH env so as to make CyberNetHunter available as a package
if __package__ == '':
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)

from . import cybernethunter_cli as cycli

if __name__ == '__main__':
    sys.exit(cycli.main())