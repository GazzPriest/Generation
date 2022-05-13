def prodmenu(): ## function to call product menu
    menuline()
    print()
    print('Products Menu')
    print()
    menuline()
    print()
    print('1: Print Products Menu \n2: Create New Product \n3: Update Existing Product \n4: Delete Product \n0: Return to Main Menu')
    print()
    prodmenu_input()

def prodmenu_input(): ##function to call product menu input from user
    user_input = input('Press a Key: ')
    if user_input == '1':
        printprod()
    elif user_input == '2':
        createprod()
    elif user_input == '3':
        updateprod()
    elif user_input == '4':
        delprod()
    elif user_input == '0':
        mainmenu()
    else:
        print('Sorry, invalid input, please try again')
        prodmenu()

def printprod(): ##function to print list of current products
    with open('Project\data\products.csv', 'r') as file:
        reader = csv.reader(file)
        print()
        menuline()
        print()
        print("Available products are")
        print()
        for products in reader:
            print(products)
    print()
    menuline()
    input("Press Enter to return to the Products Menu: ")
    prodmenu()

def createprod(): ##function to create new product
    with open('Project\data\products.csv', 'a', newline='') as csvfile:
        product_info = ['id', 'Name', 'Price']
        writer = csv.DictWriter(csvfile, fieldnames = product_info)
        id_value = productnumber()
        product_name = input("What is the name of the new product?: ")
        product_price = float(input("What is the product price?: £"))
        products = [{'id': id_value, 'Name': product_name, 'Price': product_price}]
        if id_value == 1:
            writer.writeheader()
        else:
            pass
        writer.writerows(products)
        csvfile.close()
        print()
        menuline()
        print()
        prodrepeat()

def productnumber():##function to track product id numbers
    with open(r"Project\data\products.csv", 'r') as file:
        productnumber = len(file.readlines())
        if productnumber == 0:
            productnumber + 1
        return productnumber

def prodrepeat(): ##function that allows user to add products one by one without moving menus
    user_input = input("Would you like to add another product? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        createprod()
    elif user_input == 'N' or user_input == 'n':
        prodmenu()
    else:
        print('Sorry, invalid input, please try again')
        prodrepeat()

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
        menuline()
        print()
        updaterepeat()

def updaterepeat(): ##function that allows user to update products one by one without moving menus
    user_input = input("Would you like to amend another product? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        updateprod()
    elif user_input == 'N' or user_input == 'n':
        prodmenu()
    else:
        print('Sorry, invalid input, please try again')
        updaterepeat()

def delprod(): ##function to remove product
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
            printprod()
            print()
            delrepeat()
        file.close()

def delrepeat(): ##function that allows user to delete products one by one without moving menus
    user_input = input("Would you like to delete another product? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        delprod()
    elif user_input == 'N' or user_input == 'n':
        prodmenu()
    else:
        print('Sorry, invalid input, please try again')
        delrepeat()
