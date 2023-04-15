from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QDialog, QDialogButtonBox, QLabel, QSpinBox, \
    QColorDialog, QComboBox
from PyQt5.QtGui import QColor
import angem as ag

INITIAL_COLOR = QColor(0, 0, 0)


class Toolbar(QWidget):
    add_object = pyqtSignal(object)
    draw_object = pyqtSignal(str)

    def __init__(self):
        super(Toolbar, self).__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setFixedWidth(150)
        layout.setAlignment(Qt.AlignTop)

        layout.addWidget(QLabel("Режим"))
        self.mode_combo_box = QComboBox()
        self.mode_combo_box.addItems(["По координатам", "Мышью"])
        layout.addWidget(self.mode_combo_box)

        layout.addWidget(QLabel("Рисование"))

        self.button_point = QPushButton("Точка")
        self.button_point.clicked.connect(self.create_point)
        layout.addWidget(self.button_point)

        self.button_segment = QPushButton("Отрезок")
        self.button_segment.clicked.connect(self.create_segment)
        layout.addWidget(self.button_segment)

        self.button_line = QPushButton("Прямая")
        self.button_line.clicked.connect(self.create_line)
        layout.addWidget(self.button_line)

    def create_point(self):
        if self.mode_combo_box.currentIndex():
            self.draw_object.emit('point')
            return
        self.dlg = CustomDialog("Точка", {"x:": int, "y:": int, 'Цвет': QColor}, INITIAL_COLOR)
        if self.dlg.exec():
            self.add_object.emit(ag.Point(self.dlg.widgets['x:'].value(), self.dlg.widgets['y:'].value(),
                                          self.dlg.color))

    def create_segment(self):
        if self.mode_combo_box.currentIndex():
            self.draw_object.emit('segment')
            return
        self.dlg = CustomDialog("Отрезок", {"x1:": int, "y1:": int, "x2:": int, "y2:": int, 'Цвет': QColor},
                                INITIAL_COLOR)
        if self.dlg.exec():
            self.add_object.emit(ag.Segment(ag.Point(
                self.dlg.widgets['x1:'].value(), self.dlg.widgets['y1:'].value()),
                ag.Point(self.dlg.widgets['x2:'].value(), self.dlg.widgets['y2:'].value()),
                self.dlg.color))

    def create_line(self):
        if self.mode_combo_box.currentIndex():
            self.draw_object.emit('line')
            return
        self.dlg = CustomDialog("Прямая", {"x1:": int, "y1:": int, "x2:": int, "y2:": int, 'Цвет': QColor},
                                INITIAL_COLOR)
        if self.dlg.exec():
            self.add_object.emit(ag.Line(ag.Point(
                self.dlg.widgets['x1:'].value(), self.dlg.widgets['y1:'].value()),
                ag.Point(self.dlg.widgets['x2:'].value(), self.dlg.widgets['y2:'].value()),
                self.dlg.color))


class CustomDialog(QDialog):
    def __init__(self, name, struct: dict, color):
        super(CustomDialog, self).__init__()
        self.setWindowTitle(name)
        self.setMinimumWidth(240)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        self.widgets = dict()

        for key, item in struct.items():
            layout.addWidget(QLabel(str(key)))
            if item == int:
                widget = QSpinBox()
                widget.setMinimum(-1000000)
                widget.setMaximum(1000000)
            elif item == QColor:
                widget = QPushButton()
                widget.setFixedWidth(40)
                self.connect_color_button(widget)
            else:
                raise TypeError("Unknown type")

            layout.addWidget(widget)
            self.widgets[key] = widget

        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
        self.color = color

    def connect_color_button(self, widget):
        def triggered():
            color = QColorDialog.getColor(initial=self.color)
            print(f"color: rgba{color.getRgb()};")
            widget.setStyleSheet(f"background-color: rgba{color.getRgb()};")
            self.color = color

        widget.clicked.connect(triggered)
