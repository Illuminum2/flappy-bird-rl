import pygame as pg
from random import randint

import constants as config
from entities.pipe import Pipe as P

class PipeManager:
    def __init__(self, window):
        self.window = window

        self.pairs = []

    def appendPair(self, P):
        self.pairs.append(P)

    def removePair(self, pair):
        self.pairs.remove(pair)

    def generatePair(self):
        rand = randint(config.PIPE_MIN_HEIGHT, config.HEIGHT-config.GROUND_HEIGHT-config.PIPE_MIN_HEIGHT-config.PIPE_GAP)

        self.appendPair(P(pg.Rect(config.WIDTH + config.PIPE_WIDTH, 0, config.PIPE_WIDTH, rand), pg.Rect(config.WIDTH + config.PIPE_WIDTH, rand + config.PIPE_GAP, config.PIPE_WIDTH, config.HEIGHT-config.GROUND_HEIGHT-rand-config.PIPE_GAP)))

    def updatePipes(self):
        i = 0
        for pair in self.pairs:
            i += 1
            if pair.update():
                self.removePair(pair)
                self.generatePair()

    def checkCollision(self, player):
        for pair in self.pairs:
            if pair.pipe1.colliderect(player) or pair.pipe2.colliderect(player):
                return True
        return False
