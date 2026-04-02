import pygame
import Utils
import Constants as const

class Player:

    def __init__(self):
        self.health = 100
        self.stamina = 100
        self.x_pos = const.WINDOW_WIDTH / 3
        self.y_pos = const.WINDOW_HEIGHT / 2
        self.range = 10
        self.direction = 0
        self.punch_cooldown = 0 #in frames
        self.keys = pygame.key.get_pressed()

    def take_damage(self, damage=5):
        self.health -= damage

    def move(self, enemies):
        distance = self.stamina / 60
        print("Distance:", distance)
        print("position before:", self.x_pos, self.y_pos)

        # A or D buttons are pressed
        if Utils.Utils.is_key_held(pygame.K_a) != Utils.Utils.is_key_held(pygame.K_d) and (not Utils.Utils.is_key_held(pygame.K_s)) and (not Utils.Utils.is_key_held(pygame.K_w)):
            print("x change: " + str((int(Utils.Utils.is_key_held(pygame.K_d)) - int(Utils.Utils.is_key_held(pygame.K_a))) * distance))

            self.x_pos += (int(Utils.Utils.is_key_held(pygame.K_d)) - int(Utils.Utils.is_key_held(pygame.K_a))) * distance

        # S or W buttons are pressed
        elif Utils.Utils.is_key_held(pygame.K_s) != Utils.Utils.is_key_held(pygame.K_w) and (not Utils.Utils.is_key_held(pygame.K_a)) and (not Utils.Utils.is_key_held(pygame.K_a)):
            print("y change: " + str((int(Utils.Utils.is_key_held(pygame.K_s)) - int(Utils.Utils.is_key_held(pygame.K_w))) * distance))

            self.y_pos += (int(Utils.Utils.is_key_held(pygame.K_s)) - int(Utils.Utils.is_key_held(pygame.K_w))) * distance

        # Combinations between A/D and W/S
        elif Utils.Utils.is_key_held(pygame.K_a) != Utils.Utils.is_key_held(pygame.K_d) or Utils.Utils.is_key_held(pygame.K_s) != Utils.Utils.is_key_held(pygame.K_w):
            direction = Utils.Utils.angle([0, 0], [int(Utils.Utils.is_key_held(pygame.K_d)) - int(Utils.Utils.is_key_held(pygame.K_a)), int(Utils.Utils.is_key_held(pygame.K_s)) - int(Utils.Utils.is_key_held(pygame.K_w))])

            print("Direction:", direction)
            print("x change: " + str(Utils.Utils.vector_to_x_y(direction, distance)[0]))
            print("y change: " + str(Utils.Utils.vector_to_x_y(direction, distance)[1]))

            self.x_pos += Utils.Utils.vector_to_x_y(direction, distance)[0]
            self.y_pos += Utils.Utils.vector_to_x_y(direction, distance)[1]

        print("position after:", self.x_pos, self.y_pos)
        if Utils.Utils.is_key_pressed(pygame.K_SPACE):
            self.punch(enemies)

    def punch(self, enemies):
        if self.punch_cooldown <= 0:
            self.punch_cooldown += 72 - ((const.FPS * self.stamina) / 100) #
            self.stamina -= 20
            for enemy in enemies:
                if self.range <= Utils.Utils.distance([self.x_pos, self.y_pos], [enemy.x_pos, enemy.y_pos]):
                    if abs(Utils.Utils.angle([self.x_pos, self.y_pos], [enemy.x_pos, enemy.y_pos]) - self.direction) <= 45:
                        enemy.take_damage()

    def update(self, enemies):
        self.punch_cooldown -= 1
        self.stamina += 0.5
        self.move(enemies)