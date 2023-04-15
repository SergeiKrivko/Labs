from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from plot import Plot
from toolbar import Toolbar


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout()
        central_widget.setLayout(layout)
        self.resize(640, 480)

        self.objects = []

        self.toolbar = Toolbar()
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
        
        self.toolbar.draw_object.connect(self.plot.create_object)

    def add_object(self, obj):
        self.objects.append(obj)
        self.plot.update()
