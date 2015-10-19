#!/bin/python
class WinBas(object):
    def __init__(self):
        self.__baselist = {}
        self.__init_modules()

    def __init_modules(self):
        import modplugs
        for m in modplugs.__moduleset__:
            print m
            mh = __import__('modules.'+ m)
            print "mh", type(mh), dir(mh)
            ma = getattr(mh, m)
            print "ma", ma
            ma = getattr(ma, m)
            print ma
            setattr(self.__class__, m, ma)

if __name__ == "__main__":
    w = WinBas()
