from PyQt5.QtWidgets import QTextEdit, QLineEdit, QWidget, QVBoxLayout


class TestEditWidget(QWidget):
    def __init__(self, parent=None):
        super(TestEditWidget, self).__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.test_name_edit = QLineEdit()
        layout.addWidget(self.test_name_edit)

        self.test_edit = QTextEdit()
        layout.addWidget(self.test_edit)

    def open_test(self, description, data):
        self.test_name_edit.setText(description)
        self.test_edit.setText(data)
