# 1. kunna räkna antalet element i två listor och se vilken som är längst
# 2. kunna beräkna differensen mellan listorna
# 3. flytta halva differensen element till den mindre listan och returnera nya listor
# 4. om differensen är 1 eller 0 ska ingen lista ändras
# 5. ta hänsyn till ifall inparametrar inte är listor

from my_app.balansera_listor import *
import pytest

def test_balansera_listor__no_change_if_diff_1_or_0():
    # arrange
    lista_3_element = [1, 2, 3]
    lista_2_element = [4, 5]

    # act
    expected = lista_3_element, lista_2_element
    actual = balansera_listor(lista_3_element, lista_2_element)

    # assert
    assert actual == expected

def test_balansera_listor__list1_larger_than_list2():
    # arrange
    lista_4_element = [1, 2, 3, 4]
    lista_2_element = [4, 5]

    # act
    balanserad_lista_a = [1, 2,3]
    balanserad_lista_b = [4, 5, 4]

    expected = balanserad_lista_a, balanserad_lista_b
    actual = balansera_listor(lista_4_element, lista_2_element)

    # assert
    assert actual == expected