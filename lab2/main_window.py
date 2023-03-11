from PyQt5.QtWidgets import QMainWindow
from plot import Plot
from table import TableWidget
from input_widget import InputWidget
from root_refirement import find_roots
import math
from derivative import der


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(960, 640)
        self.setWindowTitle("Lab2")

        self.input_widget = InputWidget(self)
        self.input_widget.setGeometry(0, 0, 320, 640)

        self.plot = Plot(self)
        self.plot.setGeometry(320, 0, 640, 320)

        self.table = TableWidget(self)
        self.table.setGeometry(340, 340, 600, 280)

        self.input_widget.drawFunc.connect(self.done)

    def done(self, *args):
        func_str, a, b, h, eps, max_iter = args
        func = eval('lambda x: ' + func_str, {'math': math, 'm': math})
        der1 = eval('lambda x: ' + der(func_str), {'math': math, 'm': math})
        der2 = eval('lambda x: ' + der(der(func_str)), {'math': math, 'm': math})
        der3 = eval('lambda x: ' + der(der(der(func_str))), {'math': math, 'm': math})
        self.plot.draw_func(func, a, b)
        self.table.clear()
        for a_b, data in find_roots(func, der1, a, b, eps, h, max_iter):
            if data[-1] != 0:
                self.table.add_row(f"[{a_b[0]}, {a_b[1]}]", *map(format_number, data))

        for _, el in find_roots(der2, der3, a, b, eps, h, max_iter):
            print(el)


def format_number(n):
    if n is None:
        return ""
    if isinstance(n, float):
        return '{:6g}'.format(n)
    return str(n)

