import Utils

class Player:

    def __init__(self):
        self.health = 100
        self.stamina = 100
        self.x_pos = -1
        self.y_pos = -1
        self.range = 10
        self.punch_cooldown = 0

    def take_damage(self, damage):
        self.health -= damage

    def move(self, direction):
        self.x_pos += Utils.vector_to_x_y(direction, self.stamina)[0]
        self.y_pos += Utils.vector_to_x_y(direction, self.stamina)[1]

    def punch(self, enemies):
        if self.punch_cooldown <= 0:
            self.punch_cooldown -= 1.2 - (self.stamina / 100)
            self.stamina -= 5
            for enemy in enemies:
                if self.range <= Utils.distance([self.x_pos, self.y_pos], [enemy.x_pos, enemy.y_pos]):
                    enemy.take_damage(100)