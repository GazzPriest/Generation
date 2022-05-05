def menuline():
    pass

def mainmenu():
    pass

#############################################################################

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
    elif user_input == '3':
        updateorder()
    elif user_input == '4':
        delorder()
    elif user_input == '0':
        mainmenu()
    else:
        print('Sorry, invalid input, please try again')
        ordermenu()

def printorder(): ##function to print list of current orders
    orders = {}
    with open('Project\data\orders.txt') as f:
        for line in f:
            (key, val) = line.split()
            products[int(key)] = val
    print()
    menuline()
    print()
    print("The currently open orders are ", orders)
    print()
    ordermenu()

def createorder(): ##function to create new order
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