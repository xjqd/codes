#!/bin/python
import base
class child(base.Base):
	def talk(self):
		print "child's salary :%d" %salary

if __name__ == "__main__":
	ch = child("Liming", 30)
	print ch.name

