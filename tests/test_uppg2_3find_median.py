# testfil till find_median()


from my_app.uppg2_3find_median import *
import pytest


# from src.my_app.find_median import find_median


# Tasks:
# 1. Hitta det mittersta talet i en lista av tal
# modulo % 2 == 1 innebär att listan har ojämnt antal element
# 2. kontrollera att listan består av tal
#     if not isinstance(numbers, int):
#         raise TypeError(f"Input måste vara ett heltal, inte {type(numbers)}.")
# 3. om listan består av jämnt antal element ska de två mittersta talen summeras och delas med 2
# modulo % 2 == 0 innebär att listan har jämnt antal element



def test_list_has_middle_position():
    list_all_positive = [5, 20, 100]
    list_some_negative = [-10, -5, 100]
    # kom ihåg att funktionen sorterar listan!
    assert find_median(list_some_negative) == -5
    assert find_median(list_all_positive) == 20

def test_list_has_no_middle_position():
    list_all_positive = [5, 20, 100, 120]
    list_some_negative = [-10, -5, 3, 100]
    # kom ihåg att funktionen sorterar listan!
    assert find_median(list_some_negative) == -1
    assert find_median(list_all_positive) == 60

# def test_empty_list():
    # TODO