#!/bin/python

class Strategy(object):
    def __init__(self, instance=None):
        self.instance = instance
    def travel(self):
        if hasattr(self.instance, "fly"):
            self.instance.fly()


class Duck(object):
    def bark(self):
        print "Duck bark"

class Bird(object):
    def fly(self):
        print "Bird fly"

if __name__ == "__main__":
    s=Strategy(Bird())
    s.travel()
    s=Strategy(Duck())
    s.travel()
