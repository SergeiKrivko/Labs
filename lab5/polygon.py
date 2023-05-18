from math import cos, sin


class Polygon:
    def __init__(self, points):
        self.points = list(points)

    def move(self, x, y):
        for i in range(len(self.points)):
            self.points[i] = (self.points[i][0] + x, self.points[i][1] + y)

    def rotate(self, point, angle):
        for i in range(len(self.points)):
            self.points[i] = ((self.points[i][0] - point[0]) * cos(angle) -
                              (self.points[i][1] - point[1]) * sin(angle) + point[0],
                              (self.points[i][0] - point[0]) * sin(angle) +
                              (self.points[i][1] - point[1]) * cos(angle) + point[1])
