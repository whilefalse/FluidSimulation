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

    def kinetic_energy(self):
        return 0.5*self.v.lensquared()

    @classmethod
    def random_molecule(klass, max_x, max_y):
        x = random.uniform(0, max_x)
        y = random.uniform(0, max_y)
        vx = random.uniform(0, max_x/4) * random.choice([-1,1])
        vy = random.uniform(0, max_y/4) * random.choice([-1,1])
        return klass(V(x, y), V(vx, vy))

    @classmethod
    def random_molecules(klass, n, max_x, max_y):
        return [
                klass(V(0.1,0.1), V(1,1)),
                klass(V(2.9,2.9), V(-1,-1))
                ]
        return [klass.random_molecule(max_x, max_y) for i in range(n)]
