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

def update_order_status(): ##function to update order status
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
    print()
    #menuline()
    print()
    print("1: Preparing \n2: Out For Delivery \n3: Delivered \n4: Cancelled \n0: Back to Order Menu" )
    print()
    user_choice = input("Please select the order status: ")
    if user_choice == '1':
        for i in range(5, 6):
            new_status = "Preparing"
            orderlist[user_input][i] = new_status
            cursor.execute(f"UPDATE orders set order_status = '{new_status}' WHERE order_id = {user_input}")
    elif user_choice == '2':
        for i in range(5, 6):
            new_status = "Out For Delivery"
            orderlist[user_input][i] = new_status
            cursor.execute(f"UPDATE orders set order_status = '{new_status}' WHERE order_id = {user_input}")
    elif user_choice == '3':
        for i in range(5, 6):
            new_status = "Delivered"
            orderlist[user_input][i] = new_status
            cursor.execute(f"UPDATE orders set order_status = '{new_status}' WHERE order_id = {user_input}")
    elif user_choice == '4':
        for i in range(5, 6):
            new_status = "Cancelled"
            orderlist[user_input][i] = new_status
            cursor.execute(f"UPDATE orders set order_status = '{new_status}' WHERE order_id = {user_input}")    
    elif user_choice == '0':
            return #order_menu()
    else:
        print('Sorry, invalid input, please try again')
        update_order_status()
    connection.commit()
    print()
    #menuline()
    print()
    #updateorderstatusrepeat()

update_order_status()