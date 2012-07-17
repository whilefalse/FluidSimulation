import math

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(%s, %s)" % (self.x, self.y)

    def len(self):
        return math.sqrt(self.lensquared())

    def lensquared(self):
        return self.x*self.x + self.y*self.y

    def distance(self, other):
        return math.sqrt(self.distancesquared(other))

    def distancesquared(self, other):
        dx = (self.x - other.x)
        dy = (self.y - other.y)
        return dx*dx + dy*dy


