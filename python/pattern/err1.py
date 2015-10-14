#!/bin/python
class Foo(object):

    def __init__(self, val):
        self.val = val

    def level1(self):
        print self.val

    def level2(self):
       self.level1()

    @classmethod
    def method(cls):
        #NameError: global name 'self' is not defined
        #cls.level2(self)
        cls(10).level2()

if __name__ =="__main__":
    f = Foo(3)
    f.level1()
    f.level2()
    #f.method()
    #TypeError: unbound method level2() must be called with Foo instance as first argument (got nothing instead)
    Foo.method()

