#!/bin/python
def h1():
    print "begining..."
    yield 
    print "second..."
    m = yield 10
    print "checking after second..."
    print m

if __name__ == "__main__":
    import pdb
    pdb.set_trace()
    t = h1()
    #for i in t:
    #    print i
