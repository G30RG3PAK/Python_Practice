#Dictionaries is a collection that is unordered, changeable and idexed.
pydict = {
	"brand": "Apple",
	"model": "Pro",
	"year" : 2019
}
print(pydict)

#Accessing item in dict  by referring to its key name , inside squre brackets
i = pydict["model"]
print(i)
#OR
u = pydict.get("year")
print(u)

#Change values of specific item by referring to its key name
pydict["year"] = 2017
print(pydict)

#Loop through a dictionary (for)
for x in pydict:
	print(x) # return key of the dictionary


for x in pydict:
	print(pydict[x]) # return all value in the dictionary (on by one)

for x in pydict.values(): #use value()  to return values of a dict
	print(x)

for x, y in  pydict.items(): #use item() return keys and values
	print(x, y)

if "brand" in pydict:
	print("Yes, it is one of the keys in the dictionary")

#Show number of item in the dict
print(len(pydict))

#Add  item to the dict
pydict["color"] = "Blue"
print(pydict)

#Remove item from a dictionary
pydict.pop("brand")#remove the item with key name
pydict.popitem() #remove the last inserted item
print(pydict)

del pydict["year"] #remove the item with key name
print(pydict)

pydict.clear()# empties the dict
print(pydict)

pydict = dict(brand="Dell", model="XPS", type="15")
print(pydict)