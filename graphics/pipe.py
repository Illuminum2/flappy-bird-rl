import pygame as pg


class Pipe:
    def __init__(self, x, y, width, height):
        self.pipe = pg.Rect(x, y, width, height)
        self.x, self.y = x, y

    def update(self, x):
        self.x -= x
        self.pipe.move_ip(x, self.y)