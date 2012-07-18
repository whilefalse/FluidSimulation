import unittest
from vector import Vector

class TestVector(unittest.TestCase):
    def test_sets_x_and_y(self):
        v = Vector(1, 5)
        assert v.x == 1.0
        assert v.y == 5.0

    def test_repr(self):
        v = Vector(1,5)
        assert str(v) == "(1.0, 5.0)"

    def test_lensquared(self):
        v = Vector(1,5)
        assert v.lensquared() == 26.0

    def test_len(self):
        v = Vector(3,4)
        assert v.len() == 5.0

    def test_distance_squared(self):
        v1 = Vector(1,1)
        v2 = Vector(4,2)
        assert v2.distancesquared(v1) == v1.distancesquared(v2) == 10.0

    def test_distance(self):
        v1 = Vector(1,1)
        v2 = Vector(4,5)
        assert v2.distance(v1) == v1.distance(v2) == 5.0

