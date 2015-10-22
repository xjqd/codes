#!/bin/python
print max([1,2,3])
print min([4,5,6])
print cmp(1,2)
print len([1,2,3])
print range(10)
print xrange(10)
print list("hello world")
print str("abc")
print zip([1,2,3],[4,5,6,7])
f = enumerate(['a','b','c'])
print f.next()
print "iterator----------"
def getrand():
    import random
    return random.randint(1,100)
for i in iter(getrand,50):
    print i
print "filter----"
def check(x):
    return False if x%2 else True
print filter(check, [1,2,3,4,5,6,7,8,9])
print "map----"
def cube(x):
    return x*x*x
print map(cube,[1,2,3,4,5,6,7,8,9])
print map(check,[1,2,3,4,5,6,7,8,9])
def add(x,y):
    return x + y
print map(add,[1,2,3,4],[5,6,7,8])
print "reduce----"
print reduce(add,[1,2,3,4])
print reduce(add,[1,2,3,4],10)
print reduce(add, filter(lambda x:5 if not x%2 else 0,[1,2,3,4,5,6,7,8,9]))
