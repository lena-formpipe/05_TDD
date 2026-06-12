from my_app.autocomplete_list import *
import pytest

def test_autocomplete_list__input_is_not_string():
    # Arrange
    test_input_not_a_string = 123
    name_list = ["anna", "marianne", "peter"]
    # act & assert
    with pytest.raises(TypeError):
        autocomplete_list(test_input_not_a_string, name_list)

def test_autocomplete_list__name_is_not_a_list():
    # arrange
    test_name_not_a_list = 123
    user_input = "anna"
    # act & assert
    with pytest.raises(TypeError):
        autocomplete_list(user_input, test_name_not_a_list)


def test_autocomplete_list__input_matches_name():
    # arrange
    name_list1 = ["anna", "mariANNE", "Peter"]
    input1 = "Ann"

    # act
    expected = ["anna", "mariANNE"]
    actual = autocomplete_list(input1, name_list1)

    # assert
    assert actual == expected

def test_autocomplete_list__input_no_matches():
    # arrange
    name_list1 = ["anna", "mariANNE", "Peter"]
    input1 = "Olle"

    # act
    expected = False
    actual = autocomplete_list(input1, name_list1)

    # assert
    assert actual == expected
