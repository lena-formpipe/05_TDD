# 2b Skriv testfall som testar alla AK.
# User story: "som en användare vill jag veta hur många ord en mening innehåller så att jag kan skriva ner det."
# Acceptanskriterier:
# appen ska varna om det inte är en lista
# appen ska kunna hantera en tom lista
# appen ska kunna räkna ord som har mellanslag som avskiljare
#
# importera testfil till count_words()
from my_app.uppg2_2count_words import *
import pytest


def test_count_words_in_empty_string():
    # arrange
    empty_string = ""
    expected = 0

    # act
    actual = count_words(empty_string)

    # assert
    assert actual == expected, "Resultatt borde vara 0"


def test_count_words_if_not_a_string():
    # arrange
    not_a_string = True
    # act and assert
    with pytest.raises(TypeError):
        count_words(not_a_string)


def test_count_words_in_a_string():
    # arrange
    string_of_words = "Det här är en mening med 8 ord."
    expected = 8

    # act
    actual = count_words(string_of_words)

    # assert
    assert actual == expected, "Resultat borde vara 0"


