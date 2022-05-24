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

def courier_menu(): ## function to call courier menu
    menuline()
    print()
    print('Courier Menu')
    print()
    menuline()
    print()
    print('1: Print Couriers List \n2: Create New Courier \n3: Update Existing Courier \n4: Delete Courier \n0: Return to Main Menu')
    print()
    courier_menu_input()

def courier_menu_input(): ##function to call courier menu input from user
    user_input = input('Press a Key: ')
    if user_input == '1':
        print_courier()
    elif user_input == '2':
        create_courier()
    elif user_input == '3':
        update_courier()
    elif user_input == '4':
        delete_courier()
    elif user_input == '0':
        return
    else:
        print('Sorry, invalid input, please try again')
        courier_menu()

def print_courier():
    cursor.execute("SELECT * FROM couriers")
    couriers = cursor.fetchall()
    print("Current courier List")
    print("--------------------")
    print()
    print("ID  Name  Phone Number")
    for row in couriers:
        print(f"{row[0]} - {row[1]} - {row[2]}")
    connection.commit()
    #cursor.close()
    #connection.close()
    print()
    menuline()
    input("Press Enter to return to the couriers Menu: ")
    courier_menu()

def create_courier():
    cursor = connection.cursor()
    courier_name = input("What is the new courier name?: ")
    courier_phone = input("What is the new courier phone?: ")
    sql = "INSERT INTO couriers (courier_name, courier_phone) VALUES (%s, %s)"
    val = (courier_name, courier_phone)
    cursor.execute(sql, val)
    connection.commit()
    #cursor.close()
    #connection.close()
    print()
    menuline()
    print()
    courier_repeat()

def courier_repeat(): ##function that allows user to add couriers one by one without moving menus
    user_input = input("Would you like to add another courier? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        create_courier()
    elif user_input == 'N' or user_input == 'n':
        courier_menu()
    else:
        print('Sorry, invalid input, please try again')
        courier_repeat()

def update_courier():
    cursor = connection.cursor()
    courierlist = []
    cursor.execute("SELECT * FROM couriers")
    couriers = cursor.fetchall()
    print("Current courier List")
    print("--------------------")
    print()
    print("ID  Name        Phone Number")
    for row in couriers:
        courierlist.append(row)
        print(f"{row[0]} - {row[1]} - {row[2]}")
    print()
    update_courier = int(input("What is the ID of the courier to be updated?: "))
    new_courier_name = (input("What is the new courier name?: "))
    new_courier_phone = (input("What is the new courier phone?: "))
    cursor.execute(f"UPDATE couriers set courier_name = '{new_courier_name}', courier_phone = '{new_courier_phone}' WHERE courier_id = '{update_courier}'")
    connection.commit()
    #cursor.close()
    #connection.close()
    print()
    menuline()
    print()
    update_repeat()

def update_repeat(): ##function that allows user to update couriers one by one without moving menus
    user_input = input("Would you like to amend another courier? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        update_courier()
    elif user_input == 'N' or user_input == 'n':
        courier_menu()
    else:
        print('Sorry, invalid input, please try again')
        update_repeat()

def delete_courier():
    cursor = connection.cursor()
    courierlist = []
    cursor.execute("SELECT * FROM couriers")
    couriers = cursor.fetchall()
    print("Current courier List")
    print("--------------------")
    print()
    print("ID  Name        Phone Number")
    for row in couriers:
        courierlist.append(row)
        print(f"{row[0]} - {row[1]} - {row[2]}")
    print()
    delete_courier = int(input("What is the ID of the courier to be deleted?: "))
    cursor.execute(f"DELETE FROM couriers WHERE courier_id = '{delete_courier}'")
    connection.commit()
    #cursor.close()
    #connection.close()
    print()
    menuline()
    print()
    delete_repeat()

def delete_repeat(): ##function that allows user to delete products one by one without moving menus
    user_input = input("Would you like to delete another courier? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        delete_courier()
    elif user_input == 'N' or user_input == 'n':
        courier_menu()
    else:
        print('Sorry, invalid input, please try again')
        delete_repeat()
