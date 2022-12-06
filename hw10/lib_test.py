from library import exponent_multiplication
import pytest

def test_exponent():
    assert exponent_multiplication(5, 5, exp=2)

def test_exponent_TypeError():
    with pytest.raises(TypeError):
        assert exponent_multiplication(5, "2", exp=2)

def test_exponent_when_exponent():
        assert exponent_multiplication(5, -2, exp=-0.5)

def test_exponent_returned_value_is_int():
        assert type(exponent_multiplication(5, -2, exp=0)) == int, 'returned value is not int'

def test_exponent_returned_value_is_float():
    assert type(exponent_multiplication(5.2, -2, exp=0)) == float, 'returned value is not float'

# TODO: аргументировать почему нету декоратора, доделать тесты,