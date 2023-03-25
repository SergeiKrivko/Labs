from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication, QFileDialog

from code_widget import CodeWidget
from testing_widget import TestingWidget
from tests_widget import TestsWidget
from menu_bar import MenuBar
import json
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.settings = dict() if not os.path.isfile("settings.txt") else \
            json.loads(open('settings.txt', encoding='utf-8').read())

        self.setWindowTitle("TestGenerator")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        central_widget.setLayout(layout)

        self.tests_widget = TestsWidget(self.settings)
        layout.addWidget(self.tests_widget)

        self.testing_widget = TestingWidget(self.settings)
        layout.addWidget(self.testing_widget)
        self.testing_widget.hide()

        self.code_widget = CodeWidget(self.settings)
        layout.addWidget(self.code_widget)
        self.code_widget.hide()

        self.menu_bar = MenuBar({
            'Открыть': (self.open_project, None),
            'Код': (self.show_code, None),
            'Тесты': (self.show_tests, None),
            'Тестирование': (self.show_testing, None),
            'Настройки': (lambda: print('settings'), None)
        })
        self.setMenuBar(self.menu_bar)

    def open_project(self):
        path = QFileDialog.getExistingDirectory(directory=self.settings.get('path', os.getcwd()))
        if path:
            self.settings['path'] = path
            self.tests_widget.open_tests()

    def show_tests(self):
        self.testing_widget.hide()
        self.code_widget.hide()
        self.tests_widget.show()

    def show_testing(self):
        self.tests_widget.hide()
        self.code_widget.hide()
        self.testing_widget.show()

    def show_code(self):
        self.testing_widget.hide()
        self.tests_widget.hide()
        self.code_widget.show()

    def closeEvent(self, a0):
        file = open("settings.txt", 'w', encoding="utf-8")
        file.write(json.dumps(self.settings))
        file.close()
        super(MainWindow, self).close()


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
