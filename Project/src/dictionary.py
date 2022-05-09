
#orders = {}
#with open("Project\data\orders.txt") as file:
#    for line in file:
#        line = line.strip()
#        orderlist = line.split(",")
#        orders[orderlist[0]] = orderlist[1]

#val = "Order Number"
#print(orders[val])

#        list = [line.rstrip("\n") for line in orderdict]
#           (key, val) = line.split()
#           orders[int(key)] = val
#    print(orders)        
#    print(len(orders))
#for loop to populate dict json.dumps
#    orderno = orders.get("Order Number")
    #print(orderno1)



def createorder():
    orders = {}
    with open('Project\data\orders.txt', 'a') as orderdict:
        order_number = 0
        order_number_tracker = order_number + 1
        orders["Order Number"] = order_number_tracker
        order_number_tracker + 1
        orders["Name"] = input("Enter name: ")
        orders["Address"] = input("Enter delivery address: ")
        orders["Phone"] = input("Enter phone number: ") #make an int
        orders["Courier"] = input("Enter courier number: ")
        orders["Status"] = "Preparing"
        orderdict.write("\n" + str(orders))
        orderdict.close()
        print(orders)

createorder()


#order number = order_number tracker
#order_number_tracker += 1