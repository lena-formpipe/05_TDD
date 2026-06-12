# uppgift 2_1c skriv ett testfall
# hur skulle man skriva bättre?
from my_app.uppg2_1celsius import *
import pytest

Def test_c_to_f():
    # arrange
    zero_degree = 0
	expected_zero_degree_in_fahrenheit = 32
    celsius_below_absolute_freezingpoint = -300
    # act and assert
    assert c_to_f(celsius_below_absolute_freezingpoint) == None
    assert c_to_f(zero_degree) == expected_zero_degree_in_fahrenheit
