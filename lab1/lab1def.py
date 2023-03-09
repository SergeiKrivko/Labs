"""
Кривко Сергей Евгеньевич ИУ7-24Б
"""

from PyQt5 import QtWidgets, QtGui
from lab1def_convert import convert_to_added_code, covert_to_reverse_code


class MainWindow(QtWidgets.QMainWindow):
    """Главное окно"""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(400, 300)
        self.setWindowTitle('Лабораторная работа №1')

        self.input_widget = QtWidgets.QLineEdit('0' * 8, self)
        self.input_widget.setGeometry(80, 50, 240, 40)
        self.input_widget.setFont(QtGui.QFont('Arial', 20))
        self.input_widget.setClearButtonEnabled(True)
        self.input_widget.textChanged.connect(self.text_changed)

        self.button = QtWidgets.QPushButton('Перевести', self)
        self.button.setGeometry(120, 100, 160, 40)
        self.button.clicked.connect(lambda *args: self.convert())

        self.output_widget1 = QtWidgets.QLineEdit(self)
        self.output_widget1.setGeometry(80, 150, 240, 40)
        self.output_widget1.setFont(QtGui.QFont('Arial', 20))
        self.output_widget1.setReadOnly(True)

        self.output_widget2 = QtWidgets.QLineEdit(self)
        self.output_widget2.setGeometry(80, 200, 240, 40)
        self.output_widget2.setFont(QtGui.QFont('Arial', 20))
        self.output_widget2.setReadOnly(True)

    def convert(self):
        reversed_code = covert_to_reverse_code(self.input_widget.text())
        added_code = convert_to_added_code(reversed_code)

        self.output_widget1.setText(reversed_code)
        self.output_widget2.setText(added_code)

    def text_changed(self):
        text = list(self.input_widget.text().lstrip('0'))
        lst = []
        for s in text:
            if s == '1' or s == '0':
                lst.append(s)
        text = ''.join(lst)
        text = '0' * (8 - len(text)) + text[:8]
        if text == '':
            text = '0'
        self.input_widget.setText(text)


def main():
    app = QtWidgets.QApplication([])
    main_window = MainWindow()
    main_window.show()

    app.exec_()


if __name__ == '__main__':
    main()
