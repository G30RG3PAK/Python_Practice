#Python Condition(If-Statement/Loops)
"""Logical Condition
	Equals: a == b
	Not Equal: a != b
	Less Than: a < b
	Less Than or equal to: a <= b
	Greater Than: a > b
	Greter Than or Equal to: a >= b """

a = 151
b = 160
if b > a: # Using white space to define scope in the code
	print("b is greater than a")

# elif keyword = if previous conditions were not true, then go to this condition
c = 55
d = 50
if b > a:
	print("b is greater than a")
elif a == b:
	print("a and b are equal")
else: # execute anything that is not caught by the prededing conditions 
	print(" a is greater than b")

#Short Hand if-Statement
# if a > b: print("a is greater than b")
# print("A") if a > b else print("B")
# print("A") if a > b else print("=") if a == b else print("B")

#AND = logical operator, and is used to combined conditional statement
i = 77
j = 55
k = 88
if i > j and k > i:
	print("All condition are True")

#OR = logical operator, and is used to combined conditional statement
i = 44
j = 33
k = 22
if i > j or i > k:
	print("At least one of the condition is True")

