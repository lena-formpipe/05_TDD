"""
ACCEPTANSKRITERIER
AK1: om tal n eller limit rader inte är en int ska funktionen returnera TypeError
AK2: om n och limit är int ska funktionen returnera en utskrift av multiplikationstabellen enligt limit
AK3: om limit > 100 så ska funktionen returnera False
"""



from my_app.multiplication_table import *
import pytest

def test_multiplication_table__n_is_not_int():
    # Arrange
    n_not_int = "12a"
    limit_is_int = 3
    # act & assert
    with pytest.raises(TypeError):
        multiplication_table(n_not_int, limit_is_int)

def test_multiplication_table__limit_is_not_int():
    # Arrange
    limit_not_int = "12b"
    n_is_int = 5
    # act & assert
    with pytest.raises(TypeError):
        multiplication_table(n_is_int, limit_not_int)

def test_multiplication_table__multiply():
    # arrange
    n = 4
    limit = 2

    # act
    expected = [4, 8]
    actual = multiplication_table(n, limit)

    # assert
    assert actual == expected

