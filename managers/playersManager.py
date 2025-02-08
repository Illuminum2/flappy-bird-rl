import pygame as pg

import constants as config
from entities.player import Player as P

class PlayersManager:
    def __init__(self, window):
        self.window = window

        self.players = []

    def spawnPlayer(self):
        self.players.append(P(pg.Rect(config.PLAYER_X, ((config.HEIGHT-config.GROUND_HEIGHT)/2)-(config.PLAYER_SIZE/2), config.PLAYER_SIZE, config.PLAYER_SIZE)))

    def updatePlayers(self):
        for player in self.players:
            player.update()
            if player.dead:
                self.players.remove(player)