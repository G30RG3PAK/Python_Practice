#Python Classes/Objects
class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def showname(self):
		print(self.firstname, self.lastname)

class Student(Person):
	pass
#Use the pass keyword when you do not want to add any other properties or methods to the class.
x = Student("Domminic", "Tomato")
x.showname()
 
