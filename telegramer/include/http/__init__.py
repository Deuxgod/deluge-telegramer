from __future__ import unicode_literals
import sys

if sys.version_info[0] < 3:
    pass
else:
    raise ImportError('This package should not be accessible on Python 3. '
                      'Either you are trying to run from the python-future src folder '
                      'or your installation of python-future is corrupted.')
