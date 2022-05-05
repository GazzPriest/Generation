import math

fact = math.factorial(5)
print(fact)

############################################

from math import factorial

print(factorial(5))

############################################

def factfunct(num):
    print(factorial(num))

############################################

##Variable Scope

#a = local - destroyed at end of function
#b = local - ditto
#c = global - destroyed at end of file
#d = global

# This is a global variable
a = 0

if a == 0:
    # This is still a global variable
    b = 1

def my_function(c):
    # this is a local variable
    d = 3
    print(c)
    print(d)

# Now we call the function, passing the value 7 as the first and only parameter
my_function(7)

# a and b still exist
print(a)
print(b)

# c and d don't exist anymore -- these statements will give us name errors!
#print(c)
#print(d)

#prints c and d inside function first (7 and 3), then prints a and b (0 and 1), then fails on c and d outside function