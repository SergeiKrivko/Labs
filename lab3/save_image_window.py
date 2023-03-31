from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QLineEdit, QPushButton, QFileDialog


class SaveImageWindow(QMainWindow):
    def __init__(self):
        super(SaveImageWindow, self).__init__()
        self.pixmap = None
        self.image = None

        layout = QVBoxLayout()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(layout)

        layout.addWidget(QLabel("Изображение"))
        file_layout = QHBoxLayout()
        file_layout.setSpacing(0)
        layout.addLayout(file_layout)

        self.file_line_edit = QLineEdit()
        file_layout.addWidget(self.file_line_edit)

        self.file_button = QPushButton("Обзор")
        self.file_button.clicked.connect(self.select_file)
        file_layout.addWidget(self.file_button)

        self.image_widget = QLabel()
        layout.addWidget(self.image_widget)

        self.button_save = QPushButton("Сохранить")
        self.button_save.clicked.connect(self.save_image)
        layout.addWidget(self.button_save)

    def open_image(self, image):
        self.image = image
        self.pixmap = image.toqpixmap()
        # self.image_widget.setPixmap(self.pixmap)
        self.show()

    def select_file(self):
        self.file_line_edit.setText(QFileDialog.getSaveFileName(caption="Сохранение изображения",
                                                                filter="BMP (*.bmp)\n JPG (*.jpg)\n PNG (*.png)")[0])

    def save_image(self):
        self.image.save(self.file_line_edit.text())
        self.hide()
