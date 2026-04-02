from pygame.examples.eventlist import last_key

import Graphics.Graphics as Graphics
win = Graphics.Graphics()

print(win)
import EntityContainer
import pygame
import Utils
import time

game = EntityContainer.EntityContainer()
last_time = time.time()
run = True
while run:
    time.sleep(max(0, last_time - time.time() + 1/60))
    last_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    if game.is_enemies_dead():
        game.start_level()
        print("level up to: ", game.level)
    game.update()
    win.update_window(game.player, game.enemies)