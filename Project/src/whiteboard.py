from turtle import update


def updateorder(): ##function to update order information
    orders = {}
    with open('Project\data\orders.txt', 'r') as file:
        orders = file.readlines() #needs tidying up
    print()
    print("The currently open orders are ", orders)
    print()
    amend = open('Project\data\orders.txt', 'a')
    amend_user_input = int(input("What is the number of the order to be updated?: "))
    
    
    
    
    
    
    user_prod_input = input("What is the new order information?: ")
