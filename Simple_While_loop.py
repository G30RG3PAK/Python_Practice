#while loop Python
i = 0
while i <= 20:
	print(i)
	i+= 1

print("/////////////")
#Break Statement
n = 0
while n <= 20:
	print(n)
	if n == 10:
		break #stop the loop even if the while condition is true
	n += 1

print("/////////////")
#Continue Statement
j = 0
while j < 20:
	j += 1
	if j == 10:
		continue
	print(j)
