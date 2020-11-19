from __future__ import absolute_import

import os
import sys

# If we are running with `python -m cybrhunter`
# Add the current dir to the PATH env so as to make CybrHunter available as a package
if __package__ == '':
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)

from . import cybrhunter_cli as cycli

if __name__ == '__main__':
    sys.exit(cycli.main())