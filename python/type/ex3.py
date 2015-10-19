#!/bin/python
class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)

class Meta(object):
    name = "jian"
    def __init__(self):
       self.name = "xue"
       self.age = 30

    __metaclass__ = UpperAttrMetaclass

if __name__ == "__main__":
    m = Meta()
    print dir(m)
    print dir(type(m))
    #wrong print  m.name
    #wrong print m.age 
    print Meta.NAME
    print m.NAME
    # print m.AGE 
    # age must be in the attribute of the class, not the object
