from PyQt5.QtCore import QThread, pyqtSignal

from lab4.logic import get_circle


class Looper(QThread):
    complete = pyqtSignal(object)
    step = pyqtSignal(int)

    def __init__(self, points):
        super(Looper, self).__init__()
        self.points = points

    def run(self):
        for count, res in get_circle(self.points):
            self.step.emit(count)
            if res:
                self.complete.emit(res)
                return
