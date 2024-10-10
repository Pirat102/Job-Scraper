from working import convert
import pytest


def test_valid():
    assert convert("7:30 AM to 5:30 PM") == "07:30 to 17:30"
    assert convert("7 AM to 5 PM") == "07:00 to 17:00"
    
def test_invalid_input():
    with pytest.raises(ValueError):
        convert("7:30AM to 5:30PM")
        convert("7:30AM - 5:30PM")


def test_incomplete_input():
    with pytest.raises(ValueError):
        convert("09:00 AM")
        
    
def test_wrong_hours():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
        convert("13 AM to 14 PM")
    