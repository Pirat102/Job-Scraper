from plates import is_valid

def test_length():
    assert is_valid("WZY16000") == False

def test_all_letters_numbers():
    assert is_valid("WZY,:2") == False

def test_first_two_are_letters():
    assert is_valid("22WZY") == False

def test_letter_after_numbers():
    assert is_valid("WZ1Y") == False

def test_first_number_not_0():
    assert is_valid("WZY02") == False

def test_alphabetical():
    assert is_valid("WZYCS") == True

def test_all_numbers():
    assert is_valid("12345") == False

def test_correct_plate():
    assert is_valid("CS50") == True

