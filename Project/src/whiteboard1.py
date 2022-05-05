def createorder(): ##function to create new order
    orders = {}
    with open('Project\data\orders.txt') as f:
        for line in f:
            (key, val) = line.split()
            orders[int(key)] = val
    createorder= open('Project\data\orders.txt', 'a')   
    dictvalue = len(orders) + 1



##test


    
    user_prod_input = input("What is the name of the new product?: ")
    create.writelines('\n' + str(dictvalue) + ' ' + str(user_prod_input))
    products[dictvalue] = user_prod_input
    create.close()
    print()
    menuline()
    print()
    print("Available products are ", products)
    print()
    prodrepeat()