import random
import math

class Molecule(object):
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = 0
        self.ay = 0

    def __repr__(self):
        return 'Molecule: (%s, %s) -> %s' % (self.x, self.y, self.v)

    def distance(self, other):
        return math.sqrt(float(
                (self.x - other.x)**2 +
                (self.y - other.y)**2
                ))

    def energy(self):
        return 0.5 * (self.vx**2 + self.vy**2)

    @classmethod
    def random_molecule(klass, max_x, max_y):
        x = random.randint(100, max_x-100)
        y = random.randint(100, max_y-100)
        vx = random.randint(0, max_x/4) * random.choice([-1,1])
        vy = random.randint(0, max_y/4) * random.choice([-1,1])
        return klass(x, y, vx, vy)

    @classmethod
    def random_molecules(klass, n, max_x, max_y):
        return [klass.random_molecule(max_x, max_y) for i in range(n)]
