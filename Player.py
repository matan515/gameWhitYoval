import pygame
from Utils import PygameUtils as pgUtils
import Constants as Const
from Utils import Vector

class Player:

    def __init__(self):
        self.health = 100
        self.stamina = 100
        self.pos = Vector.Vector(Const.WINDOW_WIDTH / 3, Const.WINDOW_HEIGHT / 2)
        self.range = 10
        self.direction = Vector.Vector.from_polar(1, 0)
        self.punch_cooldown = 0 #in frames
        self.keys = pygame.key.get_pressed()

    def take_damage(self, damage=5):
        self.health -= damage

    def move(self, enemies):
        distance = self.stamina / 60
        print("Distance:", distance)
        print("position before:", self.pos)
        #movement = (D-A, S-W)
        movement = Vector.Vector(int(pgUtils.PygameUtils.is_key_held(pygame.K_d)) - int(pgUtils.PygameUtils.is_key_held(pygame.K_a)), int(pgUtils.PygameUtils.is_key_held(pygame.K_s)) - int(pgUtils.PygameUtils.is_key_held(pygame.K_w))).set_distance(distance)
        self.pos += movement

        print("position after:", self.pos)
        if pgUtils.PygameUtils.is_key_pressed(pygame.K_SPACE):
            self.punch(enemies)

    def punch(self, enemies):
        if self.punch_cooldown <= 0:
            self.punch_cooldown = 72 - ((Const.FPS * self.stamina) / 100) #
            self.stamina -= 20
            for enemy in enemies:
                if self.range <= self.pos.distance:
                    if abs(self.pos.angle - self.direction.angle) <= 45:
                        enemy.take_damage()

    def update(self, enemies):
        self.punch_cooldown -= 1
        self.stamina += 0.5
        self.move(enemies)