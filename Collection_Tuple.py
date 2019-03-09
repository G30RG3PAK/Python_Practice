#tuple is a collection which is ordered and unchangeable.
pytuple = ("Hello", "Hi", "Good", "Bye", "Coding")
print(pytuple) #print tuple
print(pytuple[1])#access tuple item by referring to the index number


#Loop through the tuple items
pytuple = ("Hello", "Hi", "Good", "Bye", "Coding")
for i in pytuple:
	print(i)

#Check specific item is exists in a tuple?
pytuple = ("Hello", "Hi", "Good", "Bye", "Coding")
if "Hi" in pytuple:# use 'in' keyword to determine item in tuple
	print("Yes, it is in the tuple")

#Use len() method to determine how many items in a tuple 
pytuple = ("Hello", "Hi", "Good", "Bye", "Coding")
print(len(pytuple))

#Constructor the tuple()
#use tuple() constructor to make a tuple
pytuple = tuple(("Hello", "Hi", "Good", "Bye", "Coding"))
print(pytuple)

#Count() method return number of times the value in the tuple
numtuple = (1, 2, 2, 3, 6, 8, 4, 1, 2, 5, 2)
c = numtuple.count(2)
print(c)

#Tuple are unchangeable
pytuple[2] = "Hola"
#values will remain the same
print(pytuple)
#Tuple cannot add items to it/remove items from it.(unchangeable)
#But you can delete the tuple completely --> del pytuple --> show error because tuple no longer exists

