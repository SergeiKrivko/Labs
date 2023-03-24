from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QApplication, QTextEdit, QMessageBox
from options_window import OptionsWidget
from test_table_widget import TestTableWidget
from test_edit_widget import TestEditWidget
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
        layout = QHBoxLayout()
        layout1 = QVBoxLayout()
        layout.addLayout(layout1)

        self.options_widget = OptionsWidget({
            'Рабочая папка:': {'type': 'file', 'mode': 'dir', 'width': 300,
                               'directory': self.settings.get('path', os.getcwd()),
                               'initial': self.settings.get('path', os.getcwd())},
            'Номер лабы:': {'type': int, 'min': 1, 'initial': self.settings.get('lab', 1),
                            'name': OptionsWidget.NAME_LEFT},
            'Номер задания:': {'type': int, 'min': 1, 'initial': self.settings.get('task', 1),
                               'name': OptionsWidget.NAME_LEFT},
            'Номер варианта:': {'type': int, 'min': 0, 'initial': self.settings.get('var', 0),
                                'name': OptionsWidget.NAME_LEFT},
            'Входные данные:': {'type': str, 'initial': '-', 'width': 300},
            'Выходные данные:': {'type': str, 'initial': '-', 'width': 300},
            'Сохранить': {'type': 'button', 'text': 'Сохранить', 'name': OptionsWidget.NAME_SKIP}
        })
        self.options_widget.clicked.connect(self.option_changed)
        layout1.addWidget(self.options_widget)

        self.code_widget = QTextEdit()
        self.code_widget.setReadOnly(True)
        layout1.addWidget(self.code_widget)

        layout2 = QVBoxLayout()
        layout.addLayout(layout2)

        self.test_list_widget = TestTableWidget()
        self.test_list_widget.setMinimumWidth(400)
        self.test_list_widget.setMinimumHeight(150)
        self.test_list_widget.pos_add_button.clicked.connect(self.add_pos_test)
        self.test_list_widget.pos_delete_button.clicked.connect(self.delete_pos_test)
        self.test_list_widget.neg_add_button.clicked.connect(self.add_neg_test)
        self.test_list_widget.neg_delete_button.clicked.connect(self.delete_neg_test)
        self.test_list_widget.pos_test_list.itemSelectionChanged.connect(self.select_pos_test)
        self.test_list_widget.neg_test_list.itemSelectionChanged.connect(self.select_neg_test)
        layout2.addWidget(self.test_list_widget)

        self.test_edit_widget = TestEditWidget()
        self.test_edit_widget.setMinimumHeight(300)
        self.test_edit_widget.test_name_edit.textChanged.connect(self.set_test_name)
        self.test_edit_widget.test_edit.textChanged.connect(self.set_test_data)
        layout2.addWidget(self.test_edit_widget)

        central_widget.setLayout(layout)

        self.pos_tests = []
        self.neg_tests = []
        self.selected_test = 'pos'

        self.path = ''
        self.open_tests()

    def option_changed(self, key):
        if key == 'Сохранить':
            self.save_tests()
        elif key in ('Номер лабы:', 'Номер задания:', 'Номер варианта:', 'Рабочая папка:'):
            self.open_tests()

    def add_pos_test(self):
        self.pos_tests.append(['-', ''])
        self.test_list_widget.update_pos_items([item[0] for item in self.pos_tests])

    def add_neg_test(self):
        self.neg_tests.append(['-', ''])
        self.test_list_widget.update_neg_items([item[0] for item in self.neg_tests])

    def delete_pos_test(self):
        if len(self.pos_tests) == 0:
            return
        ind = self.test_list_widget.pos_test_list.currentRow()
        self.pos_tests.pop(ind)
        self.test_list_widget.update_pos_items([item[0] for item in self.pos_tests])
        self.test_list_widget.pos_test_list.setCurrentRow(ind if ind < len(self.pos_tests) else ind - 1)

    def delete_neg_test(self):
        if len(self.neg_tests) == 0:
            return
        ind = self.test_list_widget.neg_test_list.currentRow()
        self.neg_tests.pop(ind)
        self.test_list_widget.update_neg_items([item[0] for item in self.neg_tests])
        self.test_list_widget.neg_test_list.setCurrentRow(ind if ind < len(self.neg_tests) else ind - 1)

    def select_pos_test(self):
        self.test_list_widget.neg_test_list.setCurrentItem(None)
        try:
            self.test_edit_widget.open_test(*self.pos_tests[self.test_list_widget.pos_test_list.currentRow()])
        except IndexError:
            pass

    def select_neg_test(self):
        self.test_list_widget.pos_test_list.setCurrentItem(None)
        try:
            self.test_edit_widget.open_test(*self.neg_tests[self.test_list_widget.neg_test_list.currentRow()])
        except IndexError:
            pass

    def set_test_name(self, name):
        if self.test_list_widget.pos_test_list.currentItem() is not None:
            self.pos_tests[self.test_list_widget.pos_test_list.currentRow()][0] = name
            self.test_list_widget.pos_test_list.currentItem().setText(name)
        elif self.test_list_widget.neg_test_list.currentItem() is not None:
            self.neg_tests[self.test_list_widget.neg_test_list.currentRow()][0] = name
            self.test_list_widget.neg_test_list.currentItem().setText(name)

    def set_test_data(self):
        if self.test_list_widget.pos_test_list.currentItem() is not None:
            self.pos_tests[self.test_list_widget.pos_test_list.currentRow()][1] = \
                self.test_edit_widget.test_edit.toPlainText()
        elif self.test_list_widget.neg_test_list.currentItem() is not None:
            self.neg_tests[self.test_list_widget.neg_test_list.currentRow()][1] = \
                self.test_edit_widget.test_edit.toPlainText()

    def open_tests(self):
        self.path = self.options_widget['Рабочая папка:'] + f"/lab_{self.options_widget['Номер лабы:']:0>2}_" \
                            f"{self.options_widget['Номер задания:']:0>2}_" \
                            f"{self.options_widget['Номер варианта:']:0>2}"
        try:
            self.code_widget.setMarkdown("")
            file = open(f"{self.path}/main.c")
            self.code_widget.setMarkdown(f"```c\n{file.read()}\n```")
            file.close()
        except Exception as ex:
            print(f"{ex.__class__.__name__}: {ex}")
        self.readme_parser()
        self.test_list_widget.update_pos_items([item[0] for item in self.pos_tests])
        self.test_list_widget.update_neg_items([item[0] for item in self.neg_tests])

    def readme_parser(self):
        self.pos_tests.clear()
        self.neg_tests.clear()

        if not os.path.isfile(f"{self.path}/func_tests/readme.md"):
            return
        file = open(f"{self.path}/func_tests/readme.md", encoding='utf-8')
        lines = file.readlines()
        file.close()
        self.options_widget.set_value("Входные данные:", "-")
        self.options_widget.set_value("Выходные данные:", "-")

        for i in range(len(lines)):
            if "Позитивные тесты" in lines[i]:
                for j in range(i + 1, len(lines)):
                    if lines[j][:2] == '- ' and lines[j][4:7] == ' - ':
                        self.pos_tests.append([lines[j][7:].strip(), ''])
                    else:
                        break

            elif "Негативные тесты" in lines[i]:
                for j in range(i + 1, len(lines)):
                    if lines[j][:2] == '- ' and lines[j][4:7] == ' - ':
                        self.neg_tests.append([lines[j][7:].strip(), ''])
                    else:
                        break

            elif "Входные данные" in lines[i]:
                self.options_widget.set_value("Входные данные:", lines[i + 1].strip())

            elif "Выходные данные" in lines[i]:
                self.options_widget.set_value("Выходные данные:", lines[i + 1].strip())

        for i in range(len(self.pos_tests)):
            if os.path.isfile(f"{self.path}/func_tests/data/pos_{i + 1:0>2}_in.txt"):
                file = open(f"{self.path}/func_tests/data/pos_{i + 1:0>2}_in.txt")
                self.pos_tests[i][1] = file.read()
                file.close()

        for i in range(len(self.neg_tests)):
            if os.path.isfile(f"{self.path}/func_tests/data/neg_{i + 1:0>2}_in.txt"):
                file = open(f"{self.path}/func_tests/data/neg_{i + 1:0>2}_in.txt")
                self.neg_tests[i][1] = file.read()
                file.close()

    def generate_test(self, index, type='pos'):
        os.makedirs(f"{self.path}/func_tests/data", exist_ok=True)

        tests = self.pos_tests if type == 'pos' else self.neg_tests
        file_in = open(f"{self.path}/func_tests/data/{type}_{index + 1:0>2}_in.txt", "w")
        file_in.write(tests[index][1])
        file_in.close()

        os.system(f"{self.path}/app.exe < {self.path}/func_tests/data/{type}_{index + 1:0>2}_in.txt > "
                  f"{self.path}/func_tests/data/{type}_{index + 1:0>2}_out.txt")

    def save_tests(self):
        try:
            os.system(f"gcc -std=c99 -Wall -Werror -Wvla {self.path}/main.c -o {self.path}/app.exe -lm")

            readme = open(f"{self.path}/func_tests/readme.md", 'w', encoding='utf-8')
            readme.write(f"# Тесты для лабораторной работы №{self.options_widget['Номер лабы:']:0>2}, задания №"
                         f"{self.options_widget['Номер задания:']:0>2}\n\n"
                         f"## Входные данные\n{self.options_widget['Входные данные:']}\n\n"
                         f"## Выходные данные\n{self.options_widget['Выходные данные:']}\n\n"
                         f"## Позитивные тесты:\n")
            for i in range(len(self.pos_tests)):
                readme.write(f"- {i + 1:0>2} - {self.pos_tests[i][0]}\n")
                self.generate_test(i, 'pos')

            readme.write("\n## Негативные тесты:\n")

            for i in range(len(self.neg_tests)):
                readme.write(f"- {i + 1:0>2} - {self.neg_tests[i][0]}\n")
                self.generate_test(i, 'neg')
        except Exception as ex:
            QMessageBox.warning(self, 'Error', f"{ex.__class__.__name__}: {ex}")

    def closeEvent(self, a0):
        self.settings['path'] = self.options_widget["Рабочая папка:"]
        self.settings['lab'] = self.options_widget["Номер лабы:"]
        self.settings['task'] = self.options_widget["Номер задания:"]
        self.settings['var'] = self.options_widget["Номер варианта:"]

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
