import pygame
import Utils.PygameUtils as pgUtils
import Constants as Const
import Utils.Vector as Vector

class Player:

    def punch(self, enemies):
        print("PUNCHING")
        if self.punch_cooldown <= 0 and self.stamina:
            self.punch_cooldown = 72 - ((Const.FPS * self.stamina) / 100)
            self.stamina -= 20
            for enemy in enemies:
                if (enemy.pos - self.pos).distance <= self.range and abs((enemy.pos - self.pos).angle) <= self.range_angle:
                    enemy.take_damage()

    def __init__(self):
        self.health = 100
        self.stamina = 100
        self.max_health = 100
        self.max_stamina = 100
        self.pos = Vector.Vector(Const.WINDOW_WIDTH / 3, Const.WINDOW_HEIGHT / 2)
        self.range = 10
        self.range_angle = 45
        self.direction = Vector.Vector.from_polar(1, 0)
        self.punch_cooldown = 0 #in frames
        self.keys = pygame.key.get_pressed()

    def take_damage(self, damage=5):
        self.health -= damage

    def move(self, enemies):
        distance = self.stamina / 60
        #movement = (D-A, S-W)
        movement = Vector.Vector(int(pgUtils.PygameUtils.is_key_held(pygame.K_d)) - int(pgUtils.PygameUtils.is_key_held(pygame.K_a)), int(pgUtils.PygameUtils.is_key_held(pygame.K_s)) - int(pgUtils.PygameUtils.is_key_held(pygame.K_w)))
        if bool(movement):
            movement.set_distance(distance)
            self.pos += movement
        print(pgUtils.PygameUtils.is_key_pressed(pygame.K_SPACE))
        if pgUtils.PygameUtils.is_key_pressed(pygame.K_SPACE):
            self.punch(enemies)

    def update(self, enemies):
        self.punch_cooldown -= 1
        self.stamina += 0.5
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina
            self.health = min(self.health + 0.1, self.max_health)
        self.move(enemies)
        print(self.pos, self.health, self.stamina)