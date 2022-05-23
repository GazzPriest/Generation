import pymysql
import os
from dotenv import load_dotenv

#def connection():
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

def create_product():
    cursor = connection.cursor()
    product_name = input("What is the new product name?: ")
    product_price = input("What is the new product price?: £")
    sql = "INSERT INTO products (product_name, product_price) VALUES (%s, %s)"
    val = (product_name, product_price)
    cursor.execute(sql, val)
    connection.commit()
    cursor.close()
    connection.close()

create_product()
