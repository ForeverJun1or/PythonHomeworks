import math
from abc import ABC, abstractmethod


class Point:
    x = None
    y = None

    def __init__(self, x: int | float, y: int | float):
        if not isinstance(x or y, int | float):
            raise TypeError
        # check here numbers
        self.x = x
        self.y = y


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


class Line(Figure):
    def __init__(self, begin, end):
        if not isinstance(begin and end, Point):
            raise TypeError
        self.begin = begin
        self.end = end

    def length(self) -> int | float:
        res = ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5
        return res


class Triangle(Figure):
    def __init__(self, first_point: Point, second_point: Point, third_point: Point):
        if not isinstance(first_point and second_point and third_point, Point):
            raise TypeError
        # check here Point
        self.first_point = first_point
        self.second_point = second_point
        self.third_point = third_point

    def area(self) -> int | float:
        first_side_length = Line(self.first_point, self.second_point).length().__round__(2)
        second_side_length = Line(self.second_point, self.third_point).length().__round__(2)
        third_side_length = Line(self.third_point, self.first_point).length().__round__(2)
        p = (first_side_length + second_side_length + third_side_length) / 2
        pp = p * (p - first_side_length) * (p - second_side_length) * (p - third_side_length)
        result = math.sqrt(pp.__round__(2)).__round__(2)
        return result
