from angem import Vector, Line, Circle


def get_circle(points):
    res_center = points[0]
    max_radius = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                center, radius = get_3points_center(points[i], points[j], points[k])
                if radius > max_radius:
                    max_radius = radius
                    res_center = center
    return Circle(res_center, max_radius)


def get_3points_center(p1, p2, p3):
    vector1 = Vector(p1, p2)
    vector2 = Vector(p2, p3)
    vector3 = Vector(p3, p1)

    if vector1 * vector2 >= 0:
        return p3 + vector3 / 2, abs(vector3) / 2
    if vector2 * vector3 >= 0:
        return p1 + vector1 / 2, abs(vector1) / 2
    if vector3 * vector1 >= 0:
        return p2 + vector2 / 2, abs(vector2) / 2

    line1 = Line(p1 + vector1 / 2, Vector(vector1.y, -vector1.x))
    line2 = Line(p2 + vector2 / 2, Vector(vector2.y, -vector2.x))
    point = line1.intersection(line2)
    return point, abs(Vector(point, p1))


def binary_search_method(function, a, b, eps):
    if function(a) * function(b) > 0:
        raise ValueError("На отрезке нат корня")
    x = (a + b) / 2
    while abs(function(x)) >= eps and abs(a - b) > eps:
        if function(a) * function(x) > 0:
            a = x
        else:
            b = x
        x = (a + b) / 2
    return x
