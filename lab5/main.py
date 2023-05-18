import time

import pygame as pg

from lab5.aircraft import AirCraft
from lab5.figures import Rect

pg.init()

FPS = 60


class Window:
    def __init__(self):
        self.step = 0
        self.screen = pg.display.set_mode((900, 600))
        self.aircraft = None
        self.rect_list = []
        self.restart()

    def restart(self):
        self.step = 0
        self.aircraft = AirCraft((700, -180))
        self.aircraft.rotate(0.2)
        self.aircraft.speed = (-2, 2)
        for i in range(8, -2, -1):
            self.rect_list.append(Rect(i * 100, 445, 60, 5))
            self.rect_list.append(Rect(i * 100, 485, 60, 5))

    def update(self):
        self.step += 1

        if self.step % 10 == 0:
            self.rect_list.append(Rect(-100, 445, 60, 5))
            self.rect_list.append(Rect(-100, 485, 60, 5))
            self.rect_list.pop(0)
            self.rect_list.pop(0)
        for rect in self.rect_list:
            rect.move(10, 0)

        self.aircraft.update_pos()
        if self.step == 220:
            self.aircraft.speed = (-3, 0)
        if 220 < self.step < 320:
            self.aircraft.rotate(-0.002)
        if self.step == 320:
            self.aircraft.acceleration = (0.03, 0)
        if self.step == 800:
            self.restart()

        self.draw()

    def draw(self):
        pg.draw.rect(self.screen, "#3ABED9", (0, 0, 900, 300))
        pg.draw.rect(self.screen, "#9DC43C", (0, 300, 900, 300))
        pg.draw.rect(self.screen, "#878787", (0, 430, 900, 80))
        for rect in self.rect_list:
            rect.draw(self.screen)
        self.aircraft.draw(self.screen)


def main():
    clock = pg.time.Clock()
    window = Window()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit(0)
        window.update()
        pg.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
