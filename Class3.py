class S:
	def __init__(self,a):
		self.a=a
	def __add__(self,other):
		return self.a+other.a
	def __sub__(self,other):
		return self.a-other.a
a=S(10)
b=S(20)
print a+b
print a-b

