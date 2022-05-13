products = ['Sandwich', 'Drink', 'Crisps', 'Chocolate', 'Sweets'] ##should this be a dictionary?

print('Main Menu \n 1: Products Menu \n 0: Exit \n \n Press a key:')
mainmenu = input()
if mainmenu == '1':
    print('Products Menu \n \n 1: Print Products Menu \n 2: Create New Product \n 3: Update Existing Product \n 4: Delete Product \n 0: Return to Main Menu \n \n Press a key:')
    prodmenu = input()
    if prodmenu == '1':
        print(f'Current available products are: ' + str(products[0:]))
    elif prodmenu == '2':
        products.append(input('Please enter the name of the new product: ')) ##need code to save new item
        print(products)
    ##elif prodmenu == '3':
        ##products.remove(input('Please enter the name of the product to be amended: '))
        ##products.append(input('Please enter the amended details: '))
        ##print(products)
    ##elif prodmenu == '4':
        ##products.remove(input('Please enter the name of the product to be removed: '))
        ##print(products)
    ##elif prodmenu == '0': need code to return to main menu
        ##try:
            ##prodmenu = int(input())
        ##except:
            ##print('Invalid input. Please enter a number. Thank you')
elif mainmenu == '0': 
    print('Goodbye') ##need code to exit system