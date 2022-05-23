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
    products = cursor.fetchall()
    columns = cursor.description 
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    print(result)
    print("Current Product List")
    print("--------------------")
    print()
    print("ID  Name        Price(£)")
    for row in products:
        print(f"{row[0]} - {row[1]} - £{float(row[2]):.2f}")
    connection.commit()
    cursor.close()
    connection.close()
    print()
    #menuline()
    input("Press Enter to return to the products Menu: ")
    #productmenu()

print_product()
