import constants as config
from constants import GRAVITY


class Player:
    def __init__(self, player):
        self.player = player
        self.y = player.y
        self.velocity = 0
        self.dead = False

    def update(self):
        self.velocity += config.GRAVITY

        self.player.move_ip(0, self.velocity)
        if self.player.y < 0: # Out of bounds check
            self.player.y = 0
            self.velocity = 0 # Makes player fall down faster, fix this later

    def jump(self):
        self.velocity = -config.JUMP_HEIGHT