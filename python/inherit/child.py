#!/bin/python
import base
class child(base.Base):
	def __init__(self, name, age, salary):
		print self
		#base.Base.__init__(self, name, age)
                # if class is not inherited from object, it will get error
                # TypeError: must be type, not classob
		super(child, self).__init__(name, age)
		self.salary = salary
		print "child class is initilized\n"
	def talk(self):
		print "child's salary :%d" %salary

if __name__ == "__main__":
	ch = child("Liming", 30, 100)
	print ch.name

