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

def print_product():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchone()[0]
    print(products)
    print("Current Product List")
    print("--------------------")
    print()
    print("ID   Name        Price(£)")
    for items in products:
        print(items)
    print()
    #menuline()
    input("Press Enter to return to the products Menu: ")
    #productmenu()
    
    #cursor.execute("SELECT COUNT(*) FROM products") #fetches the number of rows in the table
    #products = cursor.fetchone()[0] 
    #print(products)


    connection.commit()
    cursor.close()
    connection.close()

print_product()


for count, row in enumerate(products, 1):
            print(f"{count} | {row[1]} | £{row[2]}")
