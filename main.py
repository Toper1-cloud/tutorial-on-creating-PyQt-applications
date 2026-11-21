import sys
from PyQt6.QtWidgets import (QApplication, QWidget)
class MainWindow(QWidget) :
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle('Окно на PyQt6')
        self.resize(500, 350)


if __name__ == "__main__":
    арр = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(арр.exec())
