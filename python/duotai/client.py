#!/bin/python
import server

def client(gun):
	if hasattr(gun,"fire"):
		gun.fire()

if __name__ == "__main__":
	# style - 1
	client(server.carbine.carbine())
	#client(handgun())
	client(server.handgun.handgun())
	# style - 2
	retObj = server.pickup(server.carbine.carbine)
	client(retObj)
	retObj = server.pickup(server.handgun.handgun)
	client(retObj)
	# style - 3
	# add the double quote or not , it's two different types
        # one is string
	# one is class
	# factory = gunFactory("handgun.handgun")
	factory = server.gunFactory(server.handgun.handgun)
	gun = factory.produce()
	client(gun)
	# not work but no error
	li = [1, 2]
	client(li)
