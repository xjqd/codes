#!/bin/python
def outer(p1=None):
    print p1
    def inner(p1=None):
        print p1
    return inner

if __name__=="__main__":
    f=outer(10)
    f(20)
