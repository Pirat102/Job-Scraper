from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12 # type: ignore
    jar = Jar(15)
    assert jar.capacity == 15
    jar = Jar(20, 15)
    assert jar.capacity, jar.size == (20, 15)
    with pytest.raises(ValueError):
        Jar(12, 15)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(15)
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(2)
    assert jar.size == 7
    with pytest.raises(ValueError):
        jar.deposit(6)


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(2)
    with pytest.raises(ValueError):
        jar.deposit(5)
        jar.withdraw(6)
    jar.size = 10
    jar.withdraw(2)
    assert jar.size == 8
    jar.withdraw(5)
    assert jar.size == 3