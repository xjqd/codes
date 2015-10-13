#!/bin/python
class OnlyOne(object):

    instance=None

    class __OnlyOne(object):
        def __init__(self, val):
            self.val = val

        def __str__(self):
            return repr(self)+self.val

    def __init__(self,arg):
        if (not OnlyOne.instance) :
            print "once"
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)  
        else:
            OnlyOne.instance.val = arg


if __name__ == "__main__":
    t1 = OnlyOne("egg")
    print t1.instance.val
    print t1.instance
    t2 = OnlyOne("cabbige")
    print t2.instance.val
    print t2.instance
    t3 = OnlyOne("milk")
    print t3.instance.val
    print t3.instance
    



