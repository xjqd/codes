#!/bin/python
def h():
    print "begining..."
    m = yield 5
    print "checking retrun value..."
    print m
    print "middle ...."
    m = yield 10
    print m
    print "ending ...."
    m = yield 15
    print m
