import pymysql
import os
from dotenv import load_dotenv

from Project.src.order_module import order_menu
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

def fetch_order_status():
    cursor = connection.cursor()
    print()
    print("Order Status Menu")
    #menuline()
    print()
    print("1: Preparing \n2: Out For Delivery \n3: Delivered \n4: Cancelled \n0: Back to Order Menu" )
    print()
    user_choice = input("Please select the order status: ")
    if user_choice == '1':
        cursor.execute(f"SELECT * FROM orders WHERE status = 'Preparing'")
        orders = cursor.fetchall()
        print()
        print("Current Orders")
        #menuline()
        print()
        print("ID - Name - Address - Phone Number - Courier - Items")
        for row in orders:
            print(f"{row[0]} - {row[1]} - {row[2]} - {row[3]} - {row[4]} - {row[6]}")
            #menuline()
    if user_choice == '2':
        cursor.execute(f"SELECT * FROM orders WHERE status = 'Out For Delivery'")
        orders = cursor.fetchall()
        print()
        print("Current Orders")
        #menuline()
        print()
        print("ID - Name - Address - Phone Number - Courier - Items")
        for row in orders:
            print(f"{row[0]} - {row[1]} - {row[2]} - {row[3]} - {row[4]} - {row[6]}")
            #menuline()
    if user_choice == '3':
        cursor.execute(f"SELECT * FROM orders WHERE status = 'Delivered'")
        orders = cursor.fetchall()
        print()
        print("Current Orders")
        #menuline()
        print()
        print("ID - Name - Address - Phone Number - Courier - Items")
        for row in orders:
            print(f"{row[0]} - {row[1]} - {row[2]} - {row[3]} - {row[4]} - {row[6]}")
            #menuline()
    if user_choice == '4':
        cursor.execute(f"SELECT * FROM orders WHERE status = 'Cancelled'")
        orders = cursor.fetchall()
        print()
        print("Current Orders")
        #menuline()
        print()
        print("ID - Name - Address - Phone Number - Courier - Items")
        for row in orders:
            print(f"{row[0]} - {row[1]} - {row[2]} - {row[3]} - {row[4]} - {row[6]}")
            #menuline()
    input("Press Enter to return to the Orders Menu: ")
    order_menu()

fetch_order_status()