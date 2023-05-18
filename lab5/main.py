import pygame as pg

from lab5.aircraft import AirCraft

pg.init()

FPS = 60


class Window:
    def __init__(self):
        self.step = 0
        self.screen = pg.display.set_mode((900, 600))
        self.aircraft = None
        self.restart()

    def restart(self):
        self.step = 0
        self.aircraft = AirCraft((500, -80))
        self.aircraft.rotate(0.2)
        self.aircraft.speed = (-3, 2)

    def update(self):
        self.step += 1
        self.aircraft.update_pos()
        if self.step == 120:
            self.aircraft.speed = (-4, 0)
            self.aircraft.acceleration = (0.02, 0)
        if 120 < self.step < 220:
            self.aircraft.rotate(-0.002)
        if self.step == 600:
            self.restart()
        self.draw()

    def draw(self):
        self.screen.fill((0, 0, 0))
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
