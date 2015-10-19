#!/bin/python
class Animal(object):
    food="undefined"

class Bird(Animal):
    def sing(self):
        print "voice from bird"

class People(Animal):
    def sing(self):
        print "voice from people"
