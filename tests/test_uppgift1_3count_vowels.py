# ÖVNING 1_3 count_vowels

from my_app.uppgift1_3count_vowels import *
import pytest


# test av inga vokaler
def test_count_vowels__no_vowels():
    # arrange
    expected = 0
    # act and assert
    assert count_vowels("qwrt") == expected
    assert count_vowels("Tt") == expected
    assert count_vowels("123 123") == expected
    assert count_vowels("") == expected


# test av tom sträng
def test_count_vowels__empty_string():
    # arrange
    expected = 0
    # act and assert
    assert count_vowels("") == expected


# test av flera vokaler
def test_count_vowels__some_vowels():
    # är det tillåtet att ha både arrange, act och assert ihop på detta sätt?
    assert count_vowels("AaEeIiOoUuYyÅåÄäÖö") == 18
    assert count_vowels("aaaaääääÄÄÄÄöÖ") == 14


# test av fel format inparameter
def test_count_vowels__not_a_string():
    # här vet jag inte riktigt hur man ska dela upp...
    not_a_string = 123
    with pytest.raises(TypeError):
        count_vowels(not_a_string)

