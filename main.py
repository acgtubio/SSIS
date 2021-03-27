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

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("wot")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MainWindow()
    w.show()

    sys.exit(app.exec_())
