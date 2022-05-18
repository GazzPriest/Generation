import csv
from mainmenu_function import menuline

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
        return
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
