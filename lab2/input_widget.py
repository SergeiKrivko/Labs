from PyQt5.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QDoubleSpinBox, QLabel, QPushButton, QSpinBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal
import math


class InputWidget(QWidget):
    drawFunc = pyqtSignal(str, float, float, float, float, int)

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
        self.function_line.setFixedSize(240, 40)
        self.function_line.setFont(QFont('Arial', 20))
        self.function_line.setText('x ** 2')

        layout.addWidget(self.function_line)
        self.layout.addLayout(layout)

        # Start value
        layout = QHBoxLayout()
        layout.setContentsMargins(50, 0, 50, 0)

        label = QLabel('a =', self)
        label.setFont(QFont('Arial', 14))
        label.setFixedSize(50, 40)
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
        label.setFixedSize(50, 40)
        layout.addWidget(label)

        self.stop_box = QDoubleSpinBox(self)
        self.stop_box.setFixedSize(160, 40)
        self.stop_box.setMinimum(-1e100)
        self.stop_box.setMaximum(1e100)
        self.stop_box.setValue(10)
        self.stop_box.setFont(QFont('Arial', 14))
        layout.addWidget(self.stop_box)
        self.layout.addLayout(layout)

        # Step value
        layout = QHBoxLayout()
        layout.setContentsMargins(50, 0, 50, 0)

        label = QLabel('h =', self)
        label.setFont(QFont('Arial', 14))
        label.setFixedSize(50, 40)
        layout.addWidget(label)

        self.step_box = QDoubleSpinBox(self)
        self.step_box.setFixedSize(160, 40)
        self.step_box.setMinimum(-1e100)
        self.step_box.setMaximum(1e100)
        self.step_box.setValue(1)
        self.step_box.setFont(QFont('Arial', 14))
        layout.addWidget(self.step_box)
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
        self.eps_box.setText("1e-10")
        layout.addWidget(self.eps_box)
        self.layout.addLayout(layout)

        # Iter box
        layout = QHBoxLayout()
        layout.setContentsMargins(50, 0, 50, 0)

        label = QLabel('Nmax =', self)
        label.setFont(QFont('Arial', 14))
        label.setFixedSize(50, 40)
        layout.addWidget(label)

        self.iter_box = QSpinBox(self)
        self.iter_box.setFixedSize(160, 40)
        self.iter_box.setMinimum(1)
        self.iter_box.setMaximum(100000000)
        self.iter_box.setValue(1000)
        self.iter_box.setFont(QFont('Arial', 14))
        layout.addWidget(self.iter_box)
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
            eps = float(self.eps_box.text())
        except ValueError:
            print("Invalid eps")
        except Exception as ex:
            print(f'Invalid function:\n{ex.__class__.__name__}: {ex}')
        else:
            self.drawFunc.emit(self.function_line.text(), self.start_box.value(), self.stop_box.value(),
                               self.step_box.value(), eps, self.iter_box.value())
