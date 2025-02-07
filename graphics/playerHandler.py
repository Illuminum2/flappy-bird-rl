import pygame as pg
import constants as config

class PlayerHandler:
    def __init__(self, window):
        self.window = window

        self.player = pg.Rect(config.PLAYER_X, ((config.HEIGHT-config.GROUND_HEIGHT)/2)-(config.PLAYER_SIZE/2), config.PLAYER_SIZE, config.PLAYER_SIZE)
        self.velocity = 0
        self.dead = False

    def update(self):
        self.velocity += 0.5
        self.move()

    def jump(self):
        self.velocity = -10
        self.move()

    def move(self):
        self.player.move_ip(0, self.velocity)