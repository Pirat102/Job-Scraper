
from twttr import shorten


def test_words():
    assert shorten("what's your name?") == "wht's yr nm?"
    assert shorten("TWITTER") == "TWTTR"

def test_numbers():
    assert shorten("123") == "123"
    assert shorten("- 1, 2, 3") == "- 1, 2, 3"



