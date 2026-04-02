import math

import pygame
import pygame as pg

class Utils:
    keys = pg.key.get_pressed()
    old_keys = pg.key.get_pressed()

    @staticmethod
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    @staticmethod
    def angle(p1, p2):
        return math.degrees(math.atan2(p1[1] - p2[1], p1[0] - p2[0]))

    @staticmethod
    def vector_to_x_y(dis, dir):
        return dis * math.cos(dir), dis * math.sin(dir)

    @staticmethod
    def x_y_to_vector(x, y):
        #distence, direction
        return [Utils.distance([x, 0], [0, y]), Utils.angle([x, 0], [0, y])]

    @staticmethod
    def is_key_held(key):
        keys = pygame.key.get_pressed()
        return keys[key]

    @staticmethod
    def is_key_pressed(key):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == key:
                    return True
        return False

    @staticmethod
    def update_keys():
        Utils.old_keys = Utils.keys
        Utils.keys = pg.key.get_pressed()

