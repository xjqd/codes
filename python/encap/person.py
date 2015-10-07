#!/bin/python
class Person(object):
	count = 0
	def __init__(self, name, age):
		self.name = name
		self.__age = age
		# local variable 'count' referenced before assignment
		# wrong count += 1
		self.count = Person.count + 1
	@classmethod
	def printNum(abc):
		print "count=%s" %abc.count

	#def printNum(self):
		#print "count=%s" %self.count

	def test(self):
		Person.printNum()
	@property
	def age(self):
		return self.__age
	@age.setter
	def age(self, val):
		self.__age = val

if __name__ == "__main__":
	p = Person("liming", 30)
	#Person.printNum()
	p.printNum()
	p.test()
	# Person' object has no attribute '__age'
	#p.__age
	print p.age
	p.age = 40
	print p.age
