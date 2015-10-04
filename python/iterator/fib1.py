#!/bin/python
def fib(max):
	n, a, b = 0, 0, 1
	while n < max :
		print b
		a , b = a+b, a
		n = n + 1
	
if __name__ == "__main__":
	fib(10)
