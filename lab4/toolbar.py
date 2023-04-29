from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QDialog, QDialogButtonBox, QLabel, QSpinBox, \
    QColorDialog, QListWidget, QHBoxLayout, QCheckBox, QProgressBar
from PyQt5.QtGui import QColor
import angem as ag

INITIAL_COLOR = QColor(0, 0, 0)


class Toolbar(QWidget):
    add_object = pyqtSignal(object)
    object_modified = pyqtSignal(int, object)
    delete_object = pyqtSignal(int)
    select_object = pyqtSignal(int)
    clear = pyqtSignal(bool, bool)

    def __init__(self, objects_list):
        super(Toolbar, self).__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setFixedWidth(200)
        layout.setAlignment(Qt.AlignTop)

        self.objects = objects_list

        self.button_point = QPushButton("Точка")
        self.button_point.setCheckable(True)
        layout.addWidget(self.button_point)

        buttons_layout = QHBoxLayout()
        layout.addLayout(buttons_layout)
        buttons_layout.setSpacing(0)

        self.button_add = QPushButton("+")
        buttons_layout.addWidget(self.button_add)
        self.button_add.clicked.connect(self.create_point)

        self.button_delete = QPushButton("✕")
        buttons_layout.addWidget(self.button_delete)
        self.button_delete.clicked.connect(lambda: self.delete_object.emit(self.list_widget.currentRow()))

        self.button_clean = QPushButton("🗑️")
        buttons_layout.addWidget(self.button_clean)
        self.button_clean.clicked.connect(lambda: self.clear_objects())

        self.list_widget = QListWidget()
        self.list_widget.doubleClicked.connect(self.modify_object)
        self.list_widget.currentRowChanged.connect(self.select_object.emit)
        layout.addWidget(self.list_widget)

        self.button_get_circle = QPushButton("Построить окружность")
        layout.addWidget(self.button_get_circle)

        self.progress_bar = QProgressBar()
        self.progress_bar.hide()
        layout.addWidget(self.progress_bar)

    def update_objects_list(self):
        self.list_widget.clear()
        for el in self.objects:
            self.list_widget.addItem(str(el))

    def set_disabled(self, flag):
        self.button_point.setDisabled(flag)
        self.button_add.setDisabled(flag)
        self.button_delete.setDisabled(flag)
        self.button_clean.setDisabled(flag)
        self.list_widget.setDisabled(flag)

    def progress_mode_on(self, max_value):
        self.button_get_circle.hide()
        self.progress_bar.show()
        self.set_disabled(True)
        self.progress_bar.setValue(0)
        self.progress_bar.setMaximum(max_value)

    def progress_mode_off(self):
        self.progress_bar.hide()
        self.button_get_circle.show()
        self.set_disabled(False)

    def create_point(self):
        self.dlg = CustomDialog("Точка", {"x:": int, "y:": int, 'Цвет': QColor}, INITIAL_COLOR)
        if self.dlg.exec():
            self.add_object.emit(ag.Point(self.dlg.widgets['x:'].value(), self.dlg.widgets['y:'].value(),
                                          self.dlg.color))

    def clear_objects(self):
        self.dlg = CleanObjectsDialog()
        if self.dlg.exec():
            self.clear.emit(self.dlg.check_box1.isChecked(), self.dlg.check_box2.isChecked())

    def modify_object(self):
        index = self.list_widget.currentRow()
        if self.list_widget.currentItem().text().startswith("point"):
            self.dlg = CustomDialog("Точка", {"x:": int, "y:": int, 'Цвет': QColor}, self.objects[index].color)
            self.dlg.widgets['x:'].setValue(self.objects[index].x)
            self.dlg.widgets['y:'].setValue(self.objects[index].y)
            if self.dlg.exec():
                self.object_modified.emit(self.list_widget.currentRow(),
                                          ag.Point(self.dlg.widgets['x:'].value(), self.dlg.widgets['y:'].value(),
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
                widget.setStyleSheet("border: 1px solid #A0A0A0;"
                                     "border-radius: 4px;")
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
            widget.setStyleSheet(f"background-color: rgba{color.getRgb()};"
                                 "border: 1px solid #A0A0A0;"
                                 "border-radius: 4px;")
            self.color = color

        widget.clicked.connect(triggered)


class CleanObjectsDialog(QDialog):
    def __init__(self):
        super(CleanObjectsDialog, self).__init__()
        self.setWindowTitle("Очистить")
        self.setMinimumWidth(240)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        layout1 = QHBoxLayout()
        layout1.setAlignment(Qt.AlignLeft)
        self.check_box1 = QCheckBox()
        layout1.addWidget(self.check_box1)
        layout1.addWidget(QLabel("Очистить точки"))
        layout.addLayout(layout1)

        layout2 = QHBoxLayout()
        layout2.setAlignment(Qt.AlignLeft)
        self.check_box2 = QCheckBox()
        layout2.addWidget(self.check_box2)
        layout2.addWidget(QLabel("Очистить результат"))
        layout.addLayout(layout2)

        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
