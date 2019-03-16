#For Loop Python

laptop = ["Dell", "Mac", "Hp", "Asus"] # List
for x in laptop:
	print(x)
#For loop does not require an indexing variable to set beforehand.
print("////////////////////////")
#Looping Through a String
for i in "international": #String is iterable objects(sequence of characters)
	print(i)
#loop through and print the letter in the word "international"
print("////////////////////////")
#Break Statement
team1 = ["Navi", "Secret", "OG", "Newbee"]
for t in team1: # print "OG" then break
	print(t)
	if t == "OG": # Exit loop when t is "OG"
		break
print("////////////////////////")

team2 = ["EG", "Secret", "OG", "LGD"]
for j in team2:
	if j == "OG": # break before the print
		break
	print(j)
print("////////////////////////")

#Continue Statement
team3 = ["EG", "Secret", "OG", "LGD", "Navi", "Newbee"]
for y in team3:
	if y == "OG":
		continue
	print(y)
print("////////////////////////")

#range() = loop through a set of code a specified umber of times
for x in range(10): #not the values of 0-10, but 0-9
	print(x) 
	#return a sequence of number (starting from 0 by default)
	#increment by 1, and ends at a specified number

print("////////////////////////")
for x in range(2, 8):# values from 2 to 8(but not including 8)
	print(x)

print("////////////////////////")
for x in range(2, 30, 5): #increment the sequence with 5(default 1)
	print(x)

