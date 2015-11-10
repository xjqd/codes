#!/bin/python
def outer_f(f=None):
    print "out_f"
    print f

@outer_f
def inner():
    print "inner"

if __name__ == "__main__":
    t = inner
    print "t=", t
    print "========="
    print outer_f(inner)
