#!/bin/python
class MathProxy(object):
    # do we need a reference to the Math class/ obj
    def __init__(self):
        self._math = Math()

    def add(self, x, y):
        return self._math.add(x,y)

class Math(object):
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y
