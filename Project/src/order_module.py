import csv 
from main_menu_function import menuline
import pymysql
import os
from dotenv import load_dotenv
#def create_server_connection(): #function to load .env variables and connect to SQL database "cafeapp"
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")
connection = pymysql.connect(
    host = host,
    user = user,
    password = password,
    database = database
)
cursor = connection.cursor()

def order_menu(): ## function to call orders menu
    menuline()
    print()
    print('Orders Menu')
    print()
    menuline()
    print()
    print('1: Show Open Orders \n2: Create New Order \n3: Update Existing Order \n4: Update Order Status \n5: Delete Order \n0: Return to Main Menu')
    print()
    order_menu_input()

def order_menu_input(): ##function to call order menu input from user
    user_input = input('Press a Key: ')
    if user_input == '1':
        print_order()
    elif user_input == '2':
        create_order()
    elif user_input == '3':
        update_order()
    elif user_input == '4':
        #update_order_status()
    #elif user_input == '5':
        #delete_order()
    #elif user_input == '0':
        return
    else:
        print('Sorry, invalid input, please try again')
        order_menu()

def print_order():
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    print("Current order List")
    print("--------------------")
    print()
    print("ID - Name - Address - Phone Number - Courier - Status - Items")
    for row in orders:
        print(f"{row[0]} - {row[1]} - {row[2]} - {row[3]} - {row[4]} - {row[5]} - {row[6]}")
    connection.commit()
    #cursor.close()
    #connection.close()
    print()
    menuline()
    input("Press Enter to return to the orders Menu: ")
    order_menu()

def create_order():
    cursor = connection.cursor()
    customer_name = input("What is the customer name or reference?: ")
    customer_address = input("What is the customer delivery address?: ")
    customer_phone = input("What is the customer phone number?: ")
    cursor.execute("SELECT * FROM couriers")
    couriers = cursor.fetchall()
    print()
    print("Current courier List")
    print("--------------------")
    print()
    print("ID  Name  Phone Number")
    for row in couriers:
        print(f"{row[0]} - {row[1]} - {row[2]}")
    menuline()
    order_courier = input("What is the ID of the delivery courier?: ")
    order_status = "Preparing"
    order_items = input("What are the IDs of the ordered menu items?: ")
    order_status_id = "1"
    sql = "INSERT INTO orders (customer_name, customer_address, customer_phone, courier_id, order_status, items, order_status_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (customer_name, customer_address, customer_phone, order_courier, order_status, order_items, order_status_id)
    cursor.execute(sql, val)
    connection.commit()
    #cursor.close()
    ##connection.close()
    print()
    menuline()
    print()
    order_repeat()

def order_repeat():##function that allows user to create orders one by one without moving menus
    user_input = input("Would you like to add another order? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        create_order()
    elif user_input == 'N' or user_input == 'n':
        order_menu()
    else:
        print('Sorry, invalid input, please try again')
        order_repeat()

def update_order():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM orders WHERE order_status = 'Preparing' OR order_status = 'Out For Delivery'")
    orders = cursor.fetchall()
    orderlist = []
    print()
    print("Currently Open Orders")
    print("--------------------")
    print()
    print("ID - Name - Address - Phone Number - Courier - Status - Items")
    for row in orders:
        order = {'order_id' : row[0], 'customer_name': row[1], 'customer_address': row[2], 'customer_phone': row[3], 'courier_id': row[4], 'order_status': row[5], 'items': row[6]}
        orderlist.append(order)
        print(f"{row[0]} - {row[1]} - {row[2]} - {row[3]} - {row[4]} - {row[5]} - {row[6]}")
    print()
    user_input = int(input("Please enter the ID of the order you would like to update?: "))
    print("1: Customer Name or Reference \n2: Customer Address \n3: Customer Phone \n4: Delivery Courier \n5: Ordered Menu Items\n0: All Fields" )
    user_choice = input("Please select the information you wish to update: ")
    if user_choice == '1':
        for i in range(1, 2):
            new_info = input("Enter new information for Customer Name or Reference: ")
            orderlist[user_input][i] = new_info
            cursor.execute(f"UPDATE orders set customer_name = '{new_info}' WHERE order_id = {user_input}")
    elif user_choice == '2':
        for i in range(2, 3):
            new_info = input("Enter new information for Customer Address: ")
            orderlist[user_input][i] = new_info
            cursor.execute(f"UPDATE orders set customer_address = '{new_info}' WHERE order_id = {user_input}")
    elif user_choice == '3':
        for i in range(3, 4):
            new_info = input("Enter new information for Customer Phone: ")
            orderlist[user_input][i] = new_info
            cursor.execute(f"UPDATE orders set customer_phone = '{new_info}' WHERE order_id = {user_input}")
    elif user_choice == '4':
        for i in range(4, 5):
            new_info = input("Enter new information for Delivery Courier: ")
            orderlist[user_input][i] = new_info
            cursor.execute(f"UPDATE orders set courier_id = '{new_info}' WHERE order_id = {user_input}")
    elif user_choice == '5':
        for i in range(6, 7):
            new_info = input("Enter new information for Ordered Menu Items: ")
            orderlist[user_input][i] = new_info
            cursor.execute(f"UPDATE orders set items = '{new_info}' WHERE order_id = {user_input}")
    #elif user_choice == '0':
    #    for i in range(1, len(orderlist[0])):
    #        if i == 5:
    #            continue
    #    fields = ("Customer Name or Reference", "Customer Address", "Customer Phone", "Delivery Courier", "Ordered Menu Items")
    #    for columns in fields:
    #        new_info = input("Enter new information for " + str(columns) + ": ")
    #        sql = "UPDATE orders (customer_name, customer_address, customer_phone, courier_id, items) VALUES (%s, %s,%s, %s, %s)"
    #        cursor.execute(sql, new_info)
    else:
        print('Sorry, invalid input, please try again')
        update_order()
    connection.commit()
    print()
    menuline()
    print()
    update_repeat()

def update_repeat(): ##function that allows user to update orders one by one without moving menus
    user_input = input("Would you like to amend another order? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        update_order()
    elif user_input == 'N' or user_input == 'n':
        order_menu()
    else:
        print('Sorry, invalid input, please try again')
        update_repeat()

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
            order_menu()
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
        update_order()
    elif user_input == 'N' or user_input == 'n':
        order_menu()
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
            print_order()
            print()
            deleteorderrepeat()
        file.close()

def deleteorderrepeat(): ##function that allows user to delete products one by one without moving menus
    user_input = input("Would you like to delete another order? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        deleteorder()
    elif user_input == 'N' or user_input == 'n':
        order_menu()
    else:
        print('Sorry, invalid input, please try again')
        deleteorderrepeat()
