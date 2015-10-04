#!/bin/python
def hellocounter(name):
	count=0
	def counter():
		nonlocal count
		count +=1
		print "hello %s, %d access\n" %(name, count)
	return counter
	
if __name__ == "__main__":
	hell=hellocounter("abc")
	hell()
	hell()
	hell()
