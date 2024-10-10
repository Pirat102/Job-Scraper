from um import count

def test_case_insens():
    assert count("um") == 1
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("uM") == 1

def test_alnum_after():
    assert count("um umba") == 1
    assert count("ummm") == 0
    assert count("um1") == 0

def test_alnum_before():
    assert count("1um") == 0
    assert count("wum") == 0
    
def test_spaces():
    assert count("um ") == 1
    assert count(" um") == 1
    assert count("um um ") == 2
    