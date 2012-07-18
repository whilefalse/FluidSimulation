from vector import Vector as V

class Lennard(object):
    def energy(self, this, others):
        utot = 0
        for other in others:
            r = this.r.distance(other.r)

            u = 4 * ((1/r)**(12) - (1/r)**(6))
            assert u >= -1
            utot += u
        return utot

    def force(self, this, others):
        ftot = V(0, 0)
        for other in others:
            r = this.r.distance(other.r)

            f = 24 * (2 * (1/r)**(12) - (1/r)**(6)) / (r*r)

            ftot.x += (this.r.x - other.r.x) * f
            ftot.y += (this.r.y - other.r.y) * f
        return ftot
