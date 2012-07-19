from config import config
from molecule import Molecule
from vector import Vector as V

molecules = config['molecules']

class MoleculeGenerator(object):
    @classmethod
    def generate(self):
        generated = []
        if molecules.__class__ == list:
            for m in molecules:
                generated.append(Molecule(V(*m['r']), V(*m['v'])))

        return generated
