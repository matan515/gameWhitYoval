import pygame as pg

class Graphics:
    def __init__(self):
        self.win = pg.display.set_mode((700, 300))
        pg.display.set_caption("You VS x")

    def update_window(self, player, enemies):
        self.win.fill((4, 233, 195))

        # need to change for images
        pg.draw.rect(self.win, (0, 0, 255), pg.Rect(player.x_pos, player.y_pos, 10, 20))
        for enemy in enemies:
            pg.draw.rect(self.win, (255, 0, 255), pg.Rect(enemy.x_pos, enemy.y_pos, 10, 20))

        pg.display.update()