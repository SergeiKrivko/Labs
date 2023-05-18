from math import cos, sin
import pygame as pg


class Polygon:
    def __init__(self, points, color):
        self.points = list(points)
        self.color = color

    def move(self, x, y):
        for i in range(len(self.points)):
            self.points[i] = (self.points[i][0] + x, self.points[i][1] + y)

    def rotate(self, point, angle):
        for i in range(len(self.points)):
            self.points[i] = ((self.points[i][0] - point[0]) * cos(angle) -
                              (self.points[i][1] - point[1]) * sin(angle) + point[0],
                              (self.points[i][0] - point[0]) * sin(angle) +
                              (self.points[i][1] - point[1]) * cos(angle) + point[1])

    def draw(self, screen):
        pg.draw.polygon(screen, self.color, self.points)


class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, screen):
        pg.draw.rect(screen, "#C0C0C0", (self.x, self.y, self.w, self.h))

    def move(self, x, y):
        self.x += x
        self.y += y


class Circle:
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color

    def move(self, x, y):
        self.center = (self.center[0] + x, self.center[1] + y)

    def rotate(self, point, angle):
        self.center = ((self.center[0] - point[0]) * cos(angle) -
                       (self.center[1] - point[1]) * sin(angle) + point[0],
                       (self.center[0] - point[0]) * sin(angle) +
                       (self.center[1] - point[1]) * cos(angle) + point[1])

    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.center, self.radius)


class Line:
    def __init__(self, p1, p2, color):
        self.p1 = p1
        self.p2 = p2
        self.color = color

    def move(self, x, y):
        self.p1 = (self.p1[0] + x, self.p1[1] + y)
        self.p2 = (self.p2[0] + x, self.p2[1] + y)

    def rotate(self, point, angle):
        self.p1 = ((self.p1[0] - point[0]) * cos(angle) -
                   (self.p1[1] - point[1]) * sin(angle) + point[0],
                   (self.p1[0] - point[0]) * sin(angle) +
                   (self.p1[1] - point[1]) * cos(angle) + point[1])
        self.p2 = ((self.p2[0] - point[0]) * cos(angle) -
                   (self.p2[1] - point[1]) * sin(angle) + point[0],
                   (self.p2[0] - point[0]) * sin(angle) +
                   (self.p2[1] - point[1]) * cos(angle) + point[1])

    def draw(self, screen):
        pg.draw.line(screen, self.color, self.p1, self.p2, 3)
