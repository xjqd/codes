#!/bin/python
#-*- utf-8  -*-
# list中存放的类型是可比较的。否则就会弹出错误“Type Error: unorderable type"
# lambda 是个表达式，是个匿名函数。不适用于循环中的操作
# a = lambda x, y : x+y
# a()

# key 只能有一个参数
# cmp 可以有两个参数
class Interval(object):
    def __init__(self, s=0, e=0):
        self.s = s 
        self.e = e

def check(a, b):
    if a.s != b.s:
        return cmp(a.s, b.s)
    return cmp(a.e, b.e)

if __name__ == "__main__":
    li = []
    for i in range(10, 7, -1):
        for j in range(11, i, -1):
            li.append(Interval(i,j))
    print li
    #li.sort()
    l2 = sorted(li, key=lambda x:x.s)
    print l2
    l3 = sorted(li, key=lambda x:(x.s, x.e))
    print l3
    l4 = sorted(li, cmp=check)
    print l4
    #l5 = sorted(li, key=check)
    l5 = sorted(li, cmp=lambda x:x.s)
    print l5

    d = {'a':2, 'b':23, 'c':5, 'd':17, 'e':1}
    print sorted(d, key=d.__getitem__,reverse=True)
