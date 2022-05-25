import csv
import pymysql
import os
from dotenv import load_dotenv

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

def menuline(): ## function for ease of menu readability
    print('------------------------------------------------------')

def backup_files(): ## function to call backup files menu
    menuline()
    print()
    print('Backup Files')
    print()
    menuline()
    print()
    print('1: Backup Products \n2: Backup Couriers \n3: Backup Orders \n4: Backup All Files \n0: Return to Main Menu')
    print()
    backup_files_input()

def backup_files_input(): ##function to call backup file menu input from user
    user_input = input('Press a Key: ')
    if user_input == '1':
        backup_products()
        print("Backup Successful")
        input("Press Enter to return to Backup Menu")
        backup_files()
    elif user_input == '2':
        backup_couriers()
        print("Backup Successful")
        input("Press Enter to return to Backup Menu")
        backup_files()        
    elif user_input == '3':
        backup_orders()
        backup_order_status()
        print("Backup Successful")
        input("Press Enter to return to Backup Menu")
        backup_files()
    elif user_input == '4':
        backup_products()
        backup_couriers()
        backup_orders()
        backup_order_status()
        print("Backup Successful")
        input("Press Enter to return to Backup Menu")
        backup_files()
    elif user_input == '0':
        return
    else:
        print('Sorry, invalid input, please try again')
        backup_files()

def backup_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    with open('Project\data\products.csv', 'w', newline="") as file:
        writer = csv.writer(file)
        for i in range(len(products)):
            writer.writerow(products[i])

def backup_couriers():
    cursor.execute("SELECT * FROM couriers")
    couriers = cursor.fetchall()
    with open('Project\data\couriers.csv', 'w', newline="") as file:
        writer = csv.writer(file)
        for i in range(len(couriers)):
            writer.writerow(couriers[i])

def backup_orders():
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    with open('Project\data\orders.csv', 'w', newline="") as file:
        writer = csv.writer(file)
        for i in range(len(orders)):
            writer.writerow(orders[i])

def backup_order_status():
    cursor.execute("SELECT * FROM order_status")
    status = cursor.fetchall()
    with open('Project\data\orderstatus.csv', 'w', newline="") as file:
        writer = csv.writer(file)
        for i in range(len(status)):
            writer.writerow(status[i])