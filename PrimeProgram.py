class P:
	def __init__(self,a):
		self.a=a
	def prime(self):
		v=input("Enter the Range")
		count=1
		for i in range(2,100):
			flag=1
			for j in range(2,i/2):
				if(i%j==0):
					flag=0
			if flag==1:
				count=count+1
				print i
			if count==self.a:
				break

a=p(10)
a.prime()
