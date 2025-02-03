import asyncio
import sys

import pygame as pg
import constants as config

from graphics import draw
from graphics.pipeHandler import PipeHandler
from graphics.playerHandler import PlayerHandler

class RenderEngine:
    def __init__(self, window, clock):
        self.window = window
        self.clock = clock
        self.done = False

        self.player = PlayerHandler(self.window, pg.Rect(50, 50, 50, 50))
        self.pipes = PipeHandler(self.window)

        self.dw = draw.Draw(window)

    def checkKeys(self):
        key = pg.key.get_pressed()

        if key[pg.K_w]:
            self.player.jump()
        elif key[pg.K_SPACE]:
            self.player.jump()

        if key[pg.K_ESCAPE]:
            self.done = True

    def checkEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True


    async def main(self):
        while not self.done and not self.player.dead:
            self.checkKeys()
            self.checkEvents()

            self.player.update()
            self.pipes.pipesUpdate()

            self.done = True if self.pipes.checkCollision(self.player.player) else False # Collision detection

            self.dw.draw(self.player.player, self.pipes.pipes)
            pg.display.update()

            self.clock.tick(config.FPS)
            await asyncio.sleep(0)

        self.dw.endscreen()
        pg.display.update()

        pg.quit()
        sys.exit()