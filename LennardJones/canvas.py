import Tkinter as Tk
from config import config

class Canvas(object):
    def __init__(self):
        self.tk = Tk.Tk()
        self.canvas = Tk.Canvas(
                self.tk,
                width=config['canvas']['width'],
                height=config['canvas']['height'],
                )
        self.canvas.pack()

    def setup_timer(self, func):
        self.tk.after(config['simulation']['tick_time'], func)

    def refresh(self, molecules):
        self.canvas.delete(Tk.ALL)

        for molecule in molecules:
            self.canvas.create_oval(*self.canvas_oval(molecule), fill='black')

    def canvas_oval(self, m):
        r = config['canvas']['radius']
        w = float(config['canvas']['width'] / config['box']['width'])
        h = float(config['canvas']['height'] / config['box']['height'])

        return [m.r.x * w - r,
                m.r.y * h - r,
                m.r.x * w + r,
                m.r.y * h + r]

    def start(self):
        Tk.mainloop()
