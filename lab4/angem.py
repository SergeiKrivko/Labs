from math import acos, sqrt
from PyQt5.QtCore import Qt


class Point:
    def __init__(self, x: int | float, y: int | float, color=Qt.black):
        self.x = x
        self.y = y
        self.color = color

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"point({self.x:4g}, {self.y:4g})"


class Vector:
    def __init__(self, x: int | float | Point, y: int | float | Point):
        if isinstance(x, Point) and isinstance(y, Point):
            self.x = y.x - x.x
            self.y = y.y - x.y
        else:
            self.x = x
            self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

    def __bool__(self):
        return self.x or self.y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def parallel(self, other):
        if other.x == 0:
            return self.x == 0
        if other.y == 0:
            return self.y == 0
        return abs(self.x / other.x - self.y / other.y) < 1e-10

    def angle(self, other):
        return acos(self * other / abs(self) / abs(other))

    def __str__(self):
        return f"vector({self.x:4g}, {self.y:4g})"


class Segment:
    def __init__(self, p1, p2, color=Qt.black):
        self.p1 = p1
        self.p2 = p2
        self.color = color

    def __str__(self):
        return f"segment({self.p1}, {self.p2})"


class Line:
    def __init__(self, obj1: Point, obj2: Point | Vector, color=Qt.black):
        self.point = obj1
        if isinstance(obj2, Point):
            self.vector = Vector(obj1, obj2)
        else:
            self.vector = obj2
        self.color = color

    def get_x(self, y):
        return self.vector.x * (y - self.point.y) / self.vector.y + self.point.x

    def get_y(self, x):
        return self.vector.y * (x - self.point.x) / self.vector.x + self.point.y

    def intersection(self, other):
        if self.vector.parallel(other.vector):
            return None
        if self.vector.y == 0:
            return Point(other.get_x(self.point.y), self.point.y)
        if other.vector.y == 0:
            return Point(self.get_x(other.point.y), other.point.y)
        y = (self.vector.x / self.vector.y * self.point.y - other.vector.x / other.vector.y * other.point.y -
             self.point.x + other.point.x) / (self.vector.x / self.vector.y - other.vector.x / other.vector.y)
        return Point(self.get_x(y), y)

    def __str__(self):
        return f"line( (x - {self.point.x}) / {self.vector.x} = (y - {self.point.y}) / {self.vector.y} )"


class Circle:
    def __init__(self, center, radius, color=Qt.black):
        self.center = center
        self.radius = radius
        self.color = color

    def __str__(self):
        return f"circle({self.center}, {self.radius:4g})"
