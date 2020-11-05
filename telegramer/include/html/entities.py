from __future__ import unicode_literals
from future.utils import PY3

if PY3:
    from html.entities import *
else:
    from future.moves.html.entities import *
