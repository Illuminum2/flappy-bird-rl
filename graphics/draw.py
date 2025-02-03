import pygame as pg
import constants as config

class Draw:
    def __init__(self, window):
        self.window = window

    def draw(self, player, pipes):
        self.window.fill(config.BG_COLOR)

        pg.draw.rect(self.window, config.GROUND_COLOR, pg.Rect(0, config.GROUND_HEIGHT, config.WIDTH, config.HEIGHT - config.GROUND_HEIGHT))
        pg.draw.rect(self.window, config.BIRD_COLOR, player)

        for pipe in pipes:
            pg.draw.rect(self.window, config.PIPE_COLOR, pipe)


    def endscreen(self):
        self.window.fill(config.BG_COLOR)
        title_font = pg.font.Font(None, 40)
        title = title_font.render("Process ended, please reload page to restart.", True, config.TEXT_COLOR)
        window_rect = pg.display.get_surface().get_rect()
        title_rect = title.get_rect(center=window_rect.center)
        self.window.fill(config.BG_COLOR)
        self.window.blit(title, title_rect)