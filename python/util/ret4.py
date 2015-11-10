#!/bin/python
from functools import wraps
# return self make dead-loop
def f1():
    print "f1"
    def f2():
        print "f2"
        return f2
    return f1

# callback use the stype x1()()
def x1():
    print "x1"
    def x2():
        print "x2"
    return x2

def y2():
    print "y2"
#use the style y1(y2)
def y1(y2=None):
    print "y1"
    y2()

#def z1(z=None):
    #print "z1"
    #return z

def z1_v0(z=None):
    print "z1"
    def name1():
        #print z
        z()
    return name1

def update_name(func):
    print 'outer update_name'
    def new_func(ff=None):
       print "inner update name" 
       wrapper = func
       #wrapper.__name__ = func.__name__
       print dir(wrapper)
       print wrapper.__name__
       return func()
    new_func.func = func
    print new_func.func
    return new_func 

def z1(z=None):
    print "outer z1"
    #def name1(z=None):
    #@wraps(z)
    @update_name(z)
    def name1(z=None):
        #print z
        print "researh.."
        #name1.func_name = z.func_name
        print name1.func_name
        z()
        return "abc"
    return name1
@z1
def z2():
    print "z2"

def f10():
    print "f10"
    return f10 

def f9():
    print f9
    return f9

if __name__ =="__main__":
    print "XXXXXXXX"
    t=x1()()
    print t
    print "YYYYYYYY"
    t=y1(y2)
    print t
    print "ZZZZZZZZ"
    t = z2
    print dir(t)
    #print t.func_name
    print "t=", t

    print "\n"
    t = f1
    print "t=",t
    t1 = f1()
    print "t1=",t1
    t2 = t1()
    print "t2=",t2
    print "================="
    t10 = f10
    print "t10=",t10
    print "t10=", t10()

    t9 = f9()
    print t9
