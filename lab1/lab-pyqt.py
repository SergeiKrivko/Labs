"""
Кривко Сергей Евгеньевич, ИУ7-24Б
Данная программа позволяет переводить числа из десятичной системы счисления в восмеричную и обратно.
"""

from PyQt5 import QtWidgets, QtGui, QtCore
import convert_numbers


class MainWindow(QtWidgets.QMainWindow):
    """Главное окно"""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(640, 400)
        self.setWindowTitle('Лабораторная работа №1')

        self.convert_widget = ConvertWidget(self)
        self.convert_widget.setGeometry(0, 40, 640, 160)

        self.keyboard = Keyboard(self)
        self.keyboard.setGeometry(70, 200, 500, 150)

        self.keyboard.keyboard_signal.connect(self.convert_widget.keyboard_button_pressed)

        self.menu = Menu(self)
        self.menu.setGeometry(0, 0, 640, 30)
        self.menu.menu_signal.connect(self.convert_widget.menu_button_pressed)

    def keyPressEvent(self, a0):
        if a0.key() == 16777220:
            self.convert_widget.convert()


class ConvertWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(ConvertWidget, self).__init__(parent)

        self.input_widget = QtWidgets.QLineEdit(self)
        self.input_widget.setGeometry(240, 15, 300, 50)
        self.input_widget.setFont(QtGui.QFont('Arial', 20))
        self.input_widget.setClearButtonEnabled(True)
        self.input_widget.textChanged.connect(lambda *args: self.error_label.hide())

        self.output_widget = QtWidgets.QLineEdit(self)
        self.output_widget.setGeometry(240, 95, 300, 35)
        self.output_widget.setFont(QtGui.QFont('Arial', 16))
        self.output_widget.setReadOnly(True)

        self.mode_combo_box = QtWidgets.QComboBox(self)
        self.mode_combo_box.addItems(('10сс → 8сс', '8сс → 10сс'))
        self.mode_combo_box.setFont(QtGui.QFont('Arial', 14))
        self.mode_combo_box.setGeometry(50, 60, 150, 40)

        self.error_label = QtWidgets.QLabel(self)
        self.error_label.setText('Некорректное число')
        self.error_label.setGeometry(240, 65, 200, 20)
        self.error_label.setStyleSheet('color: red')
        self.error_label.hide()

    def convert(self):
        """Перевод числа"""
        if self.mode_combo_box.currentIndex() == 0:
            self.convert_from_10_to_8()
        else:
            self.convert_from_8_to_10()

    def convert_from_10_to_8(self):
        """Перевод числа из 10сс в 8сс"""
        if self.input_widget.text() == '':
            self.output_widget.setText('')
        else:
            try:
                self.output_widget.setText(convert_numbers.from_dec_to_oct(float(self.input_widget.text())))
            except ValueError:
                self.error_label.show()
            except Exception:
                print('Неизвестная ошибка')
                self.error_label.show()

    def convert_from_8_to_10(self):
        """Перевод числа из 8сс в 10сс"""
        if self.input_widget.text() == '':
            self.output_widget.setText('')
        elif convert_numbers.number_is_oct(self.input_widget.text()):
            self.output_widget.setText(str(convert_numbers.from_oct_to_dec(self.input_widget.text())))
        else:
            self.error_label.show()

    def keyboard_button_pressed(self, symbol):
        if symbol == '←':
            self.input_widget.backspace()
        elif symbol == '=':
            self.convert()
        else:
            self.input_widget.insert(symbol)

    def menu_button_pressed(self, button):
        if button == '10':
            self.convert_from_10_to_8()
        elif button == '8':
            self.convert_from_8_to_10()
        elif button == 'clear':
            self.input_widget.clear()
            self.output_widget.clear()


class Keyboard(QtWidgets.QWidget):
    keyboard_signal = QtCore.pyqtSignal(str)

    def __init__(self, parent):
        super(Keyboard, self).__init__(parent)

        layout = QtWidgets.QGridLayout(self)
        symbols = '1234567890.-←='
        for i in range(len(symbols)):
            button = QtWidgets.QPushButton(symbols[i], self)
            button.setFont(QtGui.QFont('Arial', 20))
            button.setFixedSize(60, 60)
            self.connect_button(button, symbols[i])
            layout.addWidget(button, i % 2, i // 2)

    def connect_button(self, button, symbol):
        button.clicked.connect(lambda *args: self.keyboard_signal.emit(symbol))


class Menu(QtWidgets.QMenuBar):
    menu_signal = QtCore.pyqtSignal(str)

    def __init__(self, parent):
        super(Menu, self).__init__(parent)
        self.setFont(QtGui.QFont('Arial', 14))

        menu = self.addMenu('&Меню')

        action = QtWidgets.QAction('&10сс → 8сс', self)
        action.triggered.connect(lambda *args: self.menu_signal.emit('10'))
        menu.addAction(action)

        action = QtWidgets.QAction('&8сс → 10сс', self)
        action.triggered.connect(lambda *args: self.menu_signal.emit('8'))
        menu.addAction(action)

        action = QtWidgets.QAction('&Очистить', self)
        action.triggered.connect(lambda *args: self.menu_signal.emit('clear'))
        menu.addAction(action)

        action = QtWidgets.QAction('&Информация', self)
        action.triggered.connect(lambda *args: self.show_info())
        menu.addAction(action)

    def show_info(self):
        text = "Данная программа позволяет переводить числа из десятичной системы счисления в восмеричную и " \
                "обратно.\n\n" \
                "Разработчик: Кривко Сергей Евгеньевич, ИУ7-24Б"
        QtWidgets.QMessageBox.information(self, 'Информация об авторе и назначении программы', text)


def main():
    app = QtWidgets.QApplication([])
    main_window = MainWindow()
    main_window.show()

    app.exec_()


if __name__ == '__main__':
    main()
