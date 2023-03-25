import math
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QDoubleSpinBox, QVBoxLayout, QLineEdit, QApplication, QLabel, QWidget, \
    QPushButton, QMessageBox
from root_refirement import binary_search_method


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.setFont(QFont("Calibri", 12))

        layout.addWidget(QLabel("Функция:"))
        self.function_widget = QLineEdit()
        layout.addWidget(self.function_widget)

        layout.addWidget(QLabel("Начало отрезка:"))
        self.start_value_widget = QDoubleSpinBox()
        self.start_value_widget.setMinimum(-1e30)
        self.start_value_widget.setMaximum(1e30)
        layout.addWidget(self.start_value_widget)

        layout.addWidget(QLabel("Конец отрезка:"))
        self.end_value_widget = QDoubleSpinBox()
        self.end_value_widget.setMinimum(-1e30)
        self.end_value_widget.setMaximum(1e30)
        layout.addWidget(self.end_value_widget)

        layout.addWidget(QLabel("Точность:"))
        self.eps_widget = QDoubleSpinBox()
        self.eps_widget.setMinimum(1e-30)
        self.eps_widget.setMaximum(10)
        self.eps_widget.setDecimals(10)
        layout.addWidget(self.eps_widget)

        self.button = QPushButton()
        self.button.setText("Вычислить")
        self.button.clicked.connect(self.calc)
        layout.addWidget(self.button)

        layout.addWidget(QLabel("Результат:"))
        self.output_widget = QLineEdit()
        self.output_widget.setReadOnly(True)
        layout.addWidget(self.output_widget)

        self.function_widget.setText("m.sin(x)")
        self.start_value_widget.setValue(-1)
        self.end_value_widget.setValue(1)
        self.eps_widget.setValue(0.01)

    def calc(self, *args):
        try:
            func = eval("lambda x:" + self.function_widget.text(), {'math': math, 'm': math})
            res = binary_search_method(func, self.start_value_widget.value(), self.end_value_widget.value(),
                                       self.eps_widget.value())
        except Exception as ex:
            QMessageBox.warning(self, "Error", f"Не удалось вычислить значение функции:\n{ex.__class__.__name__}: {ex}")
        else:
            self.output_widget.setText(str(res))


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
