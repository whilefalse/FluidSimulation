import Tkinter as Tk

class Canvas(object):
    def __init__(self, width, height):
        self.canvas_width = 500.0
        self.canvas_height = 500.0
        self.width = float(width)
        self.height = float(height)
        self.radius = 2
        self.setup_window()

    def setup_window(self):
        self.tk = Tk.Tk()
        self.canvas = Tk.Canvas(
                self.tk,
                width=self.canvas_width,
                height=self.canvas_height,
                )
        self.canvas.pack()

    def setup_timer(self, func):
        self.tk.after(1, func)

    def refresh(self, molecules):
        self.canvas.delete(Tk.ALL)

        for molecule in molecules:
            self.canvas.create_oval(
                    molecule.r.x / self.width * self.canvas_width - self.radius,
                    molecule.r.y / self.height * self.canvas_height - self.radius,
                    molecule.r.x / self.width * self.canvas_width + self.radius,
                    molecule.r.y / self.height * self.canvas_height + self.radius,
                    fill = 'black'
                    )

    def start(self):
        Tk.mainloop()
