import sys
from PyQt6.QtWidgets import (QApplication, QLabel, QVBoxLayout, QHBoxLayout, QWidget)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Окно на PyQt6")
        self.resize(500, 350)

        layout = QHBoxLayout(self)
        label = QLabel("Хай!")
        layout.addWidget(label)

        label2 = QLabel("new")
        label3 = QLabel("Пример")

        layout.addWidget(label2)
        layout.addWidget(label3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
