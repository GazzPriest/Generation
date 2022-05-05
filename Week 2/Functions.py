'''##1
def product(a, b):
    return a + b
print(product(4,6))

##2
def sum(*args):
    num = 0
    for i in args:
        num += i
    return num
print(sum(4,6,7))

##3
def dictionary(*args, **kwargs):
    print(args, kwargs)

dictionary(a=1, b=2, c=3, z=26)
'''
##4
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

print('Press A to Add, S to subtract, M to multiply or D to divide')
choice = input()
if choice == 'A' or choice == 'a':
    print('Please enter the first number')
    num1 = int(input())
    print('Please enter the second number')
    num2 = int(input())
    print(add(num1, num2))
elif choice == 'S' or choice == 's':
    print('Please enter the first number')
    num1 = int(input())
    print('Please enter the second number')
    num2 = int(input())
    print(subtract(num1, num2))
elif choice == 'M' or choice == 'm':
    print('Please enter the first number')
    num1 = int(input())
    print('Please enter the second number')
    num2 = int(input())
    print(multiply(num1, num2))
elif choice == 'D' or choice == 'd':
    print('Please enter the first number')
    num1 = int(input())
    print('Please enter the second number')
    num2 = int(input())
    print(divide(num1, num2))

'''
##Don's calculator
def calc(a, sign, b):
    return "Your total is " + str(eval(str(a) + sign + str(b)))
print(calc(input('Please enter the first number : '), input('Please enter the sign : '), input('Please enter the second number : ')))
'''