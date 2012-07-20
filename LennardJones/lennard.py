from vector import Vector as V

class Lennard(object):
    def energy(self, this, others):
        utot = 0
        for other in others:
            if other == this:
                continue
            r_2 = this.r.distancesquared(other.r)
            r_6 = (1/r_2)**3
            r_12 = r_6**2

            u = 4 * (r_12 - r_6)
            assert u >= -1
            utot += u
        return utot

    def force(self, this, others):
        ftot = V(0, 0)
        for other in others:
            if other == this:
                continue
            r_2 = this.r.distancesquared(other.r)
            r_6 = (1/r_2)**3
            r_12 = r_6**2

            f = 24 * (2 * r_12 - r_6) / r_2

            ftot.x += (this.r.x - other.r.x) * f
            ftot.y += (this.r.y - other.r.y) * f
        return ftot
