#import pygame as pg

from graphics.pipe import Pipe as P

class PipeHandler:
    def __init__(self, window):
        self.window = window
        self.pipes = []

    def addPipe(self, x, y, width, height):
        self.pipes.append(P(x, y, width, height))

    def removePipe(self, pipe):
        self.pipes.remove(pipe)

    def pipesUpdate(self):
        for pipe in self.pipes:
            pipe.update()

    def checkCollision(self, player):
        for pipe in self.pipes:
            if pipe.pipe.colliderect(player):
                return True
        return False
