from __future__ import unicode_literals
import sys
__future_module__ = True

if sys.version_info[0] == 3:
    raise ImportError('Cannot import module from python-future source folder')
else:
    from future.moves.html.parser import *
