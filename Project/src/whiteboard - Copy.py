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
    elif user_choice == '0':
        for i in range(1, len(orderlist[0])):
            if i == 5:
                continue
        fields = ("Customer Name or Reference", "Customer Address", "Customer Phone", "Delivery Courier", "Ordered Menu Items")
#        database = ["customer_name", "customer_address", "customer_phone", "courier_id", "items"]
#        for row in database:
#            database.append((#            ['customer_name'],
#            ['customer_address'],
#            ['customer_phone'],
#            ['courier_id'],
#            ['items']
#    ))
        sql = "UPDATE orders (customer_name, customer_address, customer_phone, courier_id, items) VALUES (%s, %s, %s, %s, %s)"
        for columns in fields:
            new_info = input("Enter new information for " + str(columns) + ": ")
            orderlist[user_input][i] = new_info
            cursor.execute(sql, new_info)
    else:
        print('Sorry, invalid input, please try again')
        update_order()
    #cursor.execute(f"UPDATE orders set {row[user_choice]} = '{new_info}' WHERE order_id = '{user_input}'")
    connection.commit()
    #cursor.close()
    #connection.close()
    print()
    #menuline()
    print()
    #update_repeat()

update_order()