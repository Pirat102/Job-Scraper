from fuel import *
import pytest

def test_X_great_than_Y():
    with pytest.raises(ValueError):
        convert("5/4")

def test_Y_not_0():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_correct_input():
    assert convert("3/4") == 75

def test_empty_tank():
    assert gauge(1) == "E"
    assert gauge(0.5) == "E"

def test_full_tank():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_fuel_tank():
    assert gauge(50) == "50%"
    assert gauge(70) == "70%"
    assert gauge(2) == "2%"

