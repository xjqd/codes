#!/bin/python 
class Base(object):
	def __init__(self, name, age):
		print self
		self.name = name
		self.age = age
		print "Base is initialized\n"
	def speak(self, name):
		print "base class is speak %s" %name

if __name__ == "__main__":
	Li = Base("liming",20)
