#!/bin/python
class A(object):

    def run(self):
        print "running in A"

class B(object):
    def run(self):
        print "running in B"
    

class C(object):
    def run(self):
        print "running in C"


class Facade(object):
    def __init__(self):
        self.a = A()
        self.b = B()
        self.c = C()
        self.test = [ i for i in (self.a, self.b, self.c) ]
    def runall(self):
        [ obj.run() for obj in self.test ]

if __name__ == "__main__":
    fa = Facade()
    print fa.test
    fa.runall()
