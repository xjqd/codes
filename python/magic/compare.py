#!/bin/python
class Person:
	def __init__(self,name, age):
		self.name = name
		self.age = age
	def __cmp__(self, other):
		print "personal defination"
		if self.age < other.age:
			print "check < "
			return False

if __name__ == "__main__":
	p1 = Person("liming", 30)
	p2 = Person("zhangsan", 40)
	if p1  >  p2 :
		print "equal"
