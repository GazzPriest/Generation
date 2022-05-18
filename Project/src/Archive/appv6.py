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
        productmenu()
    elif user_input == '2':
        couriermenu()
    elif user_input == '3':
        ordermenu()
    elif user_input == '0':
        exit() #function should call savefile
    else:
        print('Sorry, invalid input, please try again')
        mainmenu()

def productmenu(): ## function to call product menu
    menuline()
    print()
    print('Products Menu')
    print()
    menuline()
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
        mainmenu()
    else:
        print('Sorry, invalid input, please try again')
        productmenu()

def printproduct(): ##function to print list of current products
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
        menuline()
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
        menuline()
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
        menuline()
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
        deletecourier()
    elif user_input == '0':
        mainmenu()
    else:
        print('Sorry, invalid input, please try again')
        productmenu()

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
    with open('Project\data\couriers.csv', 'a', newline='') as csvfile:
        courier_info = ['id', 'Name', 'Phone']
        writer = csv.DictWriter(csvfile, fieldnames = courier_info)
        id_value = couriernumber()
        courier_name = input("What is the name of the new courier?: ")
        courier_phone = input("What is the courier's phone number?: ")
        couriers = [{'id': id_value, 'Name': courier_name, 'Phone': courier_phone}]
        if id_value == 1:
            writer.writeheader()
        else:
            pass
        writer.writerows(couriers)
        csvfile.close()
        print()
        menuline()
        print()
        courierrepeat()

def couriernumber():##function to track courier id numbers
    with open(r"Project\data\couriers.csv", 'r') as file:
        couriernumber = len(file.readlines())
        if couriernumber == 0:
            couriernumber + 1
        return couriernumber

