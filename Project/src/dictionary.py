def ordernumber():
    with open("Project\data\orders.txt", 'r') as file:
        ordercount = len(file.readlines()) + 1
        return(ordercount)

def createorder():
    orders = {}
    with open('Project\data\orders.txt', 'a') as orderdict:
        orders["Order Number"] = ordernumber()
        orders["Name"] = input("Enter name: ")
        orders["Address"] = input("Enter delivery address: ")
        orders["Phone"] = input("Enter phone number: ") #make an int
        orders["Courier"] = input("Enter courier number: ")
        orders["Status"] = "Preparing"
        orderdict.write("\n" + str(orders))
        orderdict.close()
        print(orders)

createorder()
