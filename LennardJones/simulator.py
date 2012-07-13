from Tkinter import *
from molecule import Molecule
from lennard import Lennard
from verlet import Verlet
from vector import Vector as V

class Simulator(object):
    def __init__(self, width, height, n, r):
        self.width = width
        self.height = height
        self.canvas_height = height
        self.canvas_width = width
        self.radius = r
        self.h = 1.0/1000
        self.scale = 1.0/500

        self.molecules = self.generate_molecules(n)
        self.setup_window()
        self.setup_timer()

    def do_movement(self):
        self.calc_forces()
        self.calc_energy()
        self.move_molecules()
        self.draw_molecules()
        self.setup_timer()

    def setup_timer(self):
        self.tk.after(1, self.do_movement)

    def setup_window(self):
        self.tk = Tk()
        self.canvas = Canvas(
                self.tk,
                width=self.canvas_width,
                height=self.canvas_height,
                )
        self.canvas.pack()

    def generate_molecules(self, n):
        return [Molecule(V(0*self.scale, 0*self.scale), V(0, 0)),
                # Molecule(V(500*self.scale, 0*self.scale), V(0,0)),
                # Molecule(V(0*self.scale, 500*self.scale), V(0,0)),
                Molecule(V(500*self.scale, 500*self.scale), V(0,0))]

        return Molecule.random_molecules(
                n,
                self.width,
                self.height,
                self.scale
                )

    def calc_energy(self):
        pe = 0
        ke = 0
        for m in self.molecules:
            others = []
            for n in self.molecules:
                if m != n:
                    others.append(n)
            pe += Lennard.energy(m, others)
            ke += 0.5 * m.v.lensquared()
        print "TOT: %s, PE: %s, KE: %s" % (pe+ke, pe, ke)

    def calc_forces(self):
        for m in self.molecules:
            others = []
            for n in self.molecules:
                if m != n:
                    others.append(n)
            m.force = Lennard.force(m, others)
            m.a = m.force

    def move_molecules(self):
        for m in self.molecules:
            new_r = Verlet.new_r(m, self.h)
            new_v = Verlet.new_v(m, self.h, m.v, m.a)
            m.r = new_r
            m.v = new_v

            # if m.r.x >= self.width or m.r.x <= 0:
            #     m.v.x = - m.v.x
            # if m.r.y >= self.height or m.r.y <= 0:
            #     m.v.y = - m.v.y

    def draw_molecules(self):
        self.canvas.delete(ALL)
        for molecule in self.molecules:
            self.canvas.create_oval(
                    molecule.r.x / self.scale - self.radius,
                    molecule.r.y / self.scale - self.radius,
                    molecule.r.x / self.scale + self.radius,
                    molecule.r.y / self.scale + self.radius,
                    fill = 'black'
                    )

if __name__ == '__main__':
    sim = Simulator(500, 500, 2, 2)
    mainloop()
