import json

def createorder():
    neworder = open('Project\data\orders.txt', 'a')
    orders = {}
    
    
    #for loop to populate dict json.dumps




    orderno = orders.get("Order Number")
    #print(orderno1)
    orders["Order Number"] = orderno
    orders["Name"] = input("Enter name: ")
    orders["Address"] = input("Enter delivery address: ")
    orders["Phone"] = input("Enter phone number: ") #make an int
    orders["Courier"] = input("Enter courier number: ")
    orders["Status"] = "Preparing"
    neworder.write("\n" + str(orders))
    neworder.close()
    print(orders)

createorder()