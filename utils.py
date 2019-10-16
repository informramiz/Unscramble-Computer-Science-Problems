

def is_fixed_line_code(code):
    return code.startswith("(") and code.endswith(")")

def test_is_fixed_line_code():
    assert(is_fixed_line_code("(022)") == True)
    assert(is_fixed_line_code("(022") == False)
test_is_fixed_line_code()

def is_telemarketer_code(code):
    return code == "140"

def test_is_telemarketer_code():
    assert(is_telemarketer_code("140") == True)
    assert(is_telemarketer_code("141") == False)
test_is_telemarketer_code()

def is_mobile_code(code):
    return code[0] in ["7", "8", "9"]

def test_is_mobile_code():
    assert(is_mobile_code("9341") == True)
    assert(is_mobile_code("140") == False)
    assert(is_mobile_code("(134)") == False)
test_is_mobile_code()
