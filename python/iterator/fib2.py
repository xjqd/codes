#!/bin/python
def fib(max):
	l=[]
	n, a, b = 0, 0, 1
	while n < max :
		a , b = a+b, a
		n = n + 1
		l.append(b)
	return l
	
if __name__ == "__main__":
	print fib(10)
