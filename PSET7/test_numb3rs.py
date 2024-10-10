from numb3rs import validate

def test_string():
    validate("cat")
    
def test_too_big_number():
    assert validate("512.512.512.512") == False
    assert validate("12.512.12.12") == False
    assert validate("12.12.512.12") == False
    assert validate("12.12.12.512") == False
    assert validate("12.512.512.512") == False

def test_correct_ip():
    assert validate("255.255.255.255") == True
    assert validate("1.15.25.199") == True
    
def test_too_long_ip():
    assert validate("122.5.12.49.50") == False
    assert validate("122.5.12.49.50.100") == False
    
def test_too_short():
    assert validate("1") == False
    assert validate("1.") == False
    assert validate("1.100") == False
    assert validate("1.100.200") == False