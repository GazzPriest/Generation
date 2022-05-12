import csv
import os

def createproduct():
    with open('Project\data\products.csv', 'a', newline='') as csvfile:
        product_info = ['id', 'Name', 'Price']
        writer = csv.DictWriter(csvfile, fieldnames = product_info)
        id_value = productnumber()
        product_name = input("What is the name of the new product?: ")
        product_price = float(input("What is the product price?: £"))
        products = [{'id': id_value, 'Name': product_name, 'Price': product_price}]
        if id_value == 1:
            writer.writeheader()
        else:
            pass
        writer.writerows(products)
        csvfile.close()

def productnumber():
    with open(r"Project\data\products.csv", 'r') as file:
        productnumber = len(file.readlines())
        if productnumber == 0:
            productnumber + 1
        return productnumber

createproduct()