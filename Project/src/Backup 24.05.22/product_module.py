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

def product_menu(): ## function to call product menu
    menuline()
    print()
    print('Products Menu')
    print()
    menuline()
    print()
    print('1: Show Products Menu \n2: Create New Product \n3: Update Existing Product \n4: Delete Product \n0: Return to Main Menu')
    print()
    product_menu_input()

def product_menu_input(): ##function to call product menu input from user
    user_input = input('Press a Key: ')
    if user_input == '1':
        print_product()
    elif user_input == '2':
        create_product()
    elif user_input == '3':
        update_product()
    elif user_input == '4':
        delete_product()
    elif user_input == '0':
        return
    else:
        print('Sorry, invalid input, please try again')
        product_menu()

def print_product():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    print("Current Product List")
    print("--------------------")
    print()
    print("ID  Name        Price(£)")
    for row in products:
        print(f"{row[0]} - {row[1]} - £{float(row[2]):.2f}")
    connection.commit()
    #cursor.close()
    #connection.close()
    print()
    menuline()
    input("Press Enter to return to the products Menu: ")
    product_menu()

def create_product():
    cursor = connection.cursor()
    product_name = input("What is the new product name?: ")
    product_price = input("What is the new product price?: £")
    sql = "INSERT INTO products (product_name, product_price) VALUES (%s, %s)"
    val = (product_name, product_price)
    cursor.execute(sql, val)
    connection.commit()
    #cursor.close()
    ##connection.close()
    print()
    menuline()
    print()
    product_repeat()

def product_repeat(): ##function that allows user to add products one by one without moving menus
    user_input = input("Would you like to add another product? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        create_product()
    elif user_input == 'N' or user_input == 'n':
        product_menu()
    else:
        print('Sorry, invalid input, please try again')
        product_repeat()

def update_product():
    cursor = connection.cursor()
    productlist = []
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    print("Current Product List")
    print("--------------------")
    print()
    print("ID  Name        Price(£)")
    for row in products:
        productlist.append(row)
        print(f"{row[0]} - {row[1]} - £{float(row[2]):.2f}")
    print()
    update_product = int(input("What is the ID of the product to be updated?: "))
    new_product_name = (input("What is the new product name?: "))
    new_product_price = (input("What is the new product price?: £"))
    cursor.execute(f"UPDATE products set product_name = '{new_product_name}', product_price = '{new_product_price}' WHERE product_id = '{update_product}'")
    connection.commit()
    #cursor.close()
    #connection.close()
    print()
    menuline()
    print()
    update_repeat()

def update_repeat(): ##function that allows user to update products one by one without moving menus
    user_input = input("Would you like to amend another product? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        update_product()
    elif user_input == 'N' or user_input == 'n':
        product_menu()
    else:
        print('Sorry, invalid input, please try again')
        update_repeat()

def delete_product():
    cursor = connection.cursor()
    productlist = []
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    print("Current Product List")
    print("--------------------")
    print()
    print("ID  Name        Price(£)")
    for row in products:
        productlist.append(row)
        print(f"{row[0]} - {row[1]} - £{float(row[2]):.2f}")
    print()
    delete_product = int(input("What is the ID of the product to be deleted?: "))
    cursor.execute(f"DELETE FROM products WHERE product_id = '{delete_product}'")
    connection.commit()
    #cursor.close()
    #connection.close()
    print()
    menuline()
    print()
    delete_repeat()

def delete_repeat(): ##function that allows user to delete products one by one without moving menus
    user_input = input("Would you like to delete another product? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        delete_product()
    elif user_input == 'N' or user_input == 'n':
        product_menu()
    else:
        print('Sorry, invalid input, please try again')
        delete_repeat()
