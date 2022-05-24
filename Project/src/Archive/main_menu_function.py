from product_module import product_menu
from courier_module import courier_menu
from order_module import order_menu
from systems_module import system_menu

def main_menu_input(): ##function to call main menu input from user
    user_input = input('Press a Key: ')
    if user_input == '1':
        product_menu()
    elif user_input == '2':
        courier_menu()
    elif user_input == '3':
        order_menu()
    elif user_input == '4':
        system_menu()
    elif user_input == '0':
        exit()
    else:
        print('Sorry, invalid input, please try again')
        main_menu_input()