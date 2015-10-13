#!/bin/python
class OnlyOne(object):
    __instance = None
    def __init__(self ):
        pass
    #看到cls做为参数的好处了吧
    @classmethod
    def getinstance(cls):
        print cls
        print dir(cls)
        if not cls.__instance:
            cls.__instance=OnlyOne()
        return cls.__instance
    def __str__(self):
        return repr(self) + "name"

if __name__=="__main__":
    t1=OnlyOne.getinstance()
    t2=OnlyOne.getinstance()
    print t1
    print t2
