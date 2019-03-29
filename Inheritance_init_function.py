#Python Classes/Objects
class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def showname(self):
		print(self.firstname, self.lastname)

class Student(Person):#child class will no longer inherit the parent's init function
	def __init__(self, fname, lname):#instead of the pass keywoed
		Person.__init__(self, fname, lname) # keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
#Student's __init__() function overrides the inheritance of the parent's __init__()
x = Student("Rockie", "Romanov")
x.showname()
