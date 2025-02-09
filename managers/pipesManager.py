import pygame as pg
from random import randint

import constants as config
from entities.pipe import Pipe as P

class PipeManager:
    def __init__(self, window):
        self.window = window

        self.pairs = []
        self.collisionCheckSkip = 0

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
        if self.collisionCheckSkip > 0:
            self.collisionCheckSkip -= 1
            return False

        playerRect = pg.Rect(config.PLAYER_X, player.y, config.PLAYER_SIZE, config.PLAYER_SIZE)
        playerRightEdge = config.PLAYER_X + config.PLAYER_SIZE / 2

        for i, pair in enumerate(self.pairs):
            pairLeftEdge = pair.x - config.PIPE_WIDTH / 2
            if pairLeftEdge < playerRightEdge:
                if pair.pipe1.colliderect(playerRect) or pair.pipe2.colliderect(playerRect):
                    return True
            elif i == 0: # == instead of is, because == is used for value comparison
                self.collisionCheckSkip = int((pairLeftEdge - playerRightEdge) / config.PIPE_SPEED)
        return False
