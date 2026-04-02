import Utils
import Player
import random

class Enemy(Player.Player):

    def __init__(self):
        self.health = 100
        self.x_pos = 500
        self.y_pos = random.randint(50, 250)
        self.range = 10

    def take_damage(self, damage=100):
        self.health -= damage

    def punch(self, player):
        if self.punch_cooldown <= 0:
            self.punch_cooldown += 120
            player.take_damage()

    def update(self, player):
        self.punch_cooldown -= 1
        if Utils.Utils.distance([self.x_pos, self.y_pos], [player.x_pos, player.y_pos]) < self.range:
            self.move(Utils.Utils.angle([self.x_pos, self.y_pos], [player.x_pos, player.y_pos]), Utils.Utils.distance([self.x_pos, self.y_pos], [player.x_pos, player.y_pos]))
            self.punch(player)
        else:
            self.move(Utils.Utils.angle([self.x_pos, self.y_pos], [player.x_pos, player.y_pos]), self.range)