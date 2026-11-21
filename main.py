import sys
from PyQt6.QtWidgets import QApplication, QWidget

арр = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Первое окно')
window.resize(400, 300)

window.show()
sys.exit(арр.exec())
