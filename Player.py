import Utils
import pygame as pg

class Player:

    def __init__(self):
        self.health = 100
        self.stamina = 100
        self.x_pos = 200
        self.y_pos = 150
        self.range = 10
        self.punch_cooldown = 0 #in frames

    def take_damage(self, damage=5):
        self.health -= damage

    def move(self):
        # Player controls vector(d - a, s - w)
        direction = Utils.x_y_to_vector(int(Utils.is_key_pressed(pg.K_d)) - int(Utils.is_key_pressed(pg.K_a)), int(Utils.is_key_pressed(pg.K_s)) - int(Utils.is_key_pressed(pg.K_w)))
        self.x_pos += Utils.vector_to_x_y(direction, self.stamina)[0]
        self.y_pos += Utils.vector_to_x_y(direction, self.stamina)[1]

    def punch(self, enemies):
        if self.punch_cooldown <= 0:
            self.punch_cooldown += 72 - (self.stamina / 100)
            self.stamina -= 20
            for enemy in enemies:
                if self.range <= Utils.distance([self.x_pos, self.y_pos], [enemy.x_pos, enemy.y_pos]):
                    enemy.take_damage()

    def update(self):
        self.punch_cooldown -= 1
        self.stamina += 1