import math
from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def area(self):
        return self._area()

    def length(self):
        return self._length()

    def _area(self):
        raise NotImplementedError

    def _length(self):
        raise NotImplementedError


class Point:
    _x = None
    _y = None

    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        self._y = value


class Line(Figure):
    _begin = None
    _end = None

    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    @property
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._begin = value

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._end = value

    def length(self) -> int | float:
        res = ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5
        return res


class Triangle(Figure):
    _first_point = None
    _second_point = None
    _third_point = None

    def __init__(self, first_point: Point, second_point: Point, third_point: Point):
        self.first_point = first_point
        self.second_point = second_point
        self.third_point = third_point

    @property
    def first_point(self):
        return self._first_point

    @first_point.setter
    def first_point(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._first_point = value

    @property
    def second_point(self):
        return self._second_point

    @second_point.setter
    def second_point(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._second_point = value

    @property
    def third_point(self):
        return self._third_point

    @third_point.setter
    def third_point(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._third_point = value

    def area(self) -> int | float:
        first_side_length = Line(self.first_point, self.second_point).length().__round__(2)
        second_side_length = Line(self.second_point, self.third_point).length().__round__(2)
        third_side_length = Line(self.third_point, self.first_point).length().__round__(2)
        p = (first_side_length + second_side_length + third_side_length) / 2
        pp = p * (p - first_side_length) * (p - second_side_length) * (p - third_side_length)
        result = math.sqrt(pp.__round__(2)).__round__(2)
        return result

    def __eq__(self, other):
        return self.area() == other.area() if isinstance(other, Triangle) else False

    def __ne__(self, other):
        return self.area() != other.area() if isinstance(other, Triangle) else False

    def __gt__(self, other):
        return self.area() > other.area() if isinstance(other, Triangle) else False

    def __lt__(self, other):
        return self.area() < other.area() if isinstance(other, Triangle) else False

    def __ge__(self, other):
        return self.area() >= other.area() if isinstance(other, Triangle) else False

    def __le__(self, other):
        return self.area() <= other.area() if isinstance(other, Triangle) else False

    def __str__(self):
        return f'{self.first_point.x},{self.first_point.y}--{self.second_point.x},{self.second_point.y}--{self.third_point.x},{self.third_point.y}'
