#!/bin/python
import time
from collections import Counter, deque, defaultdict
num=1000
li = ['Dog', "cat", "mouse", 42, "Dog", 42, "Cat"]
a = Counter(li)
print type(a)
print len(set(li))
def append(c):
    if isinstance(c, deque):
        for i in range(num):
            c.append(i)

def appendleft(c):
    if isinstance(c, deque):
        for i in range(num):
            c.appendleft(i)
    else:
        for i in range(num):
            c.insert(0,i)

def pop(c):
    for i in range(num):
        c.pop()

def popleft(c):
    if isinstance(c,deque):
        for i in range(num):
            c.popleft()
    else:
        for i in range(num):
            c.pop(0)

for container in [deque, list]:
    for operator in [append, appendleft, pop, popleft]:
        c = container(range(num))
        start=time.time()
        operator(c)
        elapsed=time.time()-start
        print "completed {0}/{1} in {2} seconds: {3} ops/sec".format(container.__name__, operator.__name__, \
                elapsed, num/elapsed)


q = deque(range(5))
print q
q.append(5)
print q
q.appendleft(-1)
print q
q.pop()
print q
q.popleft()
print q

s = "the quick brown fox jumps over the lazy dog"
words = s.split()
location=defaultdict(list)
for m, n in enumerate(words):
    location[n].append(m)
print location

d={}
for key, value in enumerate(words):
    d.setdefault(key, []).append(value)
print d

