from PyQt5.QtWidgets import QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np


class Plot(QWidget):
    def __init__(self, parent=None):
        super(Plot, self).__init__(parent)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.draw_func(lambda x: x**2, -10, 10)

    def draw_func(self, func, a, b):
        try:
            x = np.linspace(a, b, 1000)
            y = [func(u) for u in x]
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(x, y)
            self.canvas.draw()
        except Exception as ex:
            print(f"{ex.__class__.__name__}: {ex}")
