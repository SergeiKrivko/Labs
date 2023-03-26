from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton


class TestEditWidget(QWidget):
    def __init__(self, parent=None):
        super(TestEditWidget, self).__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel("Описание теста"))
        self.test_name_edit = QLineEdit()
        self.test_name_edit.setFont(QFont("Calibri", 10))
        layout.addWidget(self.test_name_edit)

        h_layout = QHBoxLayout()
        layout.addLayout(h_layout)

        layout1 = QVBoxLayout()
        h_layout.addLayout(layout1)
        label = QLabel("Входные данные")
        label.setFixedHeight(20)
        layout1.addWidget(label)
        self.test_in_edit = QTextEdit()
        self.test_in_edit.setFont(QFont("Courier", 10))
        layout1.addWidget(self.test_in_edit)

        layout2 = QVBoxLayout()
        h_layout.addLayout(layout2)
        layout_h2 = QHBoxLayout()
        layout2.addLayout(layout_h2)
        layout_h2.addWidget(QLabel("Выходные данные"))
        self.button_generate = QPushButton()
        self.button_generate.setText("Сгенерировать")
        self.button_generate.setFixedHeight(20)
        layout_h2.addWidget(self.button_generate)
        self.test_out_edit = QTextEdit()
        self.test_out_edit.setFont(QFont("Courier", 10))
        layout2.addWidget(self.test_out_edit)

    def open_test(self, description, data_in, data_out):
        self.test_name_edit.setText(description)
        self.test_in_edit.setText(data_in)
        self.test_out_edit.setText(data_out)
