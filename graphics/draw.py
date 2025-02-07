import pygame as pg
import constants as config


class Draw:
    def __init__(self, window, ground):
        self.window = window
        self.ground = ground

    def draw(self, player, pipePairs):
        self.window.fill(config.BG_COLOR)

        pg.draw.rect(self.window, config.GROUND_COLOR, self.ground)  # Draw ground
        pg.draw.rect(self.window, config.PLAYER_COLOR, player) # Draw player

        #print("Drawing pipes:")
        for pair in pipePairs:
            #print("Drawing pipe: " + str(pair.pipe1))
            pg.draw.rect(self.window, config.PIPE_COLOR, pair.pipe1)
            pg.draw.rect(self.window, config.PIPE_COLOR, pair.pipe2)

    def endscreen(self):
        self.window.fill(config.BG_COLOR)
        title_font = pg.font.Font(None, 40)
        title = title_font.render("Process ended, please reload page to restart.", True, config.TEXT_COLOR)
        window_rect = pg.display.get_surface().get_rect()
        title_rect = title.get_rect(center=window_rect.center)
        self.window.fill(config.BG_COLOR)
        self.window.blit(title, title_rect)