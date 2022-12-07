import math
from abc import ABC, abstractmethod


def check_int_or_float(func):
    def wrapper(*args, **kwargs):
        for arg in range(1, len(args) - 1):
            if not isinstance(arg, (int, float)):
                raise TypeError
        for kwarg in kwargs:
            if not isinstance(kwarg, (int, float)):
                raise TypeError
        result = func(*args, **kwargs)
        return result

    return wrapper


class Point:
    x = None
    y = None

    def __init__(self, x: int | float, y: int | float):
        if not isinstance(x and y, int | float):
            raise TypeError
        # check here numbers
        self.x = x
        self.y = y


# class Figure:
#
#     def area(self):
#         return self._area()
#
#     def length(self):
#         return self._length()
#
#     def _area(self):
#         raise NotImplementedError
#
#     def _length(self):
#         raise NotImplementedError


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
    _begin = None
    _end = None

    def __init__(self, begin, end):
        if not isinstance(begin and end, Point):
            raise TypeError
        # check here Point
        self.begin = begin
        self.end = end

    def length(self):
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

    def area(self):
        first_side_length = Line(first_point, second_point).length()
        second_side_length = Line(second_point, third_point).length()
        third_side_length = Line(third_point, first_point).length()
        p = (first_side_length + second_side_length + third_side_length) / 2
        pp = p * (p - first_side_length) * (p - second_side_length) * (p - third_side_length)
        result = math.sqrt(pp)
        return result


first_point = Point(25, 16)
second_point = Point(45, 21)
third_point = Point(67, 32)

triangle1 = Triangle(first_point, second_point, third_point)
print(triangle1.area())
