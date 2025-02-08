import constants as config

class Player:
    def __init__(self, player):
        self.player = player
        self.x, self.y = player.x , player.y
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