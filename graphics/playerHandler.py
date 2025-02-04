import constants as config

class PlayerHandler:
    def __init__(self, window, player, ground):
        self.window = window
        self.player = player
        self.ground = ground
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
        if self.player.colliderect(self.ground):
            self.player.y = config.HEIGHT - config.GROUND_HEIGHT
            self.velocity = 0
            self.dead = True
        elif self.player.y <= 0:
            self.player.y = 1  # Set to slightly below the top limit
            self.velocity = 0