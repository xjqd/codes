#!/bin/python
import handgun
import carbine
def pickup(clstype):
	if clstype == carbine.carbine: 
		return carbine.carbine()
	elif clstype == handgun.handgun:
		return handgun.handgun()
class gunFactory(object):
	def __init__(self, guntype):
		self.guntype = guntype
	def produce(self):
		print "type =%s" %self.guntype
		if self.guntype == carbine.carbine:
			return carbine.carbine()
		elif self.guntype == handgun.handgun:
			return handgun.handgun()

if __name__ == "__main__":
	pass
