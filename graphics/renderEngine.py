import sys
import asyncio
import pygame as pg

import constants as config
from graphics import draw
from managers.groundManager import GroundManager
from managers.pipesManager import PipeManager
from managers.playersManager import PlayersManager

class RenderEngine:
    def __init__(self, window, clock):
        self.window = window

        self.clock = clock
        self.done = False

        self.ground = GroundManager(self.window)
        self.players = PlayersManager(self.window)
        self.pipePairs = PipeManager(self.window)

        self.dw = draw.Draw(window, self.ground)

    def checkKeys(self):
        key = pg.key.get_pressed()

        if key[pg.K_w] or key[pg.K_SPACE] or key[pg.K_UP]:
            self.players.players[0].jump()

        if key[pg.K_ESCAPE]:
            self.done = True

    def checkEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True


    async def main(self):
        self.pipePairs.generatePair()
        self.players.spawnPlayer()
        while not self.done:
            self.done = True if self.pipePairs.checkCollision(self.players.players[0].player) or self.ground.checkCollision(self.players.players[0].player) else False  # Collision detection, must be done before checking keys

            self.checkKeys()
            self.checkEvents()

            self.players.players[0].update()
            self.pipePairs.updatePipes()

            self.dw.draw(self.players.players[0].player, self.pipePairs.pairs, self.ground.ground)
            pg.display.update()

            self.clock.tick(config.FPS)
            await asyncio.sleep(0)
        self.dw.endscreen()
        pg.display.update()

        pg.quit()
        sys.exit()