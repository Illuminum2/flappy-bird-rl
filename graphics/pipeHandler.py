from random import randint

import pygame as pg
import random
import constants as config
from constants import PIPE_GAP, PIPE_MIN_HEIGHT

from graphics.pipe import Pipe as P

class PipeHandler:
    def __init__(self, window):
        self.window = window
        self.pairs = []

    def appendPair(self, P):
        print("Append pipe")
        self.pairs.append(P)

    def removePair(self, pair):
        self.pairs.remove(pair)

    def generatePair(self):
        max_pipe_height = config.HEIGHT - config.GROUND_HEIGHT - config.PIPE_GAP - config.PIPE_MIN_HEIGHT
        rand = random.randint(config.PIPE_MIN_HEIGHT, max_pipe_height)
        #print("Pipe generator: " + str(config.WIDTH+config.PIPE_WIDTH))
        self.appendPair(P(pg.Rect(config.WIDTH+config.PIPE_WIDTH, 0, config.PIPE_WIDTH, rand+PIPE_MIN_HEIGHT), pg.Rect(config.WIDTH+config.PIPE_WIDTH, rand+config.PIPE_GAP, config.PIPE_WIDTH, (config.HEIGHT-config.GROUND_HEIGHT)-(rand+config.PIPE_GAP))))
        #self.appendPipe(config.WIDTH+config.PIPE_WIDTH, 0, config.PIPE_WIDTH, 200)
        #self.appendPipe(config.WIDTH+config.PIPE_WIDTH, config.HEIGHT-200, config.PIPE_WIDTH, 200)

    def updatePipes(self):
        i = 0
        for pair in self.pairs:
            i += 1
            if pair.update():
                self.removePair(pair)
                self.generatePair()
                print("Pipe removed")

    def checkCollision(self, player):
        for pair in self.pairs:
            if pair.pipe1.colliderect(player) or pair.pipe2.colliderect(player):
                return True
        return False
