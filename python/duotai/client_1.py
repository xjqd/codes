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
def client(gun):
	gun.fire()

if __name__ == "__main__":
	# style - 1
	client(carbine.carbine())
	#client(handgun())
	client(handgun.handgun())
	# style - 2
	retObj = pickup(carbine.carbine)
	client(retObj)
	retObj = pickup(handgun.handgun)
	client(retObj)
	# style - 3
	# add the double quote or not , it's two different types
        # one is string
	# one is class
	# factory = gunFactory("handgun.handgun")
	factory = gunFactory(handgun.handgun)
	gun = factory.produce()
	client(gun)
