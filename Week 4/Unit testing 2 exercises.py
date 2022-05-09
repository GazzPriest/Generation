from country_info import get_country_code, get_country_currency, transform, show_country_info

def test_get_country_code():
    test_countries = [
        {"name":"United Kingdom", "alpha3Code": "UK"},
        {"name":"United States", "alpha3Code": "USA"}
    ]

    test_name = "United Kingdom"
    expected = "UK"
    actual = get_country_code(test_countries, test_name)

    assert expected == actual
    print("Code Passed")

test_get_country_code()

#########################################################

def test_get_country_currency():
    test_currencies = [
        {"name":"United Kingdom", "currencies":[{"code": "GBP", "name": "British Pound", "symbol": "£"}]}]

    test_currency = "United Kingdom"
    expected = "GBP"
    actual = get_country_currency(test_currencies, test_currency)

    assert expected == actual
    print("Currency Passed")

test_get_country_currency()

########################################################

def test_transform():
    def mock_get_countries():
        return [{"name": "United Kingdom", "alpha3Code": "UK", "currencies": [{"code": "GBP"}]}]
    
    test_name = "United Kingdom"
    expected = {"name": "United Kingdom", "country_code": "UK", "currency_code": "GBP"}
    actual = transform(test_name, mock_get_countries) #added get_countries to line 27 of country_info.py to add positional argument
    
    assert actual == expected
    print("Transform Passed")

test_transform()

#######################################################

def test_show_country_info():
    def mock_get_countries():
        return [{"name": "United Kingdom", "alpha3Code": "UK", "currencies": [{"code": "GBP"}]}]
    def mock_print(*args):
        pass
    def mock_input(msg):
        return 0
    
    expected = {"name": "United Kingdom", "country_code": "UK", "currency_code": "GBP"}
    actual = show_country_info(mock_get_countries, transform, mock_print, mock_input)
    
    assert expected == actual
    print("Country Info Passed")