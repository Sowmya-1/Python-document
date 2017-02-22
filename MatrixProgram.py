class A:
	def __init__(self):
		mat=[]
		for i in range(3):
			row=[]
			for j in range(3):
				v=input("enter")
				row.append(v)
			lis.append(row)
		mat1=[]
		for i1 in range(2):
			row1=[]
			for j1 in range(2):
				v1=input("enter")
				row1.append(v1)
			lis1.append(row1)
		mat2=[]
		print row
		print row1
		for k in range(2):
			row2=[]
			for m in range(2):
				v=row[k][m]+row1[k][m]
				print row[m]
				print row1[m]
				row2.append(v)
			mat2.append(row2)
		print row
		print mat2
a=A()
