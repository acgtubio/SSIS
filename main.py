from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(898, 515)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Table
        self.studentList = QtWidgets.QTableWidget(self.centralwidget)
        self.studentList.setGeometry(QtCore.QRect(20, 20, 711, 461))
        self.studentList.setColumnCount(5)
        self.studentList.setObjectName("studentList")
        self.studentList.setRowCount(0)
        self.studentList.setHorizontalHeaderLabels(["ID","Name","Course","Year","Gender"])

        #Buttons
        self.editInfo = QtWidgets.QPushButton(self.centralwidget)
        self.editInfo.setGeometry(QtCore.QRect(760, 370, 111, 41))
        self.editInfo.setObjectName("editInfo")
        self.editInfo.clicked.connect(self.editInfoClicked)

        self.delStudent = QtWidgets.QPushButton(self.centralwidget)
        self.delStudent.setGeometry(QtCore.QRect(760, 420, 111, 41))
        self.delStudent.setObjectName("delStudent")
        self.delStudent.clicked.connect(self.delStudentClicked)

        self.addStudent = QtWidgets.QPushButton(self.centralwidget)
        self.addStudent.setGeometry(QtCore.QRect(760, 320, 111, 41))
        self.addStudent.setObjectName("addStudent")
        self.addStudent.clicked.connect(self.addStudentClicked)

        self.showList = QtWidgets.QPushButton(self.centralwidget)
        self.showList.setGeometry(QtCore.QRect(760, 20, 111, 41))
        self.showList.setObjectName("showList")
        self.showList.clicked.connect(self.showListClicked)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def editInfoClicked(self):
        pass

    def addStudentClicked(self):
        pass

    def delStudentClicked(self):
        pass

    def showListClicked(self):
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Student Information Sytem"))
        self.editInfo.setText(_translate("MainWindow", "Edit Information"))
        self.delStudent.setText(_translate("MainWindow", "Delete Student"))
        self.addStudent.setText(_translate("MainWindow", "Add Sudent"))
        self.showList.setText(_translate("MainWindow", "Show List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
