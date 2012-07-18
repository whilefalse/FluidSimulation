from vector import Vector as V

class Verlet(object):
    def __init__(self, force):
        self.force_model = force
        self.dt = 0.001

    def others(self, this, every):
        others = []
        for m in every:
            if m != this:
                others.append(m)
        return others

    def process_molecules(self, ms):
        self.print_energy(ms)

        for m in ms:
            self.update_position(m)

        old_as = []
        for m in ms:
            old_as.append(m.a)
            self.update_acceleration(m, self.others(m, ms))

        for i, m in enumerate(ms):
            self.update_velocity(m, old_as[i])

    def update_position(self, m):
        m.r.x = m.r.x + m.v.x*self.dt + (0.5)*m.a.x*(self.dt**2)
        m.r.y = m.r.y + m.v.y*self.dt + (0.5)*m.a.y*(self.dt**2)

    def update_acceleration(self, m, others):
        m.a = self.force_model.force(m, others)

    def update_velocity(self, m, original_a):
        m.v.x = m.v.x + (0.5)*(original_a.x + m.a.x)*self.dt
        m.v.y = m.v.y + (0.5)*(original_a.y + m.a.y)*self.dt

    def print_energy(self, ms):
        pe = 0
        ke = 0
        for m in ms:
            ke += m.kinetic_energy()
            pe += self.force_model.energy(m, self.others(m, ms))
        print "TOT ENERGY: %s, PE: %s, KE: %s" % (pe+ke, pe, ke)
