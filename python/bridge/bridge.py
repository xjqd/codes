#!/bin/python
class DrawApiOne(object):
    def draw_circle(selfi, x, y, radius):
        print "ApiOne.circle at {}:{} radius{}".format(x, y, radius)

class DrawApiTwo(object):
    def draw_circle(selfi, x, y, radius):
        print "ApiTwo.circle at {}:{} radius{}".format(x, y, radius)

class Bridge(object):
    def __init__(self, x,y, radius, drawapi):
        self.x = x
        self.y = y
        self.radius = radius
        self.drawapi = drawapi()

    def draw(self):
        self.drawapi.draw_circle(self.x, self.y, self.radius)

class client(object):
    def __init__(self, bridge):
        self.bridge = bridge

if __name__ == "__main__":
    c1 = client(Bridge(1,2, 3,DrawApiOne))
    c1.bridge.draw()
    c2 = client(Bridge(4,5, 6,DrawApiTwo))
    c2.bridge.draw()
