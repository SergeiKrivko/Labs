from PyQt5.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QDoubleSpinBox, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal
import math
from derivative import der


class InputWidget(QWidget):
    drawFunc = pyqtSignal(object, float, float)

    def __init__(self, parent):
        super(InputWidget, self).__init__(parent)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(20, 20, 20, 20)

        # Function
        layout = QHBoxLayout()
        label = QLabel('y =', self)
        label.setFont(QFont('Arial', 20))
        label.setFixedSize(40, 40)
        layout.addWidget(label)

        self.function_line = QLineEdit(self)
        self.function_line.setFixedSize(320, 40)
        self.function_line.setFont(QFont('Arial', 20))
        self.function_line.setText('x ** 2')

        layout.addWidget(self.function_line)
        self.layout.addLayout(layout)

        # Start value
        layout = QHBoxLayout()
        layout.setContentsMargins(50, 0, 50, 0)

        label = QLabel('a =', self)
        label.setFont(QFont('Arial', 14))
        label.setFixedSize(40, 40)
        layout.addWidget(label)

        self.start_box = QDoubleSpinBox(self)
        self.start_box.setFixedSize(160, 40)
        self.start_box.setMinimum(-1e100)
        self.start_box.setMaximum(1e100)
        self.start_box.setValue(-10)
        self.start_box.setFont(QFont('Arial', 14))
        layout.addWidget(self.start_box)
        self.layout.addLayout(layout)

        # Stop value
        layout = QHBoxLayout()
        layout.setContentsMargins(50, 0, 50, 0)

        label = QLabel('b =', self)
        label.setFont(QFont('Arial', 14))
        label.setFixedSize(40, 40)
        layout.addWidget(label)

        self.stop_box = QDoubleSpinBox(self)
        self.stop_box.setFixedSize(160, 40)
        self.stop_box.setMinimum(-1e100)
        self.stop_box.setMaximum(1e100)
        self.stop_box.setValue(10)
        self.stop_box.setFont(QFont('Arial', 14))
        layout.addWidget(self.stop_box)
        self.layout.addLayout(layout)

        # Epsilon
        layout = QHBoxLayout()
        layout.setContentsMargins(50, 0, 50, 0)

        label = QLabel('eps =', self)
        label.setFont(QFont('Arial', 14))
        label.setFixedSize(50, 40)
        layout.addWidget(label)

        self.eps_box = QLineEdit(self)
        self.eps_box.setFixedSize(160, 40)
        self.eps_box.setFont(QFont('Arial', 14))
        layout.addWidget(self.eps_box)
        self.layout.addLayout(layout)

        self.button = QPushButton("Построить", self)
        self.button.setFixedSize(200, 50)
        self.button.setFont(QFont('Arial', 20))
        self.button.clicked.connect(self.done)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def done(self, *args):
        try:
            func = eval('lambda x: ' + self.function_line.text(), {'math': math, 'm': math})
            print(der(self.function_line.text()))
            d = eval('lambda x: ' + der(self.function_line.text()), {'math': math, 'm': math})
        except Exception as ex:
            print(f'Invalid function:\n{ex.__class__.__name__}: {ex}')
        else:
            # self.drawFunc.emit(func, self.start_box.value(), self.stop_box.value())
            self.drawFunc.emit(d, self.start_box.value(), self.stop_box.value())
