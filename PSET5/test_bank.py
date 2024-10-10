from bank import value

def test_hello():
    assert value("hello") == 0

def test_HELLO():
    assert value("HELLO") == 0

def test_start_with_h():
    assert value("hipo") == 20

def test_other():
    assert value("parrot") == 100
