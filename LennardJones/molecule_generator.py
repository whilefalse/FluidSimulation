from config import config
from molecule import Molecule
from vector import Vector as V

molecules = config['molecules']

class MoleculeGenerator(object):
    @classmethod
    def generate(self):
        if type(molecules) == list:
            return self.generate_list()
        else:
            return getattr(self, 'generate_%s' % molecules)(**config['molecules_args'])
        return generated

    @classmethod
    def generate_list(self):
        return reduce(lambda acc, m: acc + [Molecule(V(*m['r']), V(*m['v']))], molecules, [])

    @classmethod
    def generate_grid(self, x_num, y_num, y_scale):
        ms = []
        xstep = float(config['box']['height'])/x_num

        for y in range(y_num+1):
            for x in range(x_num+1):
                ms.append(Molecule(V(x*xstep,config['box']['height'] - xstep*y*y_scale),V(0,0)))

        return ms
