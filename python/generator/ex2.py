#!/bin/python
class CountDown(object):
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def next(self):
        if self.start <= 0:
            raise StopIteration
        r = self.start
        self.start -= 1
        return r
def countdown(n):
    while n > 0:
        print "iteration from ", n
        m = yield "hello"
        print m
        n = n-1

if __name__ == "__main__":
    for x in CountDown(5):
        print x

    import pdb
    pdb.set_trace()
    #for i in countdown(5):
    #    print i
    f = countdown(5)
    f.next()
    f.send("nihao")
    f.send("world")
    #for i in f.send("nihao"):
    for i in f:
        print i
    
