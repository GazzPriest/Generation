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

def restore_files(): ## function to call restore files menu
    menuline()
    print()
    print('Restore Files')
    print()
    menuline()
    print()
    print('1: Restore Products \n2: Restore Couriers \n3: Restore Orders \n4: Restore All Files \n0: Return to Main Menu')
    print()
    restore_files_input()

def restore_files_input(): ##function to call restore file menu input from user
    user_input = input('Press a Key: ')
    if user_input == '1':
        restore_products()
        print("Restore Successful")
        restore_files_input()
    elif user_input == '2':
        restore_couriers()
        print("Restore Successful")
        restore_files_input()        
    elif user_input == '3':
        restore_orders()
        restore_order_status()
        print("Restore Successful")
        restore_files_input()
    elif user_input == '4':
        restore_products()
        restore_couriers()
        restore_orders()
        restore_order_status()
        print("Restore Successful")
        restore_files_input()
    elif user_input == '0':
        return
    else:
        print('Sorry, invalid input, please try again')
        restore_files()

def restore_products():
    pass

def restore_couriers():
    pass

def restore_orders():
    pass

def restore_order_status():
    pass