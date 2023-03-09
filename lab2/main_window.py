from PyQt5.QtWidgets import QMainWindow
from plot import Plot
from table import TableWidget
from input_widget import InputWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(960, 640)
        self.setWindowTitle("Lab2")

        self.input_widget = InputWidget(self)
        self.input_widget.setGeometry(0, 0, 320, 400)

        self.plot = Plot(self)
        self.plot.setGeometry(320, 0, 640, 320)

        self.table = TableWidget(self)
        self.table.setGeometry(340, 340, 600, 280)

        self.input_widget.drawFunc.connect(lambda *args: self.plot.draw_func(*args))

