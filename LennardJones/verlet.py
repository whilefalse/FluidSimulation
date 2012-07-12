class Verlet(object):
    @classmethod
    def new_r(self, m, h):
        return (m.x + h*m.vx + ((h**2)/2)*m.ax,
                m.y + h*m.vy + ((h**2)/2)*m.ay)
    @classmethod
    def new_v(self, m, h, oldv, olda):
        return (oldv[0] + (h/2)*(m.ax + olda[0]),
                oldv[1] + (h/2)*(m.ay + olda[1]))



