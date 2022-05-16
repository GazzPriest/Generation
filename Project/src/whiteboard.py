import csv

def printorder(): ##function to print list of current orders
    with open('Project\data\orders.csv', 'r') as file:
        reader = csv.reader(file)
        print()
        #menuline()
        print()
        print("Currently open orders are")
        print()
        for orders in reader:
            if orders[5] == "Delivered" or orders[5] == "Cancelled":
                continue
            print(orders)
    print()
    #menuline()
    input("Press Enter to return to the orders Menu: ")
    #ordermenu()

printorder()





