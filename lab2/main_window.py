from PyQt5.QtWidgets import QMainWindow, QMessageBox
from lab2.plot import Plot
from lab2.table import TableWidget
from lab2.input_widget import InputWidget
from lab2.root_refirement import find_roots
import math
from lab2.derivative import der


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

        self.input_widget.drawFunc.connect(self.do)

    def do(self, *args):
        self.plot.clear()
        func_str, a, b, h, eps, max_iter = args
        func = eval('lambda x: ' + func_str, {'math': math, 'm': math})
        try:
            der1 = eval('lambda x: ' + der(func_str), {'math': math, 'm': math})
        except Exception as ex:
            QMessageBox.warning(self, 'Ошибка', f'Не удалось найти производную:\n{ex.__class__.__name__}: {ex}')
        else:
            self.plot.draw_func(func, a, b)
            self.table.clear()
            for a_b, data in find_roots(func, der1, a, b, eps, h, max_iter):
                if data[-1] != -1:
                    self.table.add_row(f"[{a_b[0]}, {a_b[1]}]", *format_numbers(data))

            try:
                der2 = eval('lambda x: ' + der(der(func_str)), {'math': math, 'm': math})
                der3 = eval('lambda x: ' + der(der(der(func_str))), {'math': math, 'm': math})
            except Exception as ex:
                QMessageBox.warning(self, 'Ошибка', f'Не удалось найти производную:\n{ex.__class__.__name__}: {ex}')
            else:
                lst = []
                for _, el in find_roots(der2, der3, a, b, eps, h, max_iter):
                    if el[0] is not None:
                        lst.append(el[0])
                self.plot.draw_points(lst, list(map(func, lst)))


def format_numbers(lst):
    res = []
    if lst[0] is not None:
        res.append('{:6g}'.format(lst[0]))
    else:
        res.append('')
    if lst[1] is not None:
        res.append('{:1g}'.format(lst[1]))
    else:
        res.append('')
    if lst[2] is not None:
        res.append(str(lst[2]))
    else:
        res.append('')
    res.append(str(lst[3]))
    return res
