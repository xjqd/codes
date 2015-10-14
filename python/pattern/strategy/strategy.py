#!/bin/python
import types

class Strategy(object):
    
    def __init__(self, func=None):
        self.name = " default strategy "
        if func is not None:
            self.execute=types.MethodType(func, self)

    def execute(self):
        print self.name

def func1(a):
    print "change by func1" + a.name

def execute_replace(self):
    print self.name + "from execute_replace"

if __name__ =="__main__":
    s=Strategy()
    s.execute()
    # case-1
    s=Strategy(func1)
    s.execute()
    #case -2
    s2 = Strategy(execute_replace)
    s2.execute()
