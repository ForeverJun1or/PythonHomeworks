import math

from library import exponent_multiplication
import pytest

def test_exponent():
    assert exponent_multiplication(5, 5, exp=2)

def test_exponent_TypeError():
    with pytest.raises(TypeError):
        assert exponent_multiplication(5, "2", exp=2)

def test_exponent_ValueError():
    with pytest.raises(ValueError):
        assert exponent_multiplication(2, 3, exp=math.sqrt(-10))

def test_exponent_returned_value_is_int():
        assert type(exponent_multiplication(5, -2, exp=2)) == int or float, 'returned value is not int'

def test_exponent_returned_value_is_float():
    assert type(exponent_multiplication(5.2, -2, exp=2)) == float, 'returned value is not float'