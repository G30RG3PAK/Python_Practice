#Else in For Loop
#specifies a block of code to be executed when the loop is finished
for x in range(11):
	print(x) #print all number from 0 to 10
else: #print a message when the loop has ended
	print("Finished!")


#Nested Loops = Loop inside a loop.
adj = ["Good","Bad","Perfect"]
N   = ["Man","Woman","Kid"]
for x in adj:
	for y in N:
		print(x,y)