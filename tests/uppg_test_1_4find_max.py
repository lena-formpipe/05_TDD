"""
Uppgift 1_4
 Formulera testfall för en funktion som hittar största talet i en lista.
 Returnerar det största talet i listan
 Returnerar None om det inte finns något 
"""

import pytest

def find_max(list):
    return None

# Returnerar None om det inte finns något
def test_find_max__list_empty():
    # arrange
    expected = None
    # act
    actual = find_max([])
    #assert
    assert actual == expected

def test_find_max__one():
    # arrange
    one_number = [1]
    expected = 1

    #act
    actual = find_max(one_number)

    # assert
    assert actual == expected


def test_find_max__three_numbers():
    # arrange
    three_numbers = [-1, 2, 3]
    expected = 3

    # act
    actual = find_max(three_numbers)

    # assert
    assert actual == expected

def test_find_max__no_max_number():
    # arrange
    all_same_numbers = [5, 5, 5]
    expected = None
    # act
    actual = find_max(all_same_numbers)
    # assert
    assert actual == expected


def test_find_max__not_a_string():
    # arrange
    not_a_string = 123
    with pytest.raises(TypeError):
        find_max(not_a_string)


