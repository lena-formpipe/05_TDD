"""
LÄGGER DENNA I TEST-MAPPEN
4 Betrakta funktionen is_sorted_ascending(numbers).
Den ska returnera True om listan numbers är sorterad i stigande ordning, False annars.
a Vilka ekvivalensklasser har numbers?
--> TRUE och FALSE
"""

def is_sorted_ascending(numbers):
    return False
"""
 4b Formulera krav och acceptanskriterier för funktionen.
 Som en utvecklare
 vill jag ha en funktion som kan tala om ifall en lista med nummer är sorterad i stigande ordning
 så att jag kan använda denna funktion i min kod.

 Acceptanskriterier:
 	Sorterad i stigande ordning TRUE
 	Sorterad i minskande ordning FALSE
 	Helt osorterad FALSE
   Tom lista FALSE
"""

# 4c Skriv testfall för funktionen.

def test_is_sorted_ascending_true():
    # arrange
    ascending_list = [1, 2, 3, 4, 5]
    expected = True
    # act
    actual = is_sorted_ascending(ascending_list)
    # assert
    assert actual == expected


def test_is_sorted_ascending__descending():
    # arrange
    descending = [5, 4, 3, 2, 1]
    expected = False
    # act
    actual = is_sorted_ascending(descending)
    # assert
    assert actual == expected


def test_is_sorted_ascending__unsorted():
    # arrange
    unsorted = [1, 5, 3, 2, 4]
    expected = False
    # act
    actual = is_sorted_ascending(unsorted)
    # assert
    assert actual == expected


def test_is_sorted_ascending__emptylist():
    # arrange
    emptylist = []
    expected = False
    # act
    actual = is_sorted_ascending(emptylist)
    # assert
    assert actual == expected
