class A:
	def __init__(self,array):
		self.array=array
		list=[]
		for i in range(3):
			row=[]
			for j in range(3):
				m=input("enter")
				row.append(m)
			list .append(row)
	def __add__(self,other):
		return self.list+other.list
a=A()
b=A()
print a+b
