#!/bin/python
import base

class Factory(object):
    @classmethod
    def create(cls, type=None):
        if type=="bird":
            return base.Bird()
        elif type=="people":
            return base.People()

class SimpleFactory(Factory):
    pass

if __name__ == "__main__":
    cls1 = SimpleFactory.create(type="bird")
    cls1.sing()
    print dir(cls1)
    print dir(SimpleFactory)

