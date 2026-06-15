"""
uppgift 1_5
Formulera testfall för en funktion som hittar näst största talet i en lista!
Returnerar det nästa största talet i listan
Returnerar None om det inte finns något
Om det är delad förstaplats så returneras det talet.

uppgiften innefattar inte att skriva klart funktionen
"""
import pytest

def find_2nd_max(list):
    return None


def test_find_2nd_max__two_of_same_number():
    # arrange
    list_two_of_same_number = [5, 5, 1]
    expected = 5

    # act
    actual = find_2nd_max(list_two_of_same_number)

    assert actual == expected


def test_find_2nd_max__empty_string():
    # arrange
    empty_string = []
    expected = None
    # act
    actual = find_2nd_max(empty_string)
    # assert
    assert actual == expected


def test_find_2nd_max__only_one_number():
    # arrange
    one_number = [4]
    expected = None
    # act
    actual = find_2nd_max(one_number)
    # assert
    assert actual == expected


def test_find_2nd_max__not_a_string():
    # här vet jag inte riktigt hur man ska dela upp...
    not_a_string = 123
    with pytest.raises(TypeError):
        find_2nd_max(not_a_string)