#!/bin/python
import cls
t1 = cls.exp
class T1(object):
   
	def check_cls(self):
		print cls.Num.num
		print t1.num

if __name__ == "__main__":
	t=T1()
        t.check_cls()
