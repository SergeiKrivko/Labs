import polynom
from matrix import Matrix
from fraction import Fraction
import slae
import angem
import linal
import math
import json
from Math.function import MathFunction

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QLineEdit, QTextEdit, QAction, QWidget, QPushButton, QGridLayout, QFileDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


def remove_space(string):
    return string.replace(' ', '')


def input_matrix_of_int():
    return Matrix(name=var, function=int)


def input_matrix_of_float():
    return Matrix(name=var, function=float)


def input_matrix_of_fractions():
    return Matrix(name=var, function=Fraction)


def tr(matrix):
    return matrix.transpose()


def smart_input(s):
    for function in [angem.Plane.from_str, angem.Vector.from_str, angem.Point.from_str, Fraction]:
        try:
            return function(s)
        except Exception:
            pass
    return


def smart_input2(s):
    try:
        return Fraction(s)
    except Exception:
        return eval(s)


def command_slae():
    s = slae.input_slae(function=Fraction, print_slae=True)
    print('Решение:')
    slae.print_slae_solve(slae.solve_slae(s[0], s[1]))
    print()


variables = {'det': Matrix.determinant, 'opp': Matrix.opposite, 'tr': tr, 'rank': Matrix.rang, 'rg': Matrix.rang,
             'imatrix': input_matrix_of_int, 'fmatrix': input_matrix_of_float, 'frmatrix': input_matrix_of_fractions,
             'slae': command_slae, 'angem': angem, 'ag': angem, 'vector': linal.Vector, 'basis': linal.Basis,
             'polynom': polynom.Polynom, 'monomial': polynom.Monomial, 'circle': angem.Circle, 'sphere': angem.Sphere,
             'matrix': Matrix, 'math': math, 'm': math, 'lin_op': linal.LinealOperator, "fraction": Fraction,
             'func': MathFunction, 'function': MathFunction}


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Math Program")

        font = QFont('Courier', 12)
        self.text = ""
        self.command_list = []
        self.current_command = 0

        self.cmd = QLineEdit(self)
        self.cmd.setGeometry(0, self.height() - 30, self.width(), 30)
        self.cmd.setFont(font)
        self.cmd.returnPressed.connect(self.input_command)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(0, 20, self.width(), self.height() - 50)
        self.text_edit.setFont(font)
        self.text_edit.setReadOnly(True)

        self.file_dialog = QFileDialog(self)

        self.menu = MenuBar(
            {
                "File":
                    {
                        "Save": (lambda: print("save"), "Ctrl+S"),
                        "Open": (self.open, "Ctrl+Alt+Y"),
                        "Save as": (lambda: self.save(), "Ctrl+Shift+S")
                    }})

        self.setMenuBar(self.menu)

        self.resize(960, 640)

    def keyPressEvent(self, a0) -> None:
        if a0.key() == Qt.Key_Up:
            if self.current_command < len(self.command_list) - 1:
                self.current_command += 1
                self.cmd.setText(self.command_list[self.current_command])
        elif a0.key() == Qt.Key_Down:
            if self.current_command <= 0:
                self.current_command = -1
                self.cmd.setText("")
            else:
                self.current_command -= 1
                self.cmd.setText(self.command_list[self.current_command])

    def print(self, *args, sep=' ', end='<br>'):
        self.text += sep.join(map(str, args)).replace("\n", "<br>") + end
        self.text_edit.setHtml(self.text)

    def input_command(self):
        command = self.cmd.text()
        self.print("<font size = '3' color='red'> >>> </font> <font size = '3' color='blue'>" + command + "</font>")
        self.cmd.setText("")
        self.command_list.insert(0, command)
        if len(self.command_list) > 50:
            self.command_list.pop()
        self.current_command = -1
        global var
        if '=' in command:
            i = command.index('=')
            var, arg = command[:i - 1].strip(), command[i + 1:].strip()
            for symbol in '-+*/ ().,':
                if symbol in var:
                    arg = command.strip()
                    res = self.execute_command(arg, var)
                    if res:
                        self.print(res)
                    break
            variables[var] = self.execute_command(arg, var)
        else:
            var = ""
            arg = command.strip()
            res = self.execute_command(arg, "")
            if res:
                self.print(res)

    def resizeEvent(self, a0) -> None:
        self.cmd.setGeometry(0, self.height() - 30, self.width(), 30)
        self.text_edit.setGeometry(0, 20, self.width(), self.height() - 50)

    def execute_command(self, com, var):
        if com.strip() == '':
            return Matrix(name=var, function=smart_input2)
        a = smart_input(com)
        if a is not None:
            return a
        try:
            return eval(com, variables)
        except Exception as ex:
            self.print(f'{ex.__class__.__name__}: {ex}')

    def save(self):
        path = self.file_dialog.getSaveFileName()[0]
        dct = dict()
        for key, item in variables.items():
            src = serialize_obj(item)
            if src is not None:
                dct[key] = src
        serialize(dct, path)

    def open(self):
        path = self.file_dialog.getOpenFileName()[0]
        dct = deserialize(path)
        for key, item in dct.items():
            variables[key] = eval(item, variables)


class MenuBar(QMenuBar):
    def __init__(self, menu_dict):
        super().__init__()

        for name in menu_dict:
            if not isinstance(menu_dict[name], dict):
                action = QAction('&{}'.format(name), self)
                action.triggered.connect(menu_dict[name][0])
                if menu_dict[name][1]:
                    action.setShortcut(menu_dict[name][1])
                self.addAction(action)
            else:
                menu = self.addMenu('&{}'.format(name))
                menu.addActions(self.unpack(menu_dict[name]))

    def unpack(self, data):
        actions = list()
        for key in data:
            action = QAction('&{}'.format(key), self)
            action.triggered.connect(data[key][0])
            if data[key][1]:
                action.setShortcut(data[key][1])
            actions.append(action)
        return actions


class InputMatrixWidget(QWidget):
    def __init__(self):
        super(InputMatrixWidget, self).__init__()
        self.setFixedSize(640, 480)
        self.n, self.m = 3, 3

        self.grid = QGridLayout()

        self.main_widget = QWidget(self)
        self.widgets = []
        for i in range(10):
            self.widgets.append([])
            for j in range(10):
                line = QLineEdit(self)
                self.widgets[i].append(line)
                line.setFixedSize(100, 24)
                self.grid.addItem(line, i, j)

        self.main_widget.setLayout(self.layout)


def serialize_obj(obj):
    if isinstance(obj, Matrix):
        return f"matrix({str(obj.mtrx)})"
    if isinstance(obj, linal.Vector):
        return f"vector({','.join(map(serialize_obj, obj.coordinates))},basis={serialize_obj(obj.basis)})"
    if isinstance(obj, linal.Basis):
        return f"basis({','.join(map(serialize_obj, obj.vectors))})"
    if isinstance(obj, linal.LinealOperator):
        return f"lin_op({','.join(obj.str_operations)})"
    if isinstance(obj, MathFunction):
        return f"func('{obj}', var='{obj.var}')"
    if isinstance(obj, Fraction):
        return f"fraction({obj.numerator},{obj.denominator})"
    if isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, str) or obj is None:
        return str(obj)


def serialize(data, path='history.txt'):
    hist = json.dumps(data)
    print(hist, file=open(path, 'w', encoding='utf-8'), end='')


def deserialize(path='history.txt'):
    return json.loads(open(path, encoding='utf-8').read())


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
