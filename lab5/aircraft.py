import pygame as pg

from lab5.polygon import Polygon


class AirCraft:
    def __init__(self, pos):
        self.pos = pos

        self.fuselage_polygon = Polygon([(10, 168), (12, 164), (36, 151), (47, 142), (55, 139), (156, 138), (214, 145),
                                         (471, 145), (475, 148), (477, 152), (474, 158), (470, 161), (340, 188),
                                         (305, 191), (101, 191), (66, 189), (39, 184), (22, 178), (12, 172)])
        self.back_polygon = Polygon([(371, 145), (386, 142), (463, 78), (490, 78), (462, 145)])
        self.wind_polygon = Polygon([(147, 178), (161, 175), (218, 171), (283, 166), (335, 163), (358, 152), (368, 152),
                                     (358, 163), (341, 166), (328, 167), (306, 170), (285, 179), (265, 185), (246, 187),
                                     (220, 188), (191, 188), (163, 187), (149, 184)])
        self.speed = (0, 0)
        self.acceleration = (0, 0)
        self.move(*self.pos)

    def draw(self, screen):
        pg.draw.polygon(screen, (255, 255, 255), self.fuselage_polygon.points)
        pg.draw.polygon(screen, (21, 119, 184), self.back_polygon.points)
        pg.draw.polygon(screen, (180, 180, 180), self.wind_polygon.points)

    def move(self, x, y):
        self.fuselage_polygon.move(x, y)
        self.back_polygon.move(x, y)
        self.wind_polygon.move(x, y)

    def update_pos(self):
        self.move(*self.speed)
        self.speed = (self.speed[0] + self.acceleration[0], self.speed[1] + self.acceleration[1])

    def rotate(self, alpha):
        point = (self.pos[0] + 223, self.pos[1] + 208)
        self.fuselage_polygon.rotate(point, alpha)
        self.back_polygon.rotate(point, alpha)
        self.wind_polygon.rotate(point, alpha)
