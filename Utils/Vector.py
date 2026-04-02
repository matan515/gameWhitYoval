import math

class Vector:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.distance = math.sqrt(x_pos**2 + y_pos**2)
        self.angle = math.atan2(y_pos, x_pos)

    @classmethod
    def from_polar(cls, distance, angle):
        x = distance * math.cos(angle)
        y = distance * math.sin(angle)
        return cls(x, y)

    def __add__(self, other):
        return Vector(self.x_pos + other.x_pos, self.y_pos + other.y_pos)

    def __sub__(self, other):
        return Vector(self.x_pos - other.x_pos, self.y_pos - other.y_pos)

    def rotate(self, angle):
        self.angle += angle
        self.x_pos += self.distance * math.cos(angle)
        self.y_pos += self.distance * math.sin(angle)