class Fib(object):
	def __init__(self, max):
		self.max = max
		self.a, self.b, self.n = 0,1,0
	def __iter__(self):
		return self
	def next(self):
		if self.n < self.max:
			r = self.b
			self.a, self.b = self.b+self.a, self.a
			self.n += 1
			return r
		raise StopIteration()

if __name__ == "__main__":
	f=Fib(10)
	print f
	try:
		while True:
			print f.next()
	except	StopIteration:
		pass

	for f in Fib(10):
		print f
