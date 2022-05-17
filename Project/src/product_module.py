import csv

def productmenu(): ## function to call product menu
    import main
    main.menuline()
    print()
    print('Products Menu')
    print()
    main.menuline()
    print()
    print('1: Print Products Menu \n2: Create New Product \n3: Update Existing Product \n4: Delete Product \n0: Return to Main Menu')
    print()
    productmenu_input()

def productmenu_input(): ##function to call product menu input from user
    user_input = input('Press a Key: ')
    if user_input == '1':
        printproduct()
    elif user_input == '2':
        createproduct()
    elif user_input == '3':
        updateproduct()
    elif user_input == '4':
        deleteproduct()
    elif user_input == '0':
        import main
        main.mainmenu()
    else:
        print('Sorry, invalid input, please try again')
        productmenu()

def printproduct(): ##function to print list of current products
    with open('Project\data\products.csv', 'r') as file:
        reader = csv.reader(file)
        print()
        import main
        main.menuline()
        print()
        print("Available products are")
        print()
        for products in reader:
            print(products)
    print()
    main.menuline()
    input("Press Enter to return to the products Menu: ")
    productmenu()

def createproduct(): ##function to create new product
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
        import main
        main.menuline()
        print()
        productrepeat()

def productnumber():##function to track product id numbers
    with open(r"Project\data\products.csv", 'r') as file:
        productnumber = len(file.readlines())
        if productnumber == 0:
            productnumber + 1
        return productnumber

def productrepeat(): ##function that allows user to add products one by one without moving menus
    user_input = input("Would you like to add another product? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        createproduct()
    elif user_input == 'N' or user_input == 'n':
        productmenu()
    else:
        print('Sorry, invalid input, please try again')
        productrepeat()

def updateproduct(): ##function to update current product
    productlist = []
    with open('Project\data\products.csv', 'r') as file:
        reader = csv.reader(file)
        print()
        import main
        main.menuline()
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
        main.menuline()
        print()
        updaterepeat()

def updaterepeat(): ##function that allows user to update products one by one without moving menus
    user_input = input("Would you like to amend another product? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        updateproduct()
    elif user_input == 'N' or user_input == 'n':
        productmenu()
    else:
        print('Sorry, invalid input, please try again')
        updaterepeat()

def deleteproduct(): ##function to remove product
    readlist = []
    with open('Project\data\products.csv', 'r') as file:
        reader = csv.reader(file)
        print()
        import main
        main.menuline()
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
            printproduct()
            print()
            deleteproductrepeat()
        file.close()

def deleteproductrepeat(): ##function that allows user to delete products one by one without moving menus
    user_input = input("Would you like to delete another product? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        deleteproduct()
    elif user_input == 'N' or user_input == 'n':
        productmenu()
    else:
        print('Sorry, invalid input, please try again')
        deleteproductrepeat()
