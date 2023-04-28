from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from plot import Plot
from toolbar import Toolbar
import angem as ag
from logic import get_circle, Looper


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.looper = None
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout()
        central_widget.setLayout(layout)
        self.resize(640, 480)

        self.objects = []

        self.toolbar = Toolbar(self.objects)
        self.toolbar.add_object.connect(self.add_object)
        layout.addWidget(self.toolbar)

        plot_bar = QWidget()
        plot_bar.setStyleSheet(f"background-color: #FFFFFF; border: 2px solid #000000; border-radius: 10px;")
        pb_layout = QHBoxLayout()
        pb_layout.setContentsMargins(0, 0, 0, 0)
        plot_bar.setLayout(pb_layout)

        self.plot = Plot(self.objects)
        pb_layout.addWidget(self.plot)
        layout.addWidget(plot_bar)
        self.plot.add_point.connect(self.add_object)

        self.toolbar.button_point.clicked.connect(self.plot.set_drawing_mode)
        self.toolbar.delete_object.connect(self.delete_object)
        self.toolbar.object_modified.connect(self.modify_object)
        self.toolbar.clear.connect(self.clear_objects)

        self.toolbar.button_get_circle.clicked.connect(self.get_circle)

    def add_object(self, obj):
        self.objects.append(obj)
        self.toolbar.update_objects_list()
        self.plot.update()

    def modify_object(self, index, new_object):
        self.objects[index] = new_object
        self.plot.update()
        self.toolbar.update_objects_list()

    def clear_objects(self, points=False, circles=False):
        if points and circles:
            self.objects.clear()
        else:
            if points:
                i = 0
                while i < len(self.objects):
                    if isinstance(self.objects[i], ag.Point):
                        self.objects.pop(i)
                    else:
                        i += 1
            if circles:
                i = 0
                while i < len(self.objects):
                    if isinstance(self.objects[i], ag.Circle):
                        self.objects.pop(i)
                    else:
                        i += 1
        self.toolbar.update_objects_list()

    def delete_object(self, index):
        if index < 0:
            return
        self.objects.pop(index)
        self.toolbar.update_objects_list()
        self.plot.update()
        self.toolbar.list_widget.setCurrentRow(min(index, self.toolbar.list_widget.count() - 1))

    def get_circle(self):
        self.clear_objects(circles=True)
        self.toolbar.set_disabled(True)
        self.toolbar.progress_mode_on(len(self.objects) * (len(self.objects) - 1) * (len(self.objects) - 2) // 6)

        self.looper = Looper(self.objects)
        self.looper.complete.connect(self.calculation_complete)
        self.looper.step.connect(lambda n: self.toolbar.progress_bar.setValue(self.toolbar.progress_bar.value() + n))
        self.looper.start()

    def calculation_complete(self, res):
        if res:
            self.add_object(res)
        self.toolbar.progress_mode_off()
