from vector import Vector as V
from config import config

force_model = config['simulation']['force_model']
module, klass = force_model.split('.')
force_model = getattr(__import__(module), klass)()
dt = config['simulation']['dt']

class Verlet(object):
    def __init__(self):
        self.kes = []
        self.pes = []

    def process_molecules(self, ms):
        self.print_energy(ms)

        for m in ms:
            self.update_position(m)

        old_as = []
        for m in ms:
            old_as.append(m.a)
            self.update_acceleration(m, ms)

        for i, m in enumerate(ms):
            self.update_velocity(m, old_as[i])

    def update_position(self, m):
        m.r.x = m.r.x + m.v.x*dt + (0.5)*m.a.x*(dt**2)
        m.r.y = m.r.y + m.v.y*dt + (0.5)*m.a.y*(dt**2)

    def update_acceleration(self, m, others):
        m.a = force_model.force(m, others)

    def update_velocity(self, m, original_a):
        m.v.x = m.v.x + (0.5)*(original_a.x + m.a.x)*dt
        m.v.y = m.v.y + (0.5)*(original_a.y + m.a.y)*dt

        if config['simulation']['boundary'] == 'wall':
            if m.r.x <= 0 and m.v.x <=0:
                m.v.x = - m.v.x
            if m.r.y <= 0 and m.v.y <=0:
                m.v.y = - m.v.y
            if m.r.x >= config['box']['width'] and m.v.x >= 0:
                m.v.x = - m.v.x
            if m.r.y >= config['box']['height'] and m.v.y >= 0:
                m.v.y = - m.v.y

    def print_energy(self, ms):
        pe = 0
        ke = 0
        for m in ms:
            ke += m.kinetic_energy()
            # Each pair gets counted twice, but we only care about the
            # mutual potential energy between each pair, so divide by 2
            pe += force_model.energy(m, ms)/2

        self.kes.append(ke)
        self.pes.append(pe)
