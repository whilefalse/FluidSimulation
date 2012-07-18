import unittest
from verlet import Verlet
from molecule import Molecule
from vector import Vector as V

class VerletTest(unittest.TestCase):
    def test_others(self):
        v = Verlet(None)
        ms = [
                Molecule(V(1, 2), V(3,4)),
                Molecule(V(2, 3), V(4, 5)),
                Molecule(V(4, 5), V(6, 7))
             ]

        assert v.others(ms[0], ms) == [ms[1], ms[2]]
        assert v.others(ms[1], ms) == [ms[0], ms[2]]
        assert v.others(ms[2], ms) == [ms[0], ms[1]]
