#Python Classes/Ojects
#Python is OOP
#Class is object constructor
class FirstClass: # Create a Class
    x = 20 # property


#Create Object
Ob1 = FirstClass() #Use the FirstClass to create objects 
print(Ob1.x) 

#The _init_() Function(in All Classes)
#Always executed when the class is being initiated
#Use to assign values to object properties

class Person:# don't have to named "self", but it has to be the first parameter of any function in the class
    def __init__(self, name, age):
        self.name = name
        self.age = age
#self parameter is a reference to the class instance itself
#and is used to access variables that belongs to the class
    
    def namefunc(self): #method in object are functions that belongs to the object
        print("Hello my name is " + self.name) 
        print("I'm " + self.age + " years old")

per1 = Person("George", "22")
print(per1.name)
print(per1.age)
per1.namefunc()

#__init__() is called automatically every timethe class is being used to create a new object

