import Graphics.Graphics as Graphics
win = Graphics.Graphics()

print(win)
import EntityContainer
import pygame as pg
import time
import Constants as Const
from Utils import PygameUtils as pgUtils

game = EntityContainer.EntityContainer()
last_time = time.time()
run = True
while run:
    time.sleep(max(0.0, last_time - time.time() + 1/Const.FPS))
    last_time = time.time()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
    if game.is_enemies_dead():
        game.start_level()
        print("level up to: ", game.level)

    pgUtils.PygameUtils.update()
    game.update()
    win.update_window(game)