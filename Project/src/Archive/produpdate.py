import csv

def updateprod(): ##function to update current product
    productlist = []
    with open('Project\data\products.csv', 'r') as file:
        reader = csv.reader(file)
        print()
        print("Menuline here")
        print()
        print("Available products are")
        print()
        for products in reader:
            productlist.append(products)
            print(products)
        print()
        user_input = int(input("Please enter the ID of the product you would like to update?: "))
        for i in range(1, len(productlist[0])):
            new_info = input("Enter new information for " + str(productlist[0][i] + ": "))
            productlist[user_input][i] = new_info
        with open('Project\data\products.csv', 'w', newline="") as file:
            writer = csv.writer(file)
            for i in range(len(productlist)):
                writer.writerow(productlist[i])
        print()
        print("Menuline here")
        print()
        print("Printprod")
        print()
        print("Repeat here")


        




updateprod()
    
    
    
    
    
    
    
    
    #products = {}
    #with open('Project\data\products.txt') as f:
    #    for line in f:
    #        (key, val) = line.split()
    #        products[int(key)] = val
    #print("Available products are ", products)
    #amend = open('Project\data\products.txt', 'a')
    #amend_user_input = int(input("What is the number of the product to be updated?: "))
    #del products[amend_user_input]
    #user_prod_input = input("What is the name of the new product?: ")
    #amend.writelines('\n' + str(amend_user_input) + ' ' + str(user_prod_input))
    #products[amend_user_input] = user_prod_input
    #amend.close()
    #print()
    #menuline()
    #print()
    #print("Available products are ", products)
    #print()
    #updaterepeat()