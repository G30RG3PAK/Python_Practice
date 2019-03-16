# Python Function
# Block of code which only runs when it is called
# Pass parameter into a function and return data as a result

# Creating a Function
def Hello_Function(): #use "def" to define function
	print("Hello, this is my first function")

# Calling a Function
# To call this , use function name followed by parenthesis
Hello_Function()


# Parameter = information that pass to function
# specified after the function name, inside the parentheses

def name_function(name, surname): #name and syrname are parameters
	print(name+' '+surname) # add space between name and surname

#functions are called
name_function("Bobby", "Fischer") #data is passed to the function
name_function("Alice", "Polka")
name_function("Migante", "Duraharm")