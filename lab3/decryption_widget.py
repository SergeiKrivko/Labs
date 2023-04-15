from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout, QPushButton, QFileDialog, \
    QMessageBox, QTextEdit
from encrypting import decrypt_image


class DecryptionWidget(QWidget):
    def __init__(self):
        super(DecryptionWidget, self).__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        layout.addWidget(QLabel("Изображение"))
        file_layout = QHBoxLayout()
        file_layout.setSpacing(0)
        layout.addLayout(file_layout)

        self.file_line_edit = QLineEdit()
        file_layout.addWidget(self.file_line_edit)

        self.file_button = QPushButton("Обзор")
        self.file_button.clicked.connect(self.open_file)
        file_layout.addWidget(self.file_button)

        self.button_encrypt = QPushButton("Расшифровать")
        self.button_encrypt.setFixedWidth(200)
        layout.addWidget(self.button_encrypt)
        self.button_encrypt.clicked.connect(self.decrypt)

        layout.addWidget(QLabel("Результат:"))
        self.output_line = QTextEdit()
        self.output_line.setReadOnly(True)
        layout.addWidget(self.output_line)

    def open_file(self):
        self.file_line_edit.setText(QFileDialog.getOpenFileName(caption="Выберите исходное изображение",
                                                                filter="Images (*.bmp; *.png; *.jpg)")[0])

    def decrypt(self):
        try:
            res = decrypt_image(self.file_line_edit.text())
            self.output_line.setText(res)
        except OverflowError:
            QMessageBox.warning(self, "Ошибка", "Невозможно расшифровать данное изображение")
        except UnicodeDecodeError:
            QMessageBox.warning(self, "Ошибка", "Невозможно расшифровать данное изображение")
        except Exception as ex:
            QMessageBox.warning(self, "Ошибка", f"{ex.__class__.__name__}: {ex}")

