class Polygon:
	def __init__(self):
           pass
	def getarea(self):
           pass
class Rectangle(Polygon):
	def __init__(self,length,breadth):
	   self.length=length
	   self.breadth=breadth
	def getarea(self):
	   return self.length*self.breadth
class Square(Polygon):
	def __init__(self,side,side1):
	   self.side=side
	   self.side1=side1
	def getarea(self):
	   return self.side*self.side1
print("Enter Length and Breadth")
l,b=map(int,input().split())
r=Rectangle(l,b)
print("Area of Rectangle is=",r.getarea())
s=Square(l,l)
print("Area of Square is=",s.getarea())