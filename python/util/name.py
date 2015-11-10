#!/bin/python
from a.b.c import log
import logging
import pdb
pdb.set_trace()
ret = logging.getLogger(__name__)
if __name__ == "__main__":
    print __name__
    print ret
