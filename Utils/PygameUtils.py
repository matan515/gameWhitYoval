import pygame as pg

class PygameUtils:
    keys = pg.key.get_pressed()
    old_keys = pg.key.get_pressed()

    @staticmethod
    def is_key_held(key):
        keys = pg.key.get_pressed()
        return keys[key]

    @staticmethod
    def is_key_pressed(key):

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == key:
                    return True
        return False

    @staticmethod
    def update():
        PygameUtils.old_keys = PygameUtils.keys
        PygameUtils.keys = pg.key.get_pressed()