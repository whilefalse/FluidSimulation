from verlet import Verlet
from canvas import Canvas
from config import config
from molecule_generator import MoleculeGenerator
from plotter import Plotter

max_steps = config['simulation']['max_steps']

class Simulator(object):
    def __init__(self):
        self.current_step = 0
        self.molecules = MoleculeGenerator.generate()
        print self.molecules
        self.canvas = Canvas()
        self.canvas.setup_timer(self.do_movement)
        self.verlet = Verlet()

    def do_movement(self):
        self.current_step += 1
        self.move_molecules()
        self.canvas.refresh(self.molecules)

        # Set the timer to go again
        if self.current_step < max_steps:
            if self.current_step % 500 == 0:
                print "step %s/%s" % (self.current_step, max_steps)
            self.canvas.setup_timer(self.do_movement)
        else:
            Plotter().plot(self.verlet.pes, self.verlet.kes)

    def move_molecules(self):
        self.verlet.process_molecules(self.molecules)

if __name__ == '__main__':
    sim = Simulator()

    sim.canvas.start()
