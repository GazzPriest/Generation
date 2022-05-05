def my_function(a):
    b = a - 2
    return b

c = 1

if c > 2:
    d = my_function(5)
print(d)

#changing c to 1 means the if won't run, so d becomes undefined and returns error

#put an else into the if block to catch the error and print an error message