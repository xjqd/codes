#!/bin/python
f1 = lambda x, y : x+y
print f1(3,5)
# 三元表达式
a, b = 1, 2
h1 = a if a>b else b
h2 = (a if a>b else b)
h3 = a > b and [a] or [b]
h4 = (a < b and a or b)
print h1
print h2
print h3
print h4

