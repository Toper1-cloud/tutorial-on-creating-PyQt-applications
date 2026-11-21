import sys
from PyQt6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QVBoxLayout, QWidget)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Окно с QLineEdit")
        self.resize(500, 350)
        layout1 = QVBoxLayout(self)

        inputs_layout = QHBoxLayout()

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Введите ваше имя...")

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Введите пароль...")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        inputs_layout.addWidget(self.name_input)
        inputs_layout.addWidget(self.password_input)

        layout1.addLayout(inputs_layout)

    def get_inputs(self):
        user_input = self.name_input.text()
        password_input = self.password_input.text()
        return user_input, password_input

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
