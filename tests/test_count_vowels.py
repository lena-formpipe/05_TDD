# testfil till count_vowels()
from my_app.count_vowels import *
# pycharm föreslog följande rad för att slippa röd markering under count_vowels men då fick jag fel
# from src.my_app.count_vowels import count_vowels


def test_no_vowels():
    # arrange
    expected = 0
    assert count_vowels("qwrt") == expected
    assert count_vowels("Tt") == expected
    assert count_vowels("123 123") == expected
    assert count_vowels("") == expected


def test_some_vowels():
    assert count_vowels("AaEeIiOoUuYyÅåÄäÖö") == 18