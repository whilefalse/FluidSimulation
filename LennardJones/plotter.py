from matplotlib import pyplot as plt

class Plotter(object):
    def plot(self, pes, kes):
        f = plt.figure()
        ax = f.add_subplot(111)
        ts = xrange(0, len(pes))
        tots = map(sum, zip(pes, kes))

        l1, = ax.plot(ts, pes, 'b--')
        l2, = ax.plot(ts, kes, 'g--')
        l3, = ax.plot(ts, tots, 'r-')

        ax.set_ylabel(r'Energy / reduced units')
        ax.set_xlabel(r'Time / steps')
        ax.grid(True, 'major')
        ax.legend((l1,l2,l3), ('PE', 'KE', 'TOT'))

        plt.show()

