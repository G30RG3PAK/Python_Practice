#Set is a collection which is unordered and unindexed
pyset = {"A", "B", "C", "D", "E", "F", "G"}
print(pyset)

# it cannot be access items in set by referring to an index
# Set are unordered the items has no index!!


#Loop through the set items using a "for" loop
pyset = {"A", "B", "C", "D", "E", "F", "G"}
for i in pyset:
	print(i)

pyset = {"A", "B", "C", "D", "E", "F", "G"}
print("C" in pyset)


#Set cannot be changed its items, set can be add new items
pyset = {"A", "B", "C", "D", "E", "F", "G"}
pyset.add("H") # add an item
print(pyset)

pyset.update(["I", "J", "K", "L", "M", "N"])# add multiple items
print(pyset)

print(len(pyset)) # get number of items in  a set

# Remove an item in a set
# use remove(), or dicard() method
pyset.remove("A")# Error when item does not exist
pyset.discard("B")# NOT Error when item does not exist
print(pyset)

#pop() = remove last item(sets are unordered), you will not know what item that get removed
P = pyset.pop()
print(P)
print(pyset)

#clear() medtohd empties the set
pyset.clear()
print(pyset)

pyset = set(("A", "B", "C", "D", "E", "F", "G","I", "J", "K", "L", "M", "N"))
print(pyset)

del pyset
print(pyset)




