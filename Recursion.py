#Recursion in Python
#Recursion is a common mathematical and programming concept.
#function calls itself, and loop through data to reach a result.
def tri_recursion(k):
  if(k>0): #condition
    result = k+tri_recursion(k-1)# call functtion itself
    print(result) # show every result 
  else:
    result = 0
  return result

print("\n\nRecursion Example :")
tri_recursion(10) #call function
