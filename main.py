from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyle
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,300, 500, 500)
        self.setWindowTitle("Simple Student Information System")
        self.initUI()
    
    def initUI(self):
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("wot")


def main():
    app = QApplication(sys.argv)

    w = MainWindow()
    w.show()

    sys.exit(app.exec_())

main()