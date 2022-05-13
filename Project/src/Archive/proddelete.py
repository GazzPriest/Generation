import csv

readlist = []
with open('Project\data\products.csv', 'r') as file:
    reader = csv.reader(file)
    print()
    print("Menuline here")
    print()
    print("Available products are")
    print()
    for products in reader:
        readlist.append(products)
        print(products)
    print()
file.close()

file=open("Project\data\products.csv", 'r')
reader = csv.reader(file)
productlist=[]
user_input=int(input("Please enter the product to be deleted: "))
Found = False
for row in reader:
    if row[0]==str(user_input):
        Found=True
    else:
        productlist.append(row)
file.close


if Found==False:
    print("Sorry, that product ID has has not been found")
else:
    file=open("Project\data\products.csv", 'w+', newline='')
    writer=csv.writer(file)
    writer.writerows(productlist)
    file.seek(0)
    reader=csv.reader(file)
    for row in reader:
        print("Available products are")
        print()
        print(row)
        print()
        #delrepeat()
    file.close()