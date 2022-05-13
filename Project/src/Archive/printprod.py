import csv

def printprod(): ##function to print list of current products
    with open('Project\data\products.csv', 'r') as file:
        reader = csv.reader(file)
        print()
        #menuline()
        print()
        print("Available products are")
        print()
        for products in reader:
            print(products)
    print()
    #menuline()
    print()
    #prodmenu()

printprod()