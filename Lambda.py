#Python Lambda
#Small anonymous function
#take any number of arguments, but only one expression

x = lambda a : a + 10
# add 10 to number passed in as a argument
print(x(10))
# executed the expression and print the result

y = lambda a, b : a * b
print(y(5, 8))
#lambda can take any number of arguments

#multiplies argument a with b and print result

z = lambda a, b, c : a + b + c
print(z(10, 11, 12))
# Sum a, b, c and print result


#Using lanbda with function
def multi(n):
	return lambda a : a * n

triple = multi(3)# pass to n
double = multi(2)# pass to n

print(double(15))# pass to a
print(triple(15))# pass to a







