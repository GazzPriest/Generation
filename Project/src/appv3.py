def menuline(): ## function for ease of menu readabilityasas
    print('------------------------------------------------------')

def mainmenu(): ## function to call main menu
    menuline()
    print()
    print('Main Menu')
    print()
    menuline()
    print()
    print('1: Products Menu \n2: Couriers Menu \n3: Customers Menu \n4: Orders Menu \n0: Exit')
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
    '''elif user_input == '3':
        customermenu()
    elif user_input == '4':
        ordermenu()
    elif user_input == '0':
        exit() #function should call savefile
    else:
        print('Sorry, invalid input, please try again')
        mainmenu()'''

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
    products = {}
    with open('Project\data\products.txt') as f:
        for line in f:
            (key, val) = line.split()
            products[int(key)] = val
    print()
    menuline()
    print()
    print("Available products are ", products)
    print()
    prodmenu()

def createprod(): ##function to create new product
    products = {}
    with open('Project\data\products.txt') as f:
        for line in f:
            (key, val) = line.split()
            products[int(key)] = val
    create = open('Project\data\products.txt', 'a')   
    dictvalue = len(products) + 1
    user_prod_input = input("What is the name of the new product?: ")
    create.writelines('\n' + str(dictvalue) + ' ' + str(user_prod_input))
    products[dictvalue] = user_prod_input
    create.close()
    print()
    menuline()
    print()
    print("Available products are ", products)
    print()
    prodrepeat()

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
    products = {}
    with open('Project\data\products.txt') as f:
        for line in f:
            (key, val) = line.split()
            products[int(key)] = val
    print("Available products are ", products)
    amend = open('Project\data\products.txt', 'a')
    amend_user_input = int(input("What is the number of the product to be updated?: "))
    del products[amend_user_input]
    user_prod_input = input("What is the name of the new product?: ")
    amend.writelines('\n' + str(amend_user_input) + ' ' + str(user_prod_input))
    products[amend_user_input] = user_prod_input
    amend.close()
    print()
    menuline()
    print()
    print("Available products are ", products)
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
    products = {}
    with open('Project\data\products.txt') as f:
        for line in f:
            (key, val) = line.split()
            products[int(key)] = val
    print("Available products are ", products)
    deleteprod = open('Project\data\products.txt', 'a')
    del_user_input = int(input("What is the number of the product to be deleted?: "))
    del products[del_user_input]
    deleteprod.close()
    print()
    menuline()
    print()
    print("Available products are ", products)
    print()
    delrepeat()

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

def printcourier(): ##function to print list of current couriers
    couriers = {}
    with open('Project\data\couriers.txt') as f:
        for line in f:
            (key, val) = line.split()
            couriers[int(key)] = val
    print()
    menuline()
    print()
    print("Available couriers are ", couriers)
    print()
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

##def customermenu(): ##function to call courier menu

##def customermenu_input(): ##function to call courier menu input from user

##def ordermenu(): ##function to call courier menu

##def ordermenu_input(): ##function to call courier menu input from user

mainmenu()

