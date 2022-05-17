def menuline(): ## function for ease of menu readability
    print('------------------------------------------------------')

def mainmenu(): ## function to call main menu
    menuline()
    print()
    print('Main Menu')
    print()
    menuline()
    print()
    print('1: Products Menu \n2: Couriers Menu \n3: Orders Menu \n0: Exit')
    print()
    mainmenu_input()

def mainmenu_input(): ##function to call main menu input from user
    user_input = input('Press a Key: ')
    if user_input == '1':
        import product_module
        product_module.productmenu()
    elif user_input == '2':
        import courier_module
        courier_module.couriermenu()
    elif user_input == '3':
        import order_module
        order_module.ordermenu()
    elif user_input == '0':
        exit()
    else:
        print('Sorry, invalid input, please try again')
        mainmenu()

mainmenu()