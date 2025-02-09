import constants as config

class Pipe:
    def __init__(self, pipe1, pipe2):
        self.pipe1, self.pipe2 = pipe1, pipe2
        self.x = pipe1.x

    def update(self):
        self.pipe1.move_ip(-config.PIPE_SPEED, 0)
        self.pipe2.move_ip(-config.PIPE_SPEED, 0)
        self.x -= config.PIPE_SPEED

        if self.pipe1.x < 0-self.pipe1.width:
            return True
        return False