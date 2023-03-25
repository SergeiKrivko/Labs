import os

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTextEdit
from options_window import OptionsWidget


class CodeWidget(QWidget):
    def __init__(self, settings):
        super(CodeWidget, self).__init__()
        self.settings = settings

        layout = QHBoxLayout()
        self.setLayout(layout)
        layout_left = QVBoxLayout()
        layout.addLayout(layout_left)

        self.options_widget = OptionsWidget({
            'Номер лабы:': {'type': int, 'min': 1, 'initial': self.settings.get('lab', 1),
                            'name': OptionsWidget.NAME_LEFT},
            'Номер задания:': {'type': int, 'min': 1, 'initial': self.settings.get('task', 1),
                               'name': OptionsWidget.NAME_LEFT},
            'Номер варианта:': {'type': int, 'min': 0, 'initial': self.settings.get('var', 0),
                                'name': OptionsWidget.NAME_LEFT},
            'Тестировать': {'type': 'button', 'text': 'Тестировать', 'name': OptionsWidget.NAME_SKIP}
        })
        # self.options_widget.clicked.connect(self.option_changed)
        layout_left.addWidget(self.options_widget)

        self.code_edit = QTextEdit()
        self.code_edit.setFont(QFont("Courier", 10))
        layout.addWidget(self.code_edit)
        self.path = ''

    def option_changed(self, key):
        if key in ('Номер лабы:', 'Номер задания:'):
            self.settings['lab'] = self.options_widget["Номер лабы:"]
            self.settings['task'] = self.options_widget["Номер задания:"]
            for i in range(100):
                if os.path.isdir(self.settings['path'] + f"/lab_{self.options_widget['Номер лабы:']:0>2}_" \
                                                         f"{self.options_widget['Номер задания:']:0>2}_{i:0>2}"):
                    self.options_widget.set_value('Номер варианта:', i)
                    break
            self.open_code()
        elif key == 'Номер варианта:':
            self.settings['var'] = self.options_widget["Номер варианта:"]
            self.open_code()

    def update_options(self):
        self.options_widget.set_value('Номер лабы:', self.settings.get('lab', self.options_widget['Номер лабы:']))
        self.options_widget.set_value('Номер задания:',
                                      self.settings.get('task', self.options_widget['Номер задания:']))
        self.options_widget.set_value('Номер варианта:',
                                      self.settings.get('var', self.options_widget['Номер варианта:']))

    def open_code(self):
        self.path = self.settings['path'] + f"/lab_{self.options_widget['Номер лабы:']:0>2}_" \
                                            f"{self.options_widget['Номер задания:']:0>2}_" \
                                            f"{self.options_widget['Номер варианта:']:0>2}"
        try:
            self.code_edit.setText("")
            file = open(f"{self.path}/main.c")
            self.code_edit.setText(file.read())
            file.close()
        except Exception as ex:
            print(f"{ex.__class__.__name__}: {ex}")

    def save_code(self):
        code = self.code_edit.toPlainText()
        if code:
            file = open(f"{self.path}/main.c", 'w', encoding='utf=8')
            file.write(code)
            file.close()

    def show(self) -> None:
        self.update_options()
        self.open_code()
        super(CodeWidget, self).show()

    def hide(self):
        self.save_code()
        super(CodeWidget, self).hide()
