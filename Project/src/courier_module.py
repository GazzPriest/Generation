import csv

def couriermenu(): ## function to call courier menu
    import main
    main.menuline()
    print()
    print('Courier Menu')
    print()
    main.menuline()
    print()
    print('1: Print Couriers List \n2: Create New Courier \n3: Update Existing Courier \n4: Delete Courier \n0: Return to Main Menu')
    print()
    couriermenu_input()

def couriermenu_input(): ##function to call courier menu input from user
    user_input = input('Press a Key: ')
    if user_input == '1':
        printcourier()
    elif user_input == '2':
        createcourier()
    elif user_input == '3':
        updatecourier()
    elif user_input == '4':
        deletecourier()
    elif user_input == '0':
        import main
        main.mainmenu()
    else:
        print('Sorry, invalid input, please try again')
        import product_module
        product_module.productmenu()

def printcourier(): ##function to print list of current products
    with open('Project\data\couriers.csv', 'r') as file:
        reader = csv.reader(file)
        print()
        import main
        main.menuline()
        print()
        print("Available couriers are")
        print()
        for couriers in reader:
            print(couriers)
    print()
    main.menuline()
    input("Press Enter to return to the Couriers Menu: ")
    couriermenu()

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
        import main
        main.menuline()
        print()
        courierrepeat()

def couriernumber():##function to track courier id numbers
    with open(r"Project\data\couriers.csv", 'r') as file:
        couriernumber = len(file.readlines())
        if couriernumber == 0:
            couriernumber + 1
        return couriernumber

def courierrepeat(): ##function that allows user to add couriers one by one without moving menus
    user_input = input("Would you like to add another courier? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        createcourier()
    elif user_input == 'N' or user_input == 'n':
        couriermenu()
    else:
        print('Sorry, invalid input, please try again')
        courierrepeat()

def updatecourier(): ##function to update current courier
    courierlist = []
    with open('Project\data\couriers.csv', 'r') as file:
        reader = csv.reader(file)
        print()
        import main
        main.menuline()
        print()
        print("Available couriers are")
        print()
        for couriers in reader:
            courierlist.append(couriers)
            print(couriers)
        print()
        user_input = int(input("Please enter the ID of the courier you would like to update?: "))
        for i in range(1, len(courierlist[0])):
            new_info = input("Enter new information for " + str(courierlist[0][i] + ": "))
            courierlist[user_input][i] = new_info
        with open('Project\data\couriers.csv', 'w', newline="") as file:
            writer = csv.writer(file)
            for i in range(len(courierlist)):
                writer.writerow(courierlist[i])
        print()
        main.menuline()
        print()
        updatecourierrepeat()

def updatecourierrepeat(): ##function that allows user to update couriers one by one without moving menus
    user_input = input("Would you like to amend another courier? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        updatecourier()
    elif user_input == 'N' or user_input == 'n':
        couriermenu()
    else:
        print('Sorry, invalid input, please try again')
        updatecourierrepeat()

def deletecourier(): ##function to remove courier
    readlist = []
    with open('Project\data\couriers.csv', 'r') as file:
        reader = csv.reader(file)
        print()
        import main
        main.menuline()
        print()
        print("Available couriers are")
        print()
        for couriers in reader:
            readlist.append(couriers)
            print(couriers)
        print()
    file.close()

    file=open("Project\data\couriers.csv", 'r')
    reader = csv.reader(file)
    courierlist=[]
    user_input=int(input("Please enter the courier to be deleted: "))
    Found = False
    for row in reader:
        if row[0]==str(user_input):
            Found=True
        else:
            courierlist.append(row)
    file.close
    
    if Found==False:
        print("Sorry, that courier ID has has not been found")
    else:
        file=open("Project\data\couriers.csv", 'w+', newline='')
        writer=csv.writer(file)
        writer.writerows(courierlist)
        file.seek(0)
        reader=csv.reader(file)
        for row in reader:
            print("Available couriers are")
            print()
            printcourier()
            print()
            deletecourierrepeat()
        file.close()

def deletecourierrepeat(): ##function that allows user to delete products one by one without moving menus
    user_input = input("Would you like to delete another courier? Please type Y or N: ")
    if user_input == 'Y' or user_input == 'y':
        deletecourier()
    elif user_input == 'N' or user_input == 'n':
        couriermenu()
    else:
        print('Sorry, invalid input, please try again')
        deletecourierrepeat()
