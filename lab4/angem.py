from math import acos, sqrt
from PyQt5.QtCore import Qt


class Point:
    def __init__(self, x, y, color=Qt.black):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"point({self.x}, {self.y})"


class Vector:
    def __init__(self, x: int | Point, y: int | Point):
        if isinstance(x, Point) and isinstance(y, Point):
            self.x = y.x - x.x
            self.y = y.y - x.y
        else:
            self.x = x
            self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __bool__(self):
        return self.x or self.y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def angle(self, other):
        return acos(self * other / abs(self) / abs(other))

    def __str__(self):
        return f"vector({self.x}, {self.y})"


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

    def __str__(self):
        return f"line( (x - {self.point.x}) / {self.vector.x} = (y - {self.point.y}) / {self.vector.y})"
