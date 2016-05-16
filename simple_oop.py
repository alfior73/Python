#simpleoop.py

# simple fibonacci series
# the sum of two elements defines the next set
class Fibobacci():
	"""docstring for Fibobacci"""
	def __init__(self, a, b):
		#super(Fibobacci, self).__init__()
		self.a = a
		self.b = b
		pass

	def series(self):
		while (True):
			yield(self.b)
			self.a, self.b = self.b, self.a + self.b
			pass
		
f = Fibobacci(0, 1)

for r in f.series():
	if r > 100: break
	print(r, end=' ')
