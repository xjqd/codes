#!/bin/python
import logging
import pdb
pdb.set_trace()
name="a"
ret = logging.getLogger(name)
name="a.b"
ret = logging.getLogger(name)
name="a.b.c"
ret = logging.getLogger(name)
print ret
print __name__
log = logging.getLogger(__name__)
print  log
