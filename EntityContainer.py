import pygame as pg
from pygame.display import update

import Graphics.Graphics
import Player
import Enemy
import Utils

class EntityContainer:
    def __init__(self):
        self.player = Player.Player()
        self.level = 1
        self.enemies = []
        self.win = Graphics.Graphics.Graphics()

    def start_level(self):
        self.enemies = []
        for i in range(self.level):
            self.enemies.append(Enemy.Enemy())

    def set_level(self, level):
        self.level = level

    def update(self):
        Utils.Utils.update_keys()
        self.player.update()
        if Utils.Utils.is_key_pressed(pg.K_SPACE):
            self.player.punch(self.enemies)

        for enemy in self.enemies:
            if enemy.health <= 0:
                self.enemies.remove(self.enemies.index(enemy))

        self.win.update_window(self.player, self.enemies)

    def is_enemies_dead(self):
        if len(self.enemies) == 0:
            return True
        return False