import csv
from datetime import datetime
from dotenv import load_dotenv
import os
import pprint
import pymysql

pp = pprint.PrettyPrinter(indent=2)
customer_spend = {}
customer_sales = {}
sales_data = []
sales_data_filtered = []
date1 = datetime.strptime('2020-12-01', '%Y-%m-%d')
date2 = datetime.strptime('2020-12-05', '%Y-%m-%d')

def setup_db_connection():
    # establish db connection, create db, table etc.
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    warehouse_db_name = os.environ.get("mysql_db")

    return pymysql.connect(
        host,
        user,
        password,
        warehouse_db_name
    )
    
def create_tables():
    conn = setup_db_connection()
    cursor = conn.cursor()
    
    create_sales_data_table = \
    """
        CREATE TABLE IF NOT EXISTS sales_data(
            customer_id int NOT NULL,
            purchase_date date,
            purchase_amount decimal(19,2),
            product_id varchar(10)
        );
    """
    create_customer_spend_table = \
    """
        CREATE TABLE IF NOT EXISTS customer_spend(
            customer_id int NOT NULL,
            average_spend decimal(19,2),
            total_spend decimal(19,2)
        );
    """
    create_customer_products_table = \
    """
        CREATE TABLE IF NOT EXISTS customer_products(
            customer_id int NOT NULL,
            product_id varchar(10),
            quantity int
        );
    """

    cursor.execute(create_sales_data_table)
    cursor.execute(create_customer_spend_table)
    cursor.execute(create_customer_products_table)
    conn.commit()
    cursor.close()
    conn.close()

def extract_and_clean_sales_data():
    try:
        with open('sales_data.csv', 'r') as file:
            source_file = csv.DictReader(file, fieldnames=['customer_id', 'purchase_date', 'purchase_amount', 'product_id'], delimiter=',')
            next(source_file) #ignore the header row
            
            for row in source_file:
                if '' not in row.values(): # do not add record if data is missing
                    date = datetime.strptime(row['purchase_date'], '%Y-%m-%d')
                    if date1 <= date <= date2:
                        sales_data_filtered.append(row)
                        if row['customer_id'] not in customer_spend: # add new customer to customer_spend
                            customer_spend[row['customer_id']] = { 'avg_spend': 0, 'total_spend': 0, 'no_of_purchases': 0 }
                            
                        if row['customer_id'] not in customer_sales: # add new customer to customer_sales
                            customer_sales[row['customer_id']] = { 'products': { } }
                    
                    sales_data.append(row)
                    
    except Exception as error:
        print("An error occurred: " + str(error))
    return sales_data

# get avg and total spend for each customer
def calculate_customer_spend():
    for customer_id, spend_data in customer_spend.items():
        for sale in sales_data_filtered:
            if customer_id == sale['customer_id']:
                spend_data['total_spend'] += float(sale['purchase_amount'])
                spend_data['no_of_purchases'] += 1
                
        spend_data['total_spend'] = round(spend_data['total_spend'], 2) # round total spend to 2 decimal places
        avg_spend = spend_data['total_spend'] / spend_data['no_of_purchases']
        spend_data['avg_spend'] = round(avg_spend, 2)

# get number of purchases per product for each customer
def calculate_customer_sales():
    for customer_id, product_data in customer_sales.items():
        for sale in sales_data_filtered:
            if customer_id == sale['customer_id']:
                if sale['product_id'] not in product_data['products']:
                    product_data['products'][sale['product_id']] = 1
                else:
                    product_data['products'][sale['product_id']] += 1

def insert_sales_data():
    conn = setup_db_connection()
    cursor = conn.cursor()
    sql = \
        '''
            INSERT INTO sales_data (customer_id, purchase_date, purchase_amount, product_id)
            VALUES (%s, DATE(%s), %s, %s)
        '''

    for sale in sales_data:
        cursor.execute(sql, (int(sale['customer_id']), sale['purchase_date'], float(sale['purchase_amount']), sale['product_id']))
    conn.commit()
    cursor.close()
    conn.close()
    
def insert_customer_spend():
    conn = setup_db_connection()
    cursor = conn.cursor()
    sql = \
        '''
            INSERT INTO customer_spend (customer_id, average_spend, total_spend)
            VALUES (%s, %s, %s)
        '''
        
    for customer_id, spend_data in customer_spend.items():
        cursor.execute(sql, (customer_id, spend_data['avg_spend'], spend_data['total_spend']))

    conn.commit()
    cursor.close()
    conn.close()

def insert_customer_sales():
    conn = setup_db_connection()
    cursor = conn.cursor()
    sql = \
        '''
            INSERT INTO customer_products (customer_id, product_id, quantity)
            VALUES (%s, %s, %s)
        '''
        
    for customer_id, products in customer_sales.items():
        for product_data in products.values():
            for product_id, quantity in product_data.items():
                cursor.execute(sql, (customer_id, product_id, quantity))

    conn.commit()
    cursor.close()
    conn.close()
    
cleaned_sales_data = extract_and_clean_sales_data()
calculate_customer_spend()
calculate_customer_sales()
create_tables()
insert_sales_data()
insert_customer_spend()
insert_customer_sales()
