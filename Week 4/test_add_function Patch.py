import random
from unittest.mock import Mock, patch

def get_random_number():
    return random.randint(1, 10)

def add_number_with_random_number(a, get_random_number):
    return a + get_random_number()

def test_add_number_with_random_number():
    mock_get_random = Mock()
    mock_get_random.return_value = 5

    a = 5
    expected = 10
    
    actual = add_number_with_random_number(a, mock_get_random)

    assert actual == expected

def get_user_details():
    name = input('Please enter your name: ')
    age = int(input('Please enter your age: '))
    print(f"Thank you, your name is {name} and your age is {age}")

@patch("builtins.print")
@patch("builtins.input",  side_effect=["Gazz",37])

def test_get_user_details(mock_input, mock_print):
    get_user_details()
    mock_print.assert_called_with("Thank you, your name is Gazz and your age is 37")
    assert mock_input.call_count == 2
    assert mock_print.call_count == 1