#Python String
#It can be implemented by either single quotation marks,or double quotation marks
# 'Hello' is the same as "Hello"

#Get the character at position 1 (First character has the position 0)
a = "Python is the best"
print(a[1])

#Get the character from position  2 to position 8(not included)
b = "Python is the best"
print(b[2:8])

#strip() method removes any whitespaces from the beginning or the end
c = " Python is the best "
print(c.strip())

#len() method returns the length of a string
d = "Python is the best"
print(len(d))

#lower() method return the string in lower case
e = "Python Is The Best"
print(e.lower())

#upper() method return the string in upper case
f = "python is the best"
print(f.upper())

#replace() method replaces a string with another string:
g = "Python is the best"
print(g.replace("Python", "Apex"))

#split() method splits the string into substrings
h = "Python is the best"
print(g.split(" "))

