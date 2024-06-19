import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import *
from mainwin import Ui_MainWindow
class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWidget()
    sys.exit(app.exec())
    main.close()
    sys.exit(0)