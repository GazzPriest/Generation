import csv

#createcourier

def createcourier(): ##function to create new courier
    with open('Project\data\couriers.csv', 'a', newline='') as csvfile:
        courier_info = ['id', 'Name', 'Phone']
        writer = csv.DictWriter(csvfile, fieldnames = courier_info)
        id_value = couriernumber()
        courier_name = input("What is the name of the new courier?: ")
        courier_phone = input("What is the courier's phone number?: ")
        couriers = [{'id': id_value, 'Name': courier_name, 'Phone': courier_phone}]
        if id_value == 1:
            writer.writeheader()
        else:
            pass
        writer.writerows(couriers)
        csvfile.close()
        print()
        #menuline()
        print()
        #courierrepeat()

def couriernumber():##function to track courier id numbers
    with open(r"Project\data\couriers.csv", 'r') as file:
        couriernumber = len(file.readlines())
        if couriernumber == 0:
            couriernumber + 1
        return couriernumber

createcourier()