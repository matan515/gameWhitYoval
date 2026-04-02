import Player
import random
from Utils import Vector


class Enemy(Player.Player):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.pos = Vector.Vector(500, random.randint(50, 250))
        self.range = 10

    def take_damage(self, damage=100):
        self.health -= damage

    def punch(self, player):
        if self.punch_cooldown <= 0:
            self.punch_cooldown += 120
            player.take_damage()

    def update(self, player):
        self.punch_cooldown -= 1
        self.pos += (player.pos - self.pos).set_distance(min(self.range, (player.pos - self.pos).distance))

        if player.pos - self.pos < self.range:
            self.punch(player)