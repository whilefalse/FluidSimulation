import random
import math
from vector import Vector as V

class Molecule(object):
    def __init__(self, r, v):
        self.r = r
        self.v = v
        self.a = V(0,0)

    def __repr__(self):
        return 'Molecule: %s -> %s' % (self.r, self.v)

    @classmethod
    def random_molecule(klass, max_x, max_y, scale):
        x = random.randint(0, max_x) * scale
        y = random.randint(0, max_y) * scale
        vx = random.randint(0, max_x/4) * random.choice([-1,1]) * scale
        vy = random.randint(0, max_y/4) * random.choice([-1,1]) * scale
        return klass(V(x, y), V(vx, vy))

    @classmethod
    def random_molecules(klass, n, max_x, max_y, scale):
        return [klass.random_molecule(max_x, max_y, scale) for i in range(n)]
