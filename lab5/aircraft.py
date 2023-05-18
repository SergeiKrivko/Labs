import pygame as pg

from lab5.figures import Polygon, Circle, Line


class AirCraft:
    def __init__(self, pos):
        self.pos = pos

        self.fuselage_polygon = Polygon([(10, 168), (12, 164), (36, 151), (47, 142), (55, 139), (156, 138), (214, 145),
                                         (471, 145), (475, 148), (477, 152), (474, 158), (470, 161), (340, 188),
                                         (305, 191), (101, 191), (66, 189), (39, 184), (22, 178), (12, 172)], "#E0E0E0")
        self.back_polygon = Polygon([(371, 145), (386, 142), (463, 78), (490, 78), (462, 145)], "#1577B8")
        self.wind_polygon = Polygon([(147, 178), (161, 175), (218, 171), (283, 166), (335, 163), (358, 152), (368, 152),
                                     (358, 163), (341, 166), (328, 167), (306, 170), (285, 179), (265, 185), (246, 187),
                                     (220, 188), (191, 188), (163, 187), (149, 184)], "#B4B4B4")
        self.cabin_polygon = Polygon([(44, 145), (54, 145), (54, 149), (40, 149)], "#5D6880")
        self.engine1 = Engine()
        self.engine2 = Engine((64, -7))

        self.wheel1 = Circle((58, 204), 6, "#202020")
        self.wheel1_line = Line((58, 188), (58, 204), "#606060")

        self.wheel2 = Circle((225, 204), 6, "#202020")
        self.wheel3 = Circle((240, 204), 6, "#202020")
        self.wheel4 = Circle((255, 204), 6, "#202020")
        self.wheel5 = Circle((270, 204), 6, "#202020")

        self.wheel_line2 = Line((232, 190), (232, 204), "#606060")
        self.wheel_line3 = Line((262, 190), (262, 204), "#606060")

        self.rotation_point = (250, 204)

        self.speed = (0, 0)
        self.acceleration = (0, 0)
        self.move(*self.pos)


    def draw(self, screen):
        self.fuselage_polygon.draw(screen)
        self.back_polygon.draw(screen)
        self.wind_polygon.draw(screen)
        self.cabin_polygon.draw(screen)
        self.engine1.draw(screen)
        self.engine2.draw(screen)

        self.wheel1_line.draw(screen)
        self.wheel_line2.draw(screen)
        self.wheel_line3.draw(screen)

        self.wheel1.draw(screen)
        self.wheel2.draw(screen)
        self.wheel3.draw(screen)
        self.wheel4.draw(screen)
        self.wheel5.draw(screen)

    def move(self, x, y):
        self.fuselage_polygon.move(x, y)
        self.back_polygon.move(x, y)
        self.wind_polygon.move(x, y)
        self.cabin_polygon.move(x, y)
        self.engine1.move(x, y)
        self.engine2.move(x, y)

        self.wheel1.move(x, y)
        self.wheel2.move(x, y)
        self.wheel3.move(x, y)
        self.wheel4.move(x, y)
        self.wheel5.move(x, y)
        self.wheel1_line.move(x, y)
        self.wheel_line2.move(x, y)
        self.wheel_line3.move(x, y)

        self.rotation_point = (self.rotation_point[0] + x, self.rotation_point[1] + y)

    def update_pos(self):
        self.move(*self.speed)
        self.speed = (self.speed[0] + self.acceleration[0], self.speed[1] + self.acceleration[1])

    def rotate(self, alpha):
        point = self.rotation_point
        self.fuselage_polygon.rotate(point, alpha)
        self.back_polygon.rotate(point, alpha)
        self.wind_polygon.rotate(point, alpha)
        self.cabin_polygon.rotate(point, alpha)
        self.engine1.rotate(point, alpha)
        self.engine2.rotate(point, alpha)

        self.wheel1.rotate(point, alpha)
        self.wheel2.rotate(point, alpha)
        self.wheel3.rotate(point, alpha)
        self.wheel4.rotate(point, alpha)
        self.wheel5.rotate(point, alpha)
        self.wheel1_line.rotate(point, alpha)
        self.wheel_line2.rotate(point, alpha)
        self.wheel_line3.rotate(point, alpha)


class Engine:
    def __init__(self, pos=(0, 0)):
        self.polygon1 = Polygon([(167, 184), (171, 182), (193, 182), (196, 184), (196, 198), (194, 200), (171, 200),
                                 (168, 199)], "#D0D0D0")
        self.polygon2 = Polygon([(196, 185), (205, 187), (214, 189), (215, 195), (206, 196), (197, 198)], "#8C8C8C")
        self.polygon1.move(*pos)
        self.polygon2.move(*pos)

    def move(self, x, y):
        self.polygon1.move(x, y)
        self.polygon2.move(x, y)

    def rotate(self, point, angle):
        self.polygon1.rotate(point, angle)
        self.polygon2.rotate(point, angle)

    def draw(self, screen):
        self.polygon1.draw(screen)
        self.polygon2.draw(screen)
