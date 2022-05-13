def update():
    my_dict = { 'Khan': 4, 'Ali': 2, 'Luna': 6, 'Mark': 11, 'Pooja': 8, 'Sara': 1}
    print(my_dict)

    first_user_input = input("What category do you wish to amend? :")
    second_user_input = input("Please enter the amended information. :")

    my_dict.update({first_user_input:second_user_input})

    print(my_dict)

update()

