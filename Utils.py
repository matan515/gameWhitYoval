import math

class Utils:

    @staticmethod
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    @staticmethod
    def vector_to_x_y(dis, dir):
        return dis * math.cos(dir), dis * math.sin(dir)

    @staticmethod
    def x_y_to_vector(x, y):
        return Utils.distance([x, 0], [0, y])