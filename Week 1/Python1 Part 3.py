age = int(input("What is your age?:"))
salary = int(input("What is your salary?: £"))
if age < 21 or salary < 21000:
    print(f'Sorry, we can not offer you a loan at this time.')
elif age >= 22 and age <= 30 and salary >= 21000:
    print(f'We can offer you a loan of up to £50,000')
elif age > 30 and salary >= 35000 and salary < 50000:
    print(f'We can offer you a loan of up to £75,000')
elif age > 30 and salary >= 50000:
    print(f'We can offer you a loan of up to £100,000')
else:
    print(f'Sorry, we can not offer you a loan at this time.')