from mainmenu_function import menuline
from product_module import product_menu
from courier_module import courier_menu
from order_module import order_menu

def mainmenu(): ## function to call main menu
    menuline()
    print()
    print('Main Menu')
    print()
    menuline()
    print()
    print('1: Products Menu \n2: Couriers Menu \n3: Orders Menu \n0: Exit')
    print()

def mainmenu_input(): ##function to call main menu input from user
    mainmenu()
    user_input = input('Press a Key: ')
    if user_input == '1':
        product_menu()
    elif user_input == '2':
        courier_menu()
    elif user_input == '3':
        order_menu()
    elif user_input == '0':
        exit()
    else:
        print('Sorry, invalid input, please try again')
    
    mainmenu_input()

mainmenu_input()