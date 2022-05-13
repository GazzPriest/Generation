import csv


def menuline(): ## function for ease of menu readability
    print('------------------------------------------------------')

def mainmenu(): ## function to call main menu
    menuline()
    print()
    print('Main Menu')
    print()
    menuline()
    print()
    print('1: Products Menu \n2: Couriers Menu \n3: Orders Menu \n0: Exit')
    print()
    mainmenu_input()
    print()
    menuline()

def mainmenu_input(): ##function to call main menu input from user
    user_input = input('Press a Key: ')
    if user_input == '1':
        prodmenu()
    elif user_input == '2':
        couriermenu()
    elif user_input == '3':
        ordermenu()
    elif user_input == '0':
        exit() #function should call savefile
    else:
        print('Sorry, invalid input, please try again')
        mainmenu()

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

def couriermenu(): ## function to call courier menu
    menuline()
    print()
    print('Courier Menu')
    print()
    menuline()
    print()
    print('1: Print Couriers List \n2: Create New Courier \n3: Update Existing Courier \n4: Delete Courier \n0: Return to Main Menu')
    print()
    couriermenu_input()

def couriermenu_input(): ##function to call courier menu input from user
    user_input = input('Press a Key: ')
    if user_input == '1':
        printcourier()
    elif user_input == '2':
        createcourier()
    elif user_input == '3':
        updatecourier()
    elif user_input == '4':
        delcourier()
    elif user_input == '0':
        mainmenu()
    else:
        print('Sorry, invalid input, please try again')
        prodmenu()

def printcourier(): ##function to print list of current products
    with open('Project\data\couriers.csv', 'r') as file:
        reader = csv.reader(file)
        print()
        menuline()
        print()
        print("Available couriers are")
        print()
        for couriers in reader:
            print(couriers)
    print()
    menuline()
    input("Press Enter to return to the Couriers Menu: ")
    couriermenu()

def createcourier(): ##function to create new courier
    couriers = {}
    with open('Project\data\couriers.txt') as f:
        for line in f:
            (key, val) = line.split()
            couriers[int(key)] = val
    create = open('Project\data\couriers.txt', 'a')   
    dictvalue = len(couriers) + 1
    user_courier_input = input("What is the name of the new courier?: ")
    create.writelines('\n' + str(dictvalue) + ' ' + str(user_courier_input))
    couriers[dictvalue] = user_courier_input
    create.close()
    print()
    menuline()
    print()
    print("Available products are ", couriers)
    print()
    courierrepeat()

def courierrepeat(): ##function that allows user to add couriers one by one without moving menus
    user_input = input("Would you like to add another courier? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        createcourier()
    elif user_input == 'N' or user_input == 'n':
        couriermenu()
    else:
        print('Sorry, invalid input, please try again')
        courierrepeat()

def updatecourier(): ##function to update courier information
    couriers = {}
    with open('Project\data\couriers.txt') as f:
        for line in f:
            (key, val) = line.split()
            couriers[int(key)] = val
    print("Available products are ", couriers)
    amend = open('Project\data\couriers.txt', 'a')
    amend_user_input = int(input("What is the number of the courier to be updated?: "))
    del couriers[amend_user_input]
    user_prod_input = input("What is the new courier information?: ")
    amend.writelines('\n' + str(amend_user_input) + ' ' + str(user_prod_input))
    couriers[amend_user_input] = user_prod_input
    amend.close()
    print()
    menuline()
    print()
    print("Available products are ", couriers)
    print()
    updatecourierrepeat()

def updatecourierrepeat(): ##function that allows user to update couriers one by one without moving menus
    user_input = input("Would you like to amend another courier? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        updatecourier()
    elif user_input == 'N' or user_input == 'n':
        couriermenu()
    else:
        print('Sorry, invalid input, please try again')
        updatecourierrepeat()

def delcourier(): ##function to remove courier
    couriers = {}
    with open('Project\data\couriers.txt') as f:
        for line in f:
            (key, val) = line.split()
            couriers[int(key)] = val
    print("Available products are ", couriers)
    deletecourier = open('Project\data\couriers.txt', 'a')
    del_user_input = int(input("What is the number of the courier to be deleted?: "))
    del couriers[del_user_input]
    deletecourier.close()
    print()
    menuline()
    print()
    print("Available products are ", couriers)
    print()
    delcourierrepeat()

def delcourierrepeat(): ##function that allows user to delete products one by one without moving menus
    user_input = input("Would you like to delete another product? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        delcourier()
    elif user_input == 'N' or user_input == 'n':
        couriermenu()
    else:
        print('Sorry, invalid input, please try again')
        delcourierrepeat()

def ordermenu(): ## function to call orders menu
    menuline()
    print()
    print('Orders Menu')
    print()
    menuline()
    print()
    print('1: Print Orders \n2: Create New Order \n3: Update Existing Order \n4: Delete Order \n0: Return to Main Menu')
    print()
    ordermenu_input()

def ordermenu_input(): ##function to call order menu input from user
    user_input = input('Press a Key: ')
    if user_input == '1':
        printorder()
    elif user_input == '2':
        createorder()
    #elif user_input == '3':
        #updateorder()
    #elif user_input == '4':
        #delorder()
    elif user_input == '0':
        mainmenu()
    else:
        print('Sorry, invalid input, please try again')
        ordermenu()

def printorder(): ##function to print list of current orders
    orders = {}
    with open('Project\data\orders.txt', 'r') as file:
        orders = file.readlines() #needs tidying up
    print()
    menuline()
    print()
    print("The currently open orders are ", orders)
    print()
    ordermenu()

def ordernumber():##function to create and track order
    with open("Project\data\orders.txt", 'r') as file:
        ordercount = len(file.readlines()) + 1
        return(ordercount)

def createorder():##function to create new order
    orders = {}
    with open('Project\data\orders.txt', 'a') as orderdict:
        orders["Order Number"] = ordernumber()
        orders["Name"] = input("Enter name: ")
        orders["Address"] = input("Enter delivery address: ")
        orders["Phone"] = input("Enter phone number: ")
        orders["Courier"] = input("Enter courier number: ")
        orders["Status"] = "Preparing"
        orderdict.write("\n" + str(orders))
        orderdict.close()
        print(orders)
        print()
        menuline()
        print()
        createorderrepeat()

def createorderrepeat():##function that allows user to create orders one by one without moving menus
    user_input = input("Would you like to add another order? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        createorder()
    elif user_input == 'N' or user_input == 'n':
        ordermenu()
    else:
        print('Sorry, invalid input, please try again')
        createorderrepeat()

def updateorder():
    pass

def updateorderrepeat():
    pass

def updateorderstatus():
    pass

def deleteorder():
    pass

def deleteorderrepeat():
    pass

mainmenu()
