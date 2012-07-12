from Tkinter import *
from molecule import Molecule
from lennard import Lennard
from verlet import Verlet

class Simulator(object):
    def __init__(self, width, height, n, r):
        self.width = width
        self.height = height
        self.canvas_height = height + 100
        self.canvas_width = width + 100
        self.radius = r
        self.molecules = self.generate_molecules(n)
        self.setup_window()
        self.setup_timer()
        self.h = 0.01

    def do_movement(self):
        self.calc_forces()
        self.move_molecules()
        self.draw_molecules()
        self.setup_timer()

    def setup_timer(self):
        self.tk.after(5, self.do_movement)

    def setup_window(self):
        self.tk = Tk()
        self.canvas = Canvas(
                self.tk,
                width=self.canvas_width,
                height=self.canvas_height,
                )
        self.canvas.pack()

    def generate_molecules(self, n):
        return [
                Molecule(10,10,0,0),
                Molecule(20, 10, 0, 0)
                ]
        return Molecule.random_molecules(
                n,
                self.width,
                self.height
                )

    def calc_forces(self):
        for m in self.molecules:
            others = []
            for n in self.molecules:
                if m != n:
                    others.append(n)
            m.force = Lennard.force(m, others)
            m.ax = m.force[0]
            m.ay = m.force[1]

    def move_molecules(self):
        for m in self.molecules:
            new_r = Verlet.new_r(m, self.h)
            new_v = Verlet.new_v(m, self.h, (m.vx, m.vy), (m.ax, m.ay))
            m.x, m.y = new_r
            m.vx, m.vy = new_v

            if m.x > self.width:
                m.x = self.width
                m.vx = - m.vx
                m.ax = 0
            if m.x < 0:
                m.x = 0
                m.vx = - m.vx
                m.ax = 0
            if m.y > self.height:
                m.y = self.height
                m.vy = - m.vy
                m.ay = 0
            if m.y < 0:
                m.y = 0
                m.vy = - m.vy
                m.ay = 0

    def draw_molecules(self):
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(0, 0, self.width, self.height)
        for molecule in self.molecules:
            self.canvas.create_oval(
                    molecule.x - self.radius,
                    molecule.y - self.radius,
                    molecule.x + self.radius,
                    molecule.y + self.radius,
                    fill = 'black'
                    )

if __name__ == '__main__':
    sim = Simulator(500, 500, 2, 2)
    # print sim.molecules
    mainloop()
