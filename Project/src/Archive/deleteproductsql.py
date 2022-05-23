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
    cursor.close()
    connection.close()

delete_product()