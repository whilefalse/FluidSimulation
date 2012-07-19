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
