#!/bin/python
li = [x*x for x in range(4)]
print li
li = { x*x for x in range(4) }
print li
li = {x:x+3 for x in range(4) }
print li

li = lambda y: y+3
print li(5)

#li = sum(x*x for x in range(4))
li = sum([x*x for x in range(4)])
print li

a = 1
b = 2
li = a if a>b else b
print li
