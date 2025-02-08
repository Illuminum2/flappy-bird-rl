import pygame as pg

import constants as config

class GroundManager:
    def __init__(self, window):
        self.window = window

        self.ground = pg.Rect(0, config.HEIGHT-config.GROUND_HEIGHT, config.WIDTH, config.GROUND_HEIGHT)

    def checkCollision(self, player):
        return player.y > config.HEIGHT-config.GROUND_HEIGHT
