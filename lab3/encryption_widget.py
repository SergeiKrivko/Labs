from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout, QPushButton, QFileDialog, \
    QMessageBox, QTextEdit
from encrypting import encrypt


class EncryptionWidget(QWidget):
    def __init__(self):
        super(EncryptionWidget, self).__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        layout.addWidget(QLabel("Входной текст"))
        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        layout.addWidget(QLabel("Изображение"))
        file_layout = QHBoxLayout()
        file_layout.setSpacing(0)
        layout.addLayout(file_layout)

        self.file_line_edit = QLineEdit()
        file_layout.addWidget(self.file_line_edit)

        self.file_button = QPushButton("Обзор")
        self.file_button.clicked.connect(self.open_file)
        file_layout.addWidget(self.file_button)

        self.button_encrypt = QPushButton("Зашифровать")
        self.button_encrypt.setFixedWidth(200)
        layout.addWidget(self.button_encrypt)
        self.button_encrypt.clicked.connect(self.encrypt)

    def open_file(self):
        self.file_line_edit.setText(QFileDialog.getOpenFileName(caption="Выберите исходное изображение",
                                                                filter="Images (*.bmp; *.png)")[0])

    def encrypt(self):
        text = self.text_edit.toPlainText()
        if not text:
            QMessageBox.warning(self, "Ошибка", "Введите текст для шифрования.")
        elif not self.file_line_edit.text():
            QMessageBox.warning(self, "Ошибка", "Выберите изображение.")
        else:
            try:
                path = QFileDialog.getSaveFileName(caption="Сохранение изображения",
                                                   filter="BMP (*.bmp)\n PNG (*.png)")[0]
                encrypt(text, self.file_line_edit.text(), path)

            except OverflowError:
                QMessageBox.warning(self, "Ошибка", "Слишком длинная строка для данного изображения.")
            except Exception as ex:
                QMessageBox.warning(self, "Ошибка", f"{ex.__class__.__name__}: {ex}")

            QMessageBox.information(self, "Выполнено", "Текст успешно зашифрован.")
