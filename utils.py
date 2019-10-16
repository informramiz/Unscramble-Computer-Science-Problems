"""
A helper function to check if given number is a mobile number
"""
def is_mobile_number(number):
    """
    Mobile numbers have no parentheses, but have a space in the middle
    of the number to help readability. The prefix of a mobile number
    is its first four digits, and they always start with 7, 8 or 9.
    """
    return number[0] in ['7', '8', '9'] and number.find(" ") != -1

#do a quick test to verify above method
def test_is_mobile_number():
    assert(is_mobile_number("93412 66159") == True)
    assert(is_mobile_number("3341266159") == False)
test_is_mobile_number()


"""
A helper function to check if given number is a fixed line number
"""
def is_fixed_line_number(number):
    """
    Fixed lines start with an area code enclosed in brackets. The area
    codes vary in length but always begin with 0.
    """
    if len(number) < 3:
        return False

    return number.find("(") != -1 and number.find(")") != -1 and number[1] == '0'

def test_is_fixed_line_number():
    assert(is_fixed_line_number("(022)40840621") == True)
    assert(is_fixed_line_number("02240840621") == False)
test_is_fixed_line_number()

"""
A helper function to check if given number is a Telemarketer number
"""
def is_telemarketer_number(number):
    """
    Telemarketers' numbers have no parentheses or space, but they start
    with the area code 140.
    """
    return len(number) >= 3 and number.startswith("140")

def test_is_telemarketer_number():
    assert(is_telemarketer_number("1402316533") == True)
    assert(is_telemarketer_number("(022)40840621") == False)
test_is_telemarketer_number()
