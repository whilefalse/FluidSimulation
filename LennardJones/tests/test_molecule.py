import unittest
from molecule import Molecule
from vector import Vector as V

class TestMolecule(unittest.TestCase):
    def test_init_with_r_and_v(self):
        m = Molecule(V(1.0, 2.0), V(3.0, 4.0))

        assert m.r.x == 1.0
        assert m.r.y == 2.0

        assert m.v.x == 3.0
        assert m.v.y == 4.0

    def test_repr(self):
        m = Molecule(V(1,2), V(3,4))

        assert str(m) == "Molecule: (1.0, 2.0) -> (3.0, 4.0)"

    def test_random_molecule(self):
        m = Molecule.random_molecule(12, 16)

        assert m.__class__ == Molecule

        assert m.r.x <= 12
        assert m.r.y <= 16
        assert m.v.x <= 3
        assert m.v.y <= 4

    def test_random_molecules(self):
        ms = Molecule.random_molecules(100, 12, 16)

        assert len(ms) == 100
        for m in ms:
            assert m.__class__ == Molecule

            assert m.r.x <= 12
            assert m.r.y <= 16
            assert m.v.x <= 3
            assert m.v.y <= 4

    def test_kinetic_energy(self):
        m = Molecule(V(1.0, 1.0), V(3.0, 4.0))

        print m.kinetic_energy()
        assert m.kinetic_energy() == 12.5
