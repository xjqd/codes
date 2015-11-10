#!/bin/python
def outer():
    print "out"
    def inner():
        print "inner"
    return inner

def outer_f(f=None):
    print "out_f"
    def inner(f=None):
        print inner_f
        f()
    return inner

def study():
    print "need to study"

if __name__ == "__main__":
    f1 = outer
    print "f1=", f1
    f2 = outer()
    print "f2=", f2
    f3 = f2()
    print "f3=", f3
