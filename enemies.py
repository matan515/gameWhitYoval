import Utils
import pygame as pg
import math
import random

class enemies:

    def __init__(self):
        self.health = 100
        self.stamina = 100
        self.x_pos = random.randint(0, 800)
        self.y_pos = random.randint(0, 600)
        self.range = 10
        self.punch_cooldown = 0 #in frames
        self.player_x=x
        self.player_y=y

    def take_damage(self, damage=100):
        self.health -= damage

    def move(self):
        direction = math.sqrt((self.player_x - self.x_pos) ** 2 + (self.player_y - self.y_pos) ** 2)
        self.x_pos += Utils.vector_to_x_y(direction, self.stamina)[0]
        self.y_pos += Utils.vector_to_x_y(direction, self.stamina)[1]

    def punch(self, plyer):
        if self.punch_cooldown <= 0:
            self.punch_cooldown += 72 - (self.stamina / 100)
            self.stamina -= 20
            for plyer in plyer:
                if self.range <= Utils.distance([self.x_pos, self.y_pos], [plyer.x_pos, plyer.y_pos]):
                    plyer.take_damage()

    def update(self):
        self.punch_cooldown -= 1
        self.stamina += 1