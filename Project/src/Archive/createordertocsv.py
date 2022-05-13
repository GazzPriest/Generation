import csv

def createorder():
    with open('Project\data\orders.csv', 'a', newline='') as csvfile:
        order_info = ['id', 'Customer Name', 'Customer Address', 'Customer Phone', 'Courier', 'Status', 'Items']
        writer = csv.DictWriter(csvfile, fieldnames = order_info)
        id_value = ordernumber()
        customer_name = input("What is the customer name?: ")
        customer_address = input("What is the customer address?: ")
        customer_phone = input("What is the customer phone number?: ")
        #printcourier()
        courier = input("What is the courier number?: ")
        status = "Preparing"
        #printprod()
        items = input("What are the order items?: ")
        products = [{'id': id_value, 'Customer Name': customer_name, 'Customer Address': customer_address, 'Customer Phone': customer_phone, 'Courier': courier, 'Status': status, 'Items': items}]
        if id_value == 1:
            writer.writeheader()
        else:
            pass
        writer.writerows(products)
        csvfile.close()

def ordernumber():
    with open(r"Project\data\orders.csv", 'r') as file:
        ordernumber = len(file.readlines())
        if ordernumber == 0:
            ordernumber + 1
        return ordernumber

createorder()