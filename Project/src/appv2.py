products = {
    '1': 'Sandwich',
    '2': 'Crisps',
    '3': 'Chocolate',
    '4': 'Water',
}

print('Main Menu \n 1: Products Menu \n 0: Exit \n \n Press a key:')
mainmenu = input()
if mainmenu == '1':
    prodmenu = input('Products Menu \n \n 1: Print Products Menu \n 2: Create New Product \n 3: Update Existing Product \n 4: Delete Product \n 0: Return to Main Menu \n \n Press a key:')
    if prodmenu == '1':
        print("Available products are ", products)
    if prodmenu == '2':
       products[len(products) + 1] = input("What is the name of the new product?: ")
       print("Available products are ", products)
    ## create new product from input and append in products
    if prodmenu == '3':
       print("Available products are ", products)
       prodamend = input("What is the number of the product to be updated?: ")
       products.pop(prodamend)
       prodamend1 = input("Please enter the updated product name: ")
       products[prodamend] = prodamend1
       sorted(products.keys())
       print("Available products are ", products)
       ##for i in products:
           ##key = input("What is the number of the product to be updated?: ")
           ##value = input("Please enter the updated product name: ")
           ##products.update[key] = value
           ##print("Available products are ", products)
       ##prodamend = input("What is the number of the product to be updated?: ")
       ##products.update[prodamend] = input("Please enter the updated product name: ")
       ##print("Available products are ", products)
    ## print products with values, user input value, user input new name, update in products
    if prodmenu == '4':
        print("Available products are ", products)
        proddel = input("What is the number of the product to be removed?: ")
        products.pop(proddel)
        print("Available products are ", products)
    ## print products with values, user input value, delete in products
    ## if prodmenu == '0':
    ## return to main menu
if mainmenu == '0':
    print ("Goodbye!")