import random
from unittest.mock import Mock

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

