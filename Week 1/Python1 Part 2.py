print("Think of a number:")
x = (int(input()))
if (x % 2) == 0:
    print("Your number is even")
if (x % 2) != 0:
    print("Your number is odd")

print("Think of a second number:")
y = (int(input()))
if (y % 4) == 0:
    print("Your number is divisible by four")
if (y % 4) != 0:
    print("Your number is not divisible by four")

print("Think of a third number:")
z = (int(input()))
if (z % 3) == 0:
    print ('fizz')
if (z % 5) == 0:
    print ('buzz')

print("Are you converting to Fahrenheit or Celsius? Please enter F or C:")
unit = input()
if (unit) == "C":
    print("Please enter a temperature in Fahrenheit:")
    temp = (int(input()))
    output = (int((temp - 32) * (5/9)))
    print(f'{temp}F is {output}C')
if (unit) == "F":
    print("Please enter a temperature in Celsius:")
    temp = (int(input()))
    output = (int((temp * 1.8) + 32))
    print(f'{temp}C is {output}F')
