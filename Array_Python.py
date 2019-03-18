#Python Array --> store multiple values in single variable
#Python doesn't have built-in support for Arrays
#Python Lists can be used instead
laptop = ["Dell", "Macbook", "Asus"]
print(laptop)
print("//////////")

x = laptop[0]#Access element of Array
print(x)
print("//////////")

laptop[2] = "Lenovo"#Modify value of the array
print(laptop)
print("//////////")

array_length = len(laptop)#Return number of elements in the array
print(array_length)
print("//////////")
#Length of an array is always one more than the highest array index.

for i in laptop:#Looping array element
	print(i)

print("//////////")

laptop.append("Asus")#Adding array element
print(laptop)
print("//////////")

laptop.pop()#Remove element of the array
print(laptop)
print("//////////")

laptop.remove("Lenovo")#Remove specified value of the array
print(laptop)

#Python has a set of built-in methods that you can use on lists/arrays.





