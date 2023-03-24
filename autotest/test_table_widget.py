from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QListWidget, QListWidgetItem, QLabel


class TestTableWidget(QWidget):
    def __init__(self):
        super(TestTableWidget, self).__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)
        pos_layout = QVBoxLayout()
        layout.addLayout(pos_layout)

        pos_buttons_layout = QHBoxLayout()
        pos_layout.addLayout(pos_buttons_layout)
        pos_buttons_layout.addWidget(QLabel("Позитивные тесты"))

        self.pos_add_button = QPushButton()
        self.pos_add_button.setText("+")
        pos_buttons_layout.addWidget(self.pos_add_button)

        self.pos_delete_button = QPushButton()
        self.pos_delete_button.setText("X")
        pos_buttons_layout.addWidget(self.pos_delete_button)

        self.pos_test_list = QListWidget()
        pos_layout.addWidget(self.pos_test_list)

        neg_layout = QVBoxLayout()
        layout.addLayout(neg_layout)

        neg_buttons_layout = QHBoxLayout()
        neg_layout.addLayout(neg_buttons_layout)
        neg_buttons_layout.addWidget(QLabel("Негативные тесты"))

        self.neg_add_button = QPushButton()
        self.neg_add_button.setText("+")
        neg_buttons_layout.addWidget(self.neg_add_button)

        self.neg_delete_button = QPushButton()
        self.neg_delete_button.setText("X")
        neg_buttons_layout.addWidget(self.neg_delete_button)

        self.neg_test_list = QListWidget()
        neg_layout.addWidget(self.neg_test_list)

    def update_pos_items(self, item_list):
        self.pos_test_list.clear()
        for i in range(len(item_list)):
            self.pos_test_list.addItem(QListWidgetItem(item_list[i]))

    def update_neg_items(self, item_list):
        self.neg_test_list.clear()
        for i in range(len(item_list)):
            self.neg_test_list.addItem(QListWidgetItem(item_list[i]))

