import pytest
from Figures import Point, Line, Triangle


def test_Point_TypeError():
    with pytest.raises(TypeError):
        assert Point(0, '5')


def test_Point_return_type():
    assert type(Point(0, 5)) == Point, 'return\'s type isn\'t Point'


def test_Line_TypeError():
    with pytest.raises(TypeError):
        assert Line(Point(0, 5), 5)


def test_Line_return_type():
    assert type(Line(Point(0, 5), Point(0, 10))) == Line, 'return\'s type isn\'t Line'


def test_Line_length_return_type():
    assert type(Line(Point(0, 5), Point(0, 10)).length()) == int or float, 'return\'s type isn\'t int or float'


def test_Triangle_TypeError():
    with pytest.raises(TypeError):
        assert Triangle(Point(0, 0), Point(0, 5), [5, 0])


def test_Triangle_return_type():
    assert type(Triangle(Point(0, 0), Point(0, 5), Point(5, 0))) == Triangle, 'return\'s type isn\'t Triangle'

def test_Triangle_area_return_type():
    assert type(Triangle(Point(0, 0), Point(0, 5), Point(5, 0))) == int or float, 'return\'s type isn\'t int or float'

