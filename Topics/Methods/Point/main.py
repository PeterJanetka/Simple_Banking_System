import math


class Point:
    points_list = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.points_list.append(self)

    def dist(self, Point):
        return math.sqrt(int(self.x - Point.x) ** 2 + (self.y - Point.y) ** 2)
