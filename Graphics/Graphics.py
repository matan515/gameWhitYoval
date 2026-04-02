import pygame as pg
import Constants as Const

class Graphics:
    def __init__(self):
        self.win = pg.display.set_mode((Const.WINDOW_WIDTH, Const.WINDOW_HEIGHT))
        pg.display.set_caption("You VS x kids")

    def update_window(self, game):
        self.win.fill((4, 233, 195))

        # need to change for images
        pg.draw.rect(self.win, (0, 0, 255), pg.Rect(game.player.x_pos, game.player.y_pos, 10, 20))
        for enemy in game.enemies:
            pg.draw.rect(self.win, (255, 0, 0), pg.Rect(enemy.x_pos, enemy.y_pos, 10, 20))

        pg.display.update()