from PyQt5.QtWidgets import QVBoxLayout, QWidget, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt
import numpy as np


class Plot(QWidget):
    def __init__(self, parent=None):
        super(Plot, self).__init__(parent)

        self.figure = plt.figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.ax = None

    def clear(self):
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)

    def draw_func(self, func, a, b):
        try:
            x = np.linspace(a, b, 1000)
            y = [func(u) for u in x]
            self.ax.plot(x, y)
            self.canvas.draw()
        except Exception as ex:
            QMessageBox.warning(self, 'Ошибка', f'Ошибка при построении функции:\n{ex.__class__.__name__}: {ex}')

    def draw_points(self, x, y):
        self.ax.scatter(x, y)
        self.canvas.draw()

