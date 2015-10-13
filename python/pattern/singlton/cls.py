#!/bin/python
class Num(object):
	num = 0
	def __init__(self, val):
                print "hello"
		self.val = val
		Num.num = Num.num + 1

	def prin(self):
		print "checking Num:{0},instance:{1}".format(Num.num, self.val)

exp=Num(10)
