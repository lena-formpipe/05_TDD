

# 1 Vilka ekvivalensklasser har uttrycken? Skriv ner vad du tror kommer skrivas ut.
# 1a. x > 100
#       1. tal större än 100
#       2. tal mindre än eller lika med 99
# 1b. y == 42
#       1. tal exakt lika med 42
#       2. tal större än 42
#       3. tal mindre än 42
# 1c. len(text) >= 5
#       1. när längden av en sträng är lika med eller större än 5
#       2. längden på sträng mindre än 5 (kan aldrig var amindre än 0)
# 1d. z == True
#       1. Boolsk True
#       2. Boolsk False
# 1e. 8 < v < 16
#       1. tal mindre eller lika med 8
#       2. tal över eller lika med 16
#       3. tal mellan 8 och 16, d.v.s. 9 - 15
# 1f. w == 32 or w == 64 or w == 128
#       1. tal exakt 32
#       2. tal exakt 64
#       3. tal exakt 128
#       4. tal 31 eller lägre
#       5. tal 129 eller högre
#       6. tal mellan 33 och 63 (inkluderat)
# 1g. if x < 5: … elif x < 10: … elif x < 15: … else …
#       1. tal mindre än 5
#       2. tal 15 och uppåt
#       3. tal mellan 5 och 9 (inkl)
#       4. tal mellan 10 och 14 (inkl)

# 2 Det har smugit sig in kommentarer i stället för kod på några ställen.
# Skriv färdigt testfallen test_empty_list och test_number_list.
# Funktionen sum_list(lis) Returnerar summan av alla tal i listan
# --> just nu returnerar funktionen alltid None,så alla tester kommer att misslyckas, vilket är meningen med övningen.


def sum_list(list):
    # står inte i uppgiften att funktionen ska skrivas klart
    return None


# Är summan 0 eller None?
def test_empty_list(list):
    # arrange
    empty_list = []
    expected = 0
    # act
    actual = sum_list([empty_list])
    # assert
    assert actual == expected, "Resultatet borde vara 0"


def test_number_list(list):
    # testa med listor som har ett, två respektive fem element.
    assert sum_list([5]) == 5, "Resultatet borde vara 5"
    assert sum_list([5, 6]) == 11, "Resultatet borde vara 11"
    assert sum_list([1, 2, 10, 100, 50]) == 163, "Resultatet borde vara 163"