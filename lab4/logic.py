from PyQt5.QtCore import QThread, pyqtSignal

from angem import Vector, Line, Circle


def get_circle(points):
    res_center = points[0]
    max_radius = 0
    for i in range(len(points) - 2):
        for j in range(i + 1, len(points) - 1):
            for k in range(j + 1, len(points)):
                center, radius = get_3points_center(points[i], points[j], points[k])
                if radius > max_radius:
                    max_radius = radius
                    res_center = center
            yield len(points) - j - 1
    yield Circle(res_center, max_radius ** 0.5)


def get_3points_center(p1, p2, p3):
    vector1 = Vector(p1, p2)
    vector2 = Vector(p2, p3)
    vector3 = Vector(p3, p1)

    if vector1 * vector2 >= 0:
        return p3 + vector3 / 2, (vector3 * vector3) / 4
    if vector2 * vector3 >= 0:
        return p1 + vector1 / 2, (vector1 * vector1) / 4
    if vector3 * vector1 >= 0:
        return p2 + vector2 / 2, (vector2 * vector2) / 4

    line1 = Line(p1 + vector1 / 2, Vector(vector1.y, -vector1.x))
    line2 = Line(p2 + vector2 / 2, Vector(vector2.y, -vector2.x))
    point = line1.intersection(line2)
    v = Vector(point, p1)
    return point, v * v


class Looper(QThread):
    complete = pyqtSignal(object)
    step = pyqtSignal(int)

    def __init__(self, points):
        super(Looper, self).__init__()
        self.points = points

    def run(self):
        for el in get_circle(self.points):
            if isinstance(el, int):
                self.step.emit(el)
            else:
                self.complete.emit(el)
                return
