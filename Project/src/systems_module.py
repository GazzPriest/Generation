from main_menu_function import menuline
from backup_module import backup_files
from restore_module import restore_files

def system_menu(): ## function to call system menu
    menuline()
    print()
    print('System Menu')
    print()
    menuline()
    print()
    print('1: Backup Files Menu \n2: Restore Files Menu \n0: Return to Main Menu')
    print()
    system_menu_input()

def system_menu_input(): ##function to call system menu input from user
    user_input = input('Press a Key: ')
    if user_input == '1':
        backup_files()
    elif user_input == '2':
        restore_files()
    elif user_input == '0':
        return 
    else:
        print('Sorry, invalid input, please try again')
        system_menu()