#!/bin/python
def outer(out):
	def inner(inner):
		return out + inner
	return inner

if __name__=="__main__":
	p = outer(20)
	q = outer(30)
	print p
	print p(100)
	print q(100)
