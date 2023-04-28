from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFileDialog, QLineEdit, QPushButton, \
    QMessageBox
from logic import mirror_image


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        file_layout = QHBoxLayout()
        self.file_line_edit = QLineEdit()
        self.file_line_edit.setReadOnly(True)
        file_layout.addWidget(self.file_line_edit)

        self.file_button = QPushButton("Выбрать файл")
        self.file_button.setFixedWidth(100)
        self.file_button.clicked.connect(self.select_file)
        file_layout.addWidget(self.file_button)

        layout.addLayout(file_layout)

        self.button_mirror = QPushButton("Зеркалировать")
        self.button_mirror.clicked.connect(self.mirror)
        layout.addWidget(self.button_mirror)

    def select_file(self):
        path = QFileDialog.getOpenFileName(self, "Выберите исходное изображение", filter="Images (*.bmp)")[0]
        if path:
            self.file_line_edit.setText(path)

    def mirror(self):
        if not self.file_line_edit.text():
            QMessageBox.warning(self, "Ошибка", "Выберите исходное изображение.")
        else:
            try:
                path = self.file_line_edit.text()
                new_path = QFileDialog.getSaveFileName(self, "Сохранение изображения", filter="Images (*.bmp)")[0]
                mirror_image(path, new_path)
            except Exception as ex:
                QMessageBox.warning(self, "Ошибка", f"{ex.__class__.__name__}: {ex}")
            else:
                QMessageBox.information(self, "Выполнено", "Изображение успешно зеркалировано и сохранено.")
