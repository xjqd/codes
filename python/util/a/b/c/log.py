#!/bin/python
import logging
import pdb
#pdb.set_trace()
print __name__
name="a"
ret = logging.getLogger(name)
name="a.b"
ret = logging.getLogger(name)
name="a.b.c"
ret = logging.getLogger(name)


if __name__ == "__main__":
    print __name__
    log = logging.getLogger(__name__)
    print  log
    
