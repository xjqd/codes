#!/bin/python
class outer:
	out_1 = "outer"
	def __init__(self, value):
		self.value = value
	class inner:
		inner_1 = "inner"
		def __init__(self, name):
			self.name = name

if __name__ == "__main__":
	inn = outer.inner("neibu")
	print inn.name
	inn2 = outer(2).inner("neibu2")
	print inn2.name
	inn3 = outer.inner("neibu3")
	print inn3.name
	out = outer(3)
	inn4 = outer.inner("neibu4")
	print inn4
	print "==="*5
        print outer
	print outer.inner
	print type(outer)
	print type(outer.inner)
	print type(out.inner)
	# wrong no this innder 
        #print inner 
