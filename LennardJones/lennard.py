class Lennard(object):
    @classmethod
    def force(self, this, others):
        fx_tot, fy_tot = 0, 0
        for other in others:
            r = this.distance(other)
            if r == 0:
                r = 0.001
            f = 24 * (2 * (1/r)**(13) - (1/r)**(7))

            fx = (this.x - other.x) * f
            fy = (this.y - other.y) * f

            fx_tot += fx
            fy_tot += fy
        return (fx_tot, fy_tot)
