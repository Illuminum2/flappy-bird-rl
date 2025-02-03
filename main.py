import asyncio

import pygame as pg
import constants as config

from graphics import renderEngine as re

# initializing pygame and setting the screen resolution
pg.init()
window = pg.display.set_mode((config.WIDTH, config.HEIGHT))
pg.display.set_caption("Flappy bird RL")
clock = pg.time.Clock()

engine = re.RenderEngine(window, clock)

asyncio.run(engine.main())
