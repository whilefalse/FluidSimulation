class Lennard(object):
    @classmethod
    def potential(self, this, others):
        pot = 0
        for other in others:
            r = this.distance(other)
            if r == 0:
                r = 1
            pot += (4/r) * ((1/r)**(12) - (1/r)**(6))
        return pot

    @classmethod
    def force(self, this, others):
        fx_tot, fy_tot = 0, 0
        for other in others:
            r = this.distance(other)
            if r == 0:
                r = 1
            f = (24/r**2) * (2 * (1/r)**(12) - (1/r)**(6))

            fx = (other.x - this.x) * f
            fy = (other.y - this.y) * f

            fx_tot += fx
            fy_tot += fy

        fx_tot = 0
        fy_tot = 10
        return (fx_tot, fy_tot)
