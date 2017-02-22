class Rectangle:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def area(self):
		print 'area:',+(self.a*self.b)
	def perimeter(self):
		print 'perimeter:',+2*(self.a+self.b)
	def __add__(self,other):
		return Rectangle(self.a+other.a, self.b+other.b)
