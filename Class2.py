class A:
	def __init__(self,a):
		self.a=a
	def __add__(self,other):
		return self.a+other.a
	def __sub__(self,other):
		return self.a-other.a
m=A(10)
n=A(20)
print m-n

