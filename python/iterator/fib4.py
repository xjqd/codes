#!/bin/python
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b+a, a
		n+=1

# yield generator object list
if __name__=="__main__":
        f=fib(10)
	#print f, f.next(), f.next(), f.next()
	for e in f:
		print e
