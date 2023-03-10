from PyQt5.QtWidgets import QWidget, QScrollArea, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class TableWidget(QWidget):
    def __init__(self, parent):
        super(TableWidget, self).__init__(parent)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setFixedSize(600, 280)

        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)

        self.widget = QWidget(self)

        for i in range(100):
            self.layout.addWidget(TableRow(self, i, 2/5, 3/7, 4/3, 5e-45 / 7, 6, 7))

        self.widget.setFixedHeight(36 * 100)
        self.widget.setLayout(self.layout)
        self.scroll_area.setWidget(self.widget)


class TableRow(QWidget):
    def __init__(self, parent, *args):
        super(TableRow, self).__init__(parent)

        self.layout = QHBoxLayout(self)
        self.layout.setSpacing(0)
        self.setFont(QFont('Arial', 10))
        self.style = "border: 1px solid #7F7F7F;"

        self.texts = [str(args[0])] + ["{:6g}".format(args[i]).strip() for i in range(1, 7)]
        self.widths = [30, 80, 80, 80, 80, 80, 80]

        self.widgets = []
        for i in range(7):
            widget = QLabel(self)
            self.widgets.append(widget)
            widget.setText(self.texts[i])
            widget.setStyleSheet(self.style)
            widget.setFixedSize(self.widths[i], 24)
            self.layout.addWidget(widget)

        self.setLayout(self.layout)
