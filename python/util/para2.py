#!/bin/python
x = 5
def outer(p1=None,x=40):
    print p1
    print x
    def inner(p1=None ):
        print p1
        #global x
        #x = x + 4
        print x+10
        y=x+80
        print y
    return inner

if __name__=="__main__":
    f=outer(10)
    f(20)
