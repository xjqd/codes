#!/bin/python
def f1(f2=None):
    print f1.func_name
    #print dir(f1)
    def f3():
        """ 
            f3 function
        """
        print "f3"
    print f3
    f3.func_name = f2.func_name
    f3.__doc__ = f2.__doc__
    return f3

def sub():
    """doc sub
    """
    print 'sub=', sub
    print "sub"

def add():
    print add
if __name__ == "__main__":
    print sub
    t = f1(sub)
    print t.func_name
    print t
    print t.__doc__
    add()
