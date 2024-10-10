from seasons import calculate_minutes, convert

def test_minutes():
    assert calculate_minutes("1999-02-15".split("-")) == 13488480
    
def test_words():
    assert convert(13488480) == "thirteen million, four hundred eighty-eight thousand, four hundred eighty"
    
