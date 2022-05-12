import csv
import pandas as pd

def createproduct():
    with open('Project\data\products.csv', 'a', newline='') as csvfile:
        id_value = productnumber()
        product_name = input("What is the name of the new product?: ")
        product_price = float(input("What is the product price?: £"))
        products = [{'id': id_value, 'Name': product_name, 'Price': product_price}]
        df = pd.DataFrame(columns=["id", "Name", "Price"], data=products)
        #print(df)
        df.to_csv("products.csv", index=None)
        csvfile.close()

def productnumber():
    with open(r"Project\data\products.csv", 'r') as file:
        productnumber = len(file.readlines())
        if productnumber == 0:
            productnumber + 1
        return productnumber

createproduct()