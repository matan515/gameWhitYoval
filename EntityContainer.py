import Player
import Enemy
import Utils
import pygame as pg

class EntityContainer:
    def __init__(self):
        self.player = Player.Player()
        self.level = 0

    def start_level(self):
        self.enemies = []
        for i in range(self.level):
            self.enemies.append(Enemy.Enemy())

    def set_level(self, level):
        self.level = level

    def update(self):
        self.player
        if Utils.is_key_pressed(pg.K_SPACE):
            self.player.punch(enemies)