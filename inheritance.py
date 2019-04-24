class Person:
	def __init__(self,name,age):
	    self.name=name
	    self.age=age
	def display(self):
	    print("Name",self.name)
	    print("Age"=self.age)
p=Person("John",32)
p.display()
class Teacher(Person):
	def __init(self,name,age,exp,r_area):
	    Person.__init__(self,name,age)
	    self.exp=exp
	    self.r_area=r_area
	def displaydata(self):
	    Person.display(self)
	    print("Experience:",self.exp)
            print("Research Area:",self.r_area)
class Student(Person):
	def __init__(self,name,age,course,marks):
	    Person.__init__(self,name,age)
	    self.course=course
	    self.marks=marks
	def displaydata(self):
	    Person.display(self)
	    print("Course:",self.course)
	    print("Marks:",self.marks)
print("***********Teacher*************")
T=Teacher("John",35,15,"Computer Network")
T.displaydata()
print("***********Student************")
S=Student("Raj",28,"BE COMP",79)
S.displaydata()
	