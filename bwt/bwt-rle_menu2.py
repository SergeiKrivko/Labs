import bwt_rle
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('BWT - RLE')
        self.setFixedSize(500, 400)

        self.file_window = QtWidgets.QMainWindow()
        self.file_dialog = QtWidgets.QFileDialog(self.file_window)

        self.main_window = MainWindow(self)
        self.pack_window = None
        self.unpack_window = None
        self.progress_window = None

    def packing(self):
        self.pack_window = PackWindow(self)
        self.pack_window.show()
        self.main_window.hide()

    def unpacking(self):
        self.main_window.hide()
        self.unpack_window = UnpackWindow(self)
        self.unpack_window.show()

    def escape(self):
        if self.main_window is not None:
            self.main_window.show()
        if self.pack_window is not None:
            self.pack_window.hide()
        if self.unpack_window is not None:
            self.unpack_window.hide()


class MainWindow(QtWidgets.QWidget):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.setGeometry(QtCore.QRect(150, 120, 200, 140))

        self.button_pack = QtWidgets.QPushButton(self)
        self.button_pack.setText('Сжать')
        self.button_pack.setFont(QtGui.QFont('Arial', 18))
        self.button_pack.setGeometry(QtCore.QRect(0, 0, 200, 60))
        self.button_pack.clicked.connect(main_window.packing)

        self.button_unpack = QtWidgets.QPushButton(self)
        self.button_unpack.setText('Распаковать')
        self.button_unpack.setFont(QtGui.QFont('Arial', 18))
        self.button_unpack.setGeometry(QtCore.QRect(0, 80, 200, 60))
        self.button_unpack.clicked.connect(main_window.unpacking)


class PackWindow(QtWidgets.QWidget):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.setGeometry(QtCore.QRect(20, 20, 460, 360))

        self.main_window = main_window

        self.file1 = self.main_window.file_dialog.getOpenFileName()
        self.file2 = self.main_window.file_dialog.getSaveFileName()
        self.main_window.showMinimized()
        self.main_window.showNormal()
        self.bwt_size = 32
        self.sort = 'quick'
        self.smart_rle = True

        label1 = QtWidgets.QLabel(self)
        label1.setGeometry(QtCore.QRect(0, 0, 300, 16))
        label1.setText('Исходный файл')

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setGeometry(QtCore.QRect(0, 20, 300, 25))
        self.button1.setText(self.file1[0])
        self.button1.clicked.connect(self.select_open_file)

        label2 = QtWidgets.QLabel(self)
        label2.setGeometry(QtCore.QRect(0, 50, 300, 16))
        label2.setText('Конечный файл')

        self.button2 = QtWidgets.QPushButton(self)
        self.button2.setGeometry(QtCore.QRect(0, 70, 300, 25))
        self.button2.setText(self.file2[0])
        self.button2.clicked.connect(self.select_save_file)

        label3 = QtWidgets.QLabel(self)
        label3.setGeometry(QtCore.QRect(0, 100, 300, 16))
        label3.setText('Размер участков разбиения')

        spin_box = QtWidgets.QSpinBox(self)
        spin_box.setGeometry(QtCore.QRect(0, 120, 150, 25))
        spin_box.setMinimum(1)
        spin_box.setMaximum(1024)
        spin_box.setValue(32)
        spin_box.valueChanged.connect(self.set_bwt_size)

        label4 = QtWidgets.QLabel(self)
        label4.setGeometry(QtCore.QRect(0, 150, 300, 16))
        label4.setText('Метод сортировки')

        combo_box = QtWidgets.QComboBox(self)
        combo_box.setGeometry(QtCore.QRect(0, 170, 150, 25))
        combo_box.addItems(['quick sort', 'heap sort', 'python sort'])
        combo_box.currentIndexChanged.connect(lambda ind: self.set_sort_method(('quick', 'heap', 'python')[ind]))

        label5 = QtWidgets.QLabel(self)
        label5.setGeometry(QtCore.QRect(20, 204, 300, 16))
        label5.setText('Smart RLE')

        checkbox = QtWidgets.QCheckBox(self)
        checkbox.setGeometry(QtCore.QRect(0, 200, 150, 25))
        checkbox.setChecked(True)
        checkbox.stateChanged.connect(self.set_smart_rle)

        button_esc = QtWidgets.QPushButton(self)
        button_esc.setGeometry(QtCore.QRect(0, 250, 150, 50))
        button_esc.setText('Отмена')
        button_esc.setFont(QtGui.QFont('Arial', 18))
        button_esc.clicked.connect(lambda *args: self.main_window.escape())

        button_pack = QtWidgets.QPushButton(self)
        button_pack.setGeometry(QtCore.QRect(170, 250, 150, 50))
        button_pack.setText('Сжать')
        button_pack.setFont(QtGui.QFont('Arial', 18))
        button_pack.clicked.connect(lambda *args: self.start_packing(main_window))

    def select_open_file(self):
        self.file1 = self.main_window.file_dialog.getOpenFileName()
        self.button1.setText(self.file1[0])

    def select_save_file(self):
        self.file2 = self.main_window.file_dialog.getSaveFileName()
        self.button2.setText(self.file2[0])

    def set_bwt_size(self, size):
        self.bwt_size = size

    def set_sort_method(self, sort):
        self.sort = sort

    def set_smart_rle(self, flag):
        self.smart_rle = flag

    def start_packing(self, main_window):
        if self.file1[0] == '' or self.file2[0] == '':
            return
        self.hide()
        main_window.progress_window = ProgressWindow(main_window)
        main_window.progress_window.show()
        main_window.progress_window.start_packing(self.file1, self.file2, self.bwt_size, self.sort, self.smart_rle)


class External(QtCore.QThread):
    def __init__(self, file1, file2, bwt_size, sort, smart_rle, pack):
        super().__init__()
        self.file1 = file1
        self.file2 = file2
        self.bwt_size = bwt_size
        self.sort = sort
        self.smart_rle = smart_rle
        self.pack = pack

    countChanged = QtCore.pyqtSignal(int)
    final = QtCore.pyqtSignal(tuple)

    def run(self):
        def emit(value):
            self.countChanged.emit(int(value))
            time.sleep(0.001)

        if self.pack:
            self.final.emit(bwt_rle.pack(self.file1[0], self.file2[0], size=self.bwt_size * 1024, sort=self.sort,
                                         smart_rle=self.smart_rle, func=emit, verbose=False))
        else:
            bwt_rle.unpack(self.file1[0], self.file2[0], func=emit, verbose=False)
            self.final.emit(tuple())


class ProgressWindow(QtWidgets.QWidget):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.setGeometry(QtCore.QRect(20, 20, 460, 360))

        self.main_window = main_window

        self.progress_bar = QtWidgets.QProgressBar(self)
        self.progress_bar.setGeometry(QtCore.QRect(40, 180, 400, 30))
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)

        self.calc = None

    def start_packing(self, file1, file2, bwt_size, sort, smart_rle):
        self.calc = External(file1, file2, bwt_size, sort, smart_rle, True)
        self.calc.countChanged.connect(self.progress_bar.setValue)
        self.calc.final.connect(self.final)
        self.calc.start()

    def final(self, info):
        button = QtWidgets.QPushButton(self)
        button.setGeometry(QtCore.QRect(155, 220, 150, 50))
        button.setText('ОК')
        button.setFont(QtGui.QFont('Arial', 20))
        button.clicked.connect(self.exit)
        button.show()

        info_panel = QtWidgets.QWidget(self)
        info_panel.setGeometry(QtCore.QRect(60, 60, 400, 100))
        layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel(info_panel)
        label.setText('Размер исходного файла: ' + info[0])
        label.setFont(QtGui.QFont('Arial', 12))
        layout.addWidget(label)
        label = QtWidgets.QLabel(info_panel)
        label.setText('Размер конечного файла: ' + info[1])
        label.setFont(QtGui.QFont('Arial', 12))
        layout.addWidget(label)
        label = QtWidgets.QLabel(info_panel)
        label.setText('Степень сжатия: ' + info[2])
        label.setFont(QtGui.QFont('Arial', 12))
        layout.addWidget(label)
        label = QtWidgets.QLabel(info_panel)
        label.setText('Время сжатия: ' + str(int(info[3])) + ' с')
        label.setFont(QtGui.QFont('Arial', 12))
        layout.addWidget(label)

        info_panel.setLayout(layout)
        info_panel.show()

    def exit(self):
        self.hide()
        self.main_window.main_window.show()


class ProgressWindowUnpack(QtWidgets.QWidget):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.setGeometry(QtCore.QRect(20, 20, 460, 360))

        self.main_window = main_window

        self.progress_bar = QtWidgets.QProgressBar(self)
        self.progress_bar.setGeometry(QtCore.QRect(40, 180, 400, 30))
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)

        self.calc = None

    def start_unpacking(self, file1, file2):
        self.calc = External(file1, file2, None, None, None, False)
        self.calc.countChanged.connect(self.progress_bar.setValue)
        self.calc.final.connect(self.final)
        self.calc.start()

    def final(self, info):
        button = QtWidgets.QPushButton(self)
        button.setGeometry(QtCore.QRect(155, 220, 150, 50))
        button.setText('ОК')
        button.setFont(QtGui.QFont('Arial', 20))
        button.clicked.connect(self.exit)
        button.show()

    def exit(self):
        self.hide()
        self.main_window.main_window.show()


class UnpackWindow(QtWidgets.QWidget):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.setGeometry(QtCore.QRect(20, 20, 460, 360))

        self.main_window = main_window

        self.file1 = self.main_window.file_dialog.getOpenFileName()
        self.file2 = self.main_window.file_dialog.getSaveFileName()
        self.main_window.showMinimized()
        self.main_window.showNormal()
        self.bwt_size = 32
        self.sort = 'quick'
        self.smart_rle = True

        label1 = QtWidgets.QLabel(self)
        label1.setGeometry(QtCore.QRect(0, 0, 300, 16))
        label1.setText('Исходный файл')

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setGeometry(QtCore.QRect(0, 20, 300, 25))
        self.button1.setText(self.file1[0])
        self.button1.clicked.connect(self.select_open_file)

        label2 = QtWidgets.QLabel(self)
        label2.setGeometry(QtCore.QRect(0, 50, 300, 16))
        label2.setText('Конечный файл')

        self.button2 = QtWidgets.QPushButton(self)
        self.button2.setGeometry(QtCore.QRect(0, 70, 300, 25))
        self.button2.setText(self.file2[0])
        self.button2.clicked.connect(self.select_save_file)

        button_esc = QtWidgets.QPushButton(self)
        button_esc.setGeometry(QtCore.QRect(0, 250, 150, 50))
        button_esc.setText('Отмена')
        button_esc.setFont(QtGui.QFont('Arial', 18))
        button_esc.clicked.connect(lambda *args: self.main_window.escape())

        button_pack = QtWidgets.QPushButton(self)
        button_pack.setGeometry(QtCore.QRect(170, 250, 150, 50))
        button_pack.setText('Распаковать')
        button_pack.setFont(QtGui.QFont('Arial', 18))
        button_pack.clicked.connect(lambda *args: self.start_unpacking(main_window))

    def select_open_file(self):
        self.file1 = self.main_window.file_dialog.getOpenFileName()
        self.button1.setText(self.file1[0])

    def select_save_file(self):
        self.file2 = self.main_window.file_dialog.getSaveFileName()
        self.button2.setText(self.file2[0])

    def start_unpacking(self, main_window):
        if self.file1[0] == '' or self.file2[0] == '':
            return
        self.hide()
        main_window.progress_window = ProgressWindowUnpack(main_window)
        main_window.progress_window.show()
        main_window.progress_window.start_unpacking(self.file1, self.file2)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
