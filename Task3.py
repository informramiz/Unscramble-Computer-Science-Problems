"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

"""
A helper function to check if given number is a mobile number
"""
def is_mobile_number(number):
    """
    Mobile numbers have no parentheses, but have a space in the middle
    of the number to help readability. The prefix of a mobile number
    is its first four digits, and they always start with 7, 8 or 9.
    """
    return number[0] in ['7', '8', '9']

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

"""
A helper function to extract mobile code/prefix of a mobile number
Note: This function expects that the given number is a valid mobile number
"""
def extract_mobile_code(number):
    #The prefix of a mobile number is its first four digits
    return number[0:4]

def test_extract_mobile_code():
    assert(extract_mobile_code("93412 66159") == "9341")
test_extract_mobile_code()

"""
A helper function to extract mobile code/prefix of a fixed line number
Note: This function expects that the given number is a valid fixed line number
"""
def extract_fixed_line_code(number):
    #Fixed lines start with an area code enclosed in brackets. The area
    #codes vary in length but always begin with 0.
    end_index = number.find(")")
    return number[0:end_index+1]

def test_extract_fixed_line_code():
    assert(extract_fixed_line_code("(022)40840621") == "(022)")
test_extract_fixed_line_code()

"""
A helper function to extract mobile code/prefix of a telemarketer number
Note: This function expects that the given number is a valid telemarketer number number
"""
def extract_telemarketer_code(number):
    """
    Telemarketers' numbers have no parentheses or space, but they start
    with the area code 140.
    """
    return "140"

def test_extract_telemarketer_code():
    assert(extract_telemarketer_code("1402316533") == "140")
test_extract_telemarketer_code()

"""
A helper function to extract area code from number
"""
def extract_area_code(number):
    if is_mobile_number(number):
        return extract_mobile_code(number)
    elif is_fixed_line_number(number):
        return extract_fixed_line_code(number)
    elif is_telemarketer_number(number):
        return extract_telemarketer_code(number)

    return None

def test_extract_area_code():
    assert(extract_area_code("(022)40840621") == "(022)")
    assert(extract_area_code("1402316533") == "140")
    assert(extract_area_code("93412 66159") == "9341")
test_extract_area_code()

"""
-------------------Part A---------------------
Find all of the area codes and mobile prefixes called
by people in Bangalore.
Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""

def find_codes_called_from_bangalore(calls):
    bangalore_area_code = "(080)"
    area_codes = []
    for caller, receiver, _, _ in calls:
        if caller.startswith(bangalore_area_code):
            area_codes.append(extract_area_code(receiver))

    return area_codes

all_called_area_codes = find_codes_called_from_bangalore(calls)
unique_called_area_codes = sorted(set(all_called_area_codes))
print("The numbers called by people in Bangalore have codes:")
for code in unique_called_area_codes:
    print(code)

"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
bangalore_only_codes = [n for n in all_called_area_codes if n == "(080)"]
percentage_of_bangalore_codes = (len(bangalore_only_codes) / float(len(all_called_area_codes))) * 100
print("%.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore." % percentage_of_bangalore_codes)