def courierrepeat(): ##function that allows user to add couriers one by one without moving menus
    user_input = input("Would you like to add another courier? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        createcourier()
    elif user_input == 'N' or user_input == 'n':
        couriermenu()
    else:
        print('Sorry, invalid input, please try again')
        courierrepeat()

def updatecourier(): ##function to update current courier
    courierlist = []
    with open('Project\data\couriers.csv', 'r') as file:
        reader = csv.reader(file)
        print()
        menuline()
        print()
        print("Available couriers are")
        print()
        for couriers in reader:
            courierlist.append(couriers)
            print(couriers)
        print()
        user_input = int(input("Please enter the ID of the courier you would like to update?: "))
        for i in range(1, len(courierlist[0])):
            new_info = input("Enter new information for " + str(courierlist[0][i] + ": "))
            courierlist[user_input][i] = new_info
        with open('Project\data\couriers.csv', 'w', newline="") as file:
            writer = csv.writer(file)
            for i in range(len(courierlist)):
                writer.writerow(courierlist[i])
        print()
        menuline()
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

def deletecourier(): ##function to remove courier
    readlist = []
    with open('Project\data\couriers.csv', 'r') as file:
        reader = csv.reader(file)
        print()
        menuline()
        print()
        print("Available couriers are")
        print()
        for couriers in reader:
            readlist.append(couriers)
            print(couriers)
        print()
    file.close()

    file=open("Project\data\couriers.csv", 'r')
    reader = csv.reader(file)
    courierlist=[]
    user_input=int(input("Please enter the courier to be deleted: "))
    Found = False
    for row in reader:
        if row[0]==str(user_input):
            Found=True
        else:
            courierlist.append(row)
    file.close
    
    if Found==False:
        print("Sorry, that courier ID has has not been found")
    else:
        file=open("Project\data\couriers.csv", 'w+', newline='')
        writer=csv.writer(file)
        writer.writerows(courierlist)
        file.seek(0)
        reader=csv.reader(file)
        for row in reader:
            print("Available couriers are")
            print()
            printcourier()
            print()
            deletecourierrepeat()
        file.close()

def deletecourierrepeat(): ##function that allows user to delete products one by one without moving menus
    user_input = input("Would you like to delete another courier? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        deletecourier()
    elif user_input == 'N' or user_input == 'n':
        couriermenu()
    else:
        print('Sorry, invalid input, please try again')
        deletecourierrepeat()

def ordermenu(): ## function to call orders menu
    menuline()
    print()
    print('Orders Menu')
    print()
    menuline()
    print()
    print('1: Print Orders \n2: Create New Order \n3: Update Existing Order \n4: Update Order Status \n5: Delete Order \n0: Return to Main Menu')
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
        updateorderstatus()
    elif user_input == '5':
        deleteorder()
    elif user_input == '0':
        mainmenu()
    else:
        print('Sorry, invalid input, please try again')
        ordermenu()

def printorder(): ##function to print list of current orders
    with open('Project\data\orders.csv', 'r') as file:
        reader = csv.reader(file)
        print()
        #menuline()
        print()
        print("Currently open orders are")
        print()
        for orders in reader:
            if orders[5] == "Delivered" or orders[5] == "Cancelled":
                continue
            print(orders)
    print()
    menuline()
    input("Press Enter to return to the orders Menu: ")
    ordermenu()

def createorder(): ##function to create new order
    with open('Project\data\orders.csv', 'a', newline='') as csvfile:
        order_info = ['id', 'Customer Name', 'Customer Address', 'Customer Phone', 'Courier', 'Status', 'Items']
        writer = csv.DictWriter(csvfile, fieldnames = order_info)
        id_value = ordernumber()
        customer_name = input("What is the customer name?: ")
        customer_address = input("What is the customer address?: ")
        customer_phone = input("What is the customer phone number?: ")
        with open('Project\data\couriers.csv', 'r') as file:
            reader = csv.reader(file)
            print()
            menuline()
            print()
            print("Available couriers are")
            print()
            for couriers in reader:
                print(couriers)
        courier = input("Please enter the courier ID: ")
        status = "Preparing"
        with open('Project\data\products.csv', 'r') as file:
            reader = csv.reader(file)
            print()
            menuline()
            print()
            print("Available products are")
            print()
            for products in reader:
                print(products)
        items = input("Please enter the product ID(s): ")
        orders = [{'id': id_value, 'Customer Name': customer_name, 'Customer Address': customer_address, 'Customer Phone': customer_phone, 'Courier': courier, 'Status': status, 'Items': items}]
        if id_value == 1:
            writer.writeheader()
        else:
            pass
        writer.writerows(orders)
        csvfile.close()
        print()
        menuline()
        print()
        orderrepeat()

def ordernumber():##function to track order id numbers
    with open(r"Project\data\orders.csv", 'r') as file:
        ordernumber = len(file.readlines())
        if ordernumber == 0:
            ordernumber + 1
        return ordernumber

def orderrepeat():##function that allows user to create orders one by one without moving menus
    user_input = input("Would you like to add another order? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        createorder()
    elif user_input == 'N' or user_input == 'n':
        ordermenu()
    else:
        print('Sorry, invalid input, please try again')
        orderrepeat()

def updateorder(): ##function to update current order
    orderlist = []
    with open('Project\data\orders.csv', 'r') as file:
        reader = csv.reader(file)
        print()
        menuline()
        print()
        print("Currently open orders are")
        print()
        for orders in reader:
            orderlist.append(orders)
            print(orders)
        print()
        user_input = int(input("Please enter the ID of the order you would like to update?: "))
        print("1: Customer Name \n2: Customer Address \n3: Customer Phone \n4: Courier \n5: Items\n0: All Fields" )
        user_choice = input("Please select the information you wish to update: ")
        if user_choice == '1':
            for i in range(1, 2):
                new_info = input("Enter new information for " + str(orderlist[0][i] + ": "))
                orderlist[user_input][i] = new_info
        elif user_choice == '2':
            for i in range(2, 3):
                new_info = input("Enter new information for " + str(orderlist[0][i] + ": "))
                orderlist[user_input][i] = new_info
        elif user_choice == '3':
            for i in range(3, 4):
                new_info = input("Enter new information for " + str(orderlist[0][i] + ": "))
                orderlist[user_input][i] = new_info
        elif user_choice == '4':
            for i in range(4, 5):
                new_info = input("Enter new information for " + str(orderlist[0][i] + ": "))
                orderlist[user_input][i] = new_info
        elif user_choice == '5':
            for i in range(6, 7):
                new_info = input("Enter new information for " + str(orderlist[0][i] + ": "))
                orderlist[user_input][i] = new_info
        elif user_choice == '0':
            for i in range(1, len(orderlist[0])):
                if i == 5:
                    continue
                new_info = input("Enter new information for " + str(orderlist[0][i] + ": "))
                orderlist[user_input][i] = new_info       
        else:
            print('Sorry, invalid input, please try again')
            updateorder()
    with open('Project\data\orders.csv', 'w', newline="") as file:
        writer = csv.writer(file)
        for i in range(len(orderlist)):
            writer.writerow(orderlist[i])
    print()
    menuline()
    print()
    updateorderrepeat()

def updateorderrepeat(): ##function that allows user to update orders one by one without moving menus
    user_input = input("Would you like to amend another order? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        updateorder()
    elif user_input == 'N' or user_input == 'n':
        ordermenu()
    else:
        print('Sorry, invalid input, please try again')
        updateorderrepeat()

def updateorderstatus(): ##function to update order status
    orderlist = []
    with open('Project\data\orders.csv', 'r') as file:
        reader = csv.reader(file)
        print()
        menuline()
        print()
        print("Currently open orders are")
        print()
        for orders in reader:
            orderlist.append(orders)
            print(orders)
        print()
        user_input = int(input("Please enter the ID of the order status you would like to update?: "))
        print()
        menuline()
        print()
        print("1: Preparing \n2: Out For Delivery \n3: Delivered \n4: Cancelled \n0: Back to Order Menu" )
        print()
        user_choice = input("Please select the order status: ")
        if user_choice == '1':
            for i in range(5, 6):
                new_status = "Preparing"
                orderlist[user_input][i] = new_status
        elif user_choice == '2':
            for i in range(5, 6):
                new_status = "Out For Delivery"
                orderlist[user_input][i] = new_status
        elif user_choice == '3':
            for i in range(5, 6):
                new_status = "Delivered"
                orderlist[user_input][i] = new_status    
        elif user_choice == '4':
            for i in range(5, 6):
                new_status = "Cancelled"
                orderlist[user_input][i] = new_status        
        elif user_choice == '0':
            ordermenu()
        else:
            print('Sorry, invalid input, please try again')
            updateorderstatus()
    with open('Project\data\orders.csv', 'w', newline="") as file:
        writer = csv.writer(file)
        for i in range(len(orderlist)):
            writer.writerow(orderlist[i])
    print()
    menuline()
    print()
    updateorderstatusrepeat()

def updateorderstatusrepeat(): ##function that allows user to update order statuses one by one without moving menus
    user_input = input("Would you like to amend another order status? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        updateorder()
    elif user_input == 'N' or user_input == 'n':
        ordermenu()
    else:
        print('Sorry, invalid input, please try again')
        updateorderstatusrepeat()

def deleteorder(): ##function to remove orders
    readlist = []
    with open('Project\data\orders.csv', 'r') as file:
        reader = csv.reader(file)
        print()
        menuline()
        print()
        print("Currently open orders are")
        print()
        for orders in reader:
            readlist.append(orders)
            print(orders)
        print()
    file.close()

    file=open("Project\data\orders.csv", 'r')
    reader = csv.reader(file)
    orderlist=[]
    user_input=int(input("Please enter the order to be deleted: "))
    Found = False
    for row in reader:
        if row[0]==str(user_input):
            Found=True
        else:
            orderlist.append(row)
    file.close
    
    if Found==False:
        print("Sorry, that order ID has has not been found")
    else:
        file=open("Project\data\orders.csv", 'w+', newline='')
        writer=csv.writer(file)
        writer.writerows(orderlist)
        file.seek(0)
        reader=csv.reader(file)
        for row in reader:
            print("Currently open orders are")
            print()
            printorder()
            print()
            deleteorderrepeat()
        file.close()

def deleteorderrepeat(): ##function that allows user to delete products one by one without moving menus
    user_input = input("Would you like to delete another order? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        deleteorder()
    elif user_input == 'N' or user_input == 'n':
        ordermenu()
    else:
        print('Sorry, invalid input, please try again')
        deleteorderrepeat()

mainmenu()
