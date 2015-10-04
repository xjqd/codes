#!/bin/python
def hellocounter(name):
	count=[0]
	def counter():
		count[0]+=1
		#print 'hello ',name, str(count)," access!"
		print "hello %s, %d access\n" %(name, count[0])
	return counter
	
if __name__ == "__main__":
	hell=hellocounter("abc")
	hell()
	hell()
	hell()
