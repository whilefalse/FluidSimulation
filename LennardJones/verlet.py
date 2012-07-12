from vector import Vector as V

class Verlet(object):
    @classmethod
    def new_r(self, m, h):
        return V(m.r.x + h*m.v.x + ((h**2)/2)*m.a.x,
                m.r.y + h*m.v.y + ((h**2)/2)*m.a.y)
    @classmethod
    def new_v(self, m, h, oldv, olda):
        return V(oldv.x + (h/2)*(m.a.x + olda.x),
                oldv.y + (h/2)*(m.a.y + olda.y))



