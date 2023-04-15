from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QComboBox, QVBoxLayout, QWidget
from encryption_widget import EncryptionWidget
from decryption_widget import DecryptionWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.resize(600, 400)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        layout.setAlignment(Qt.AlignTop)

        self.mode_widget = QComboBox()
        self.mode_widget.addItems(['Сокрытие строки', 'Извлечение строки'])
        self.mode_widget.setFixedWidth(150)
        layout.addWidget(self.mode_widget)
        self.mode_widget.currentIndexChanged.connect(self.change_mode)

        self.encryption_widget = EncryptionWidget()
        layout.addWidget(self.encryption_widget)

        self.decryption_widget = DecryptionWidget()
        self.decryption_widget.hide()
        layout.addWidget(self.decryption_widget)

    def change_mode(self, index):
        if index == 0:
            self.decryption_widget.hide()
            self.encryption_widget.show()
        elif index == 1:
            self.encryption_widget.hide()
            self.decryption_widget.show()
