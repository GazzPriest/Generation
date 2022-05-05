for i in range(0,11):
    print(i)

j = 1
while(j<=10):
    print(j)
    j += 1

nums = [0, 2, 8, 20, 43, 82, 195, 204, 367]

for num in nums:
    print(num)

for i in range(0,11):
    print(i)
else: print('Done!')

list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]

for a in list1:
    for b in list2:
        if a == b:
            print(a)  

import random
while True:
    x = random.randint(1,100)
    print(x)
    if x % 5 == 0:
        break
    if x % 3 == 0:
        print("This number has been skipped")
        continue
    

