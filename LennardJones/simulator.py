from molecule import Molecule
from lennard import Lennard
from verlet import Verlet
from vector import Vector as V
from canvas import Canvas

class Simulator(object):
    def __init__(self):
        self.width = 3
        self.height = 3

        self.molecules = Molecule.random_molecules(100, self.width, self.height)

        self.canvas = Canvas(self.width, self.height)
        self.canvas.setup_timer(self.do_movement)

    def do_movement(self):
        self.move_molecules()
        self.canvas.refresh(self.molecules)

        # Set the timer to go again
        self.canvas.setup_timer(self.do_movement)

    def move_molecules(self):
        verlet = Verlet(force=Lennard())
        verlet.process_molecules(self.molecules)

if __name__ == '__main__':
    sim = Simulator()

    sim.canvas.start()
