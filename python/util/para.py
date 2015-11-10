#!/bin/python
def outer(p1=None):
    print p1
    def inner(p2=None):
        print p1
        print p2
    return inner

if __name__=="__main__":
    f=outer(10)
    f(20)
