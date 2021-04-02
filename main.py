from PyQt5 import QtCore, QtGui, QtWidgets
from csvHandling import getData
import addstudent
import delStudent


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 515)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Table
        self.studentList = QtWidgets.QTableWidget(self.centralwidget)
        self.studentList.setGeometry(QtCore.QRect(20, 20, 550, 461))
        self.studentList.setColumnCount(5)
        self.studentList.setObjectName("studentList")
        self.studentList.setHorizontalHeaderLabels(["ID","Name","Year","Course","Gender"])
        self.studentList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.studentList.setShowGrid(False)

        #Buttons
        self.editInfo = QtWidgets.QPushButton(self.centralwidget)
        self.editInfo.setGeometry(QtCore.QRect(600, 370, 111, 41))
        self.editInfo.setObjectName("editInfo")
        self.editInfo.clicked.connect(self.editInfoClicked)

        self.delStudent = QtWidgets.QPushButton(self.centralwidget)
        self.delStudent.setGeometry(QtCore.QRect(600, 420, 111, 41))
        self.delStudent.setObjectName("delStudent")
        self.delStudent.clicked.connect(self.delStudentClicked)

        self.addStudent = QtWidgets.QPushButton(self.centralwidget)
        self.addStudent.setGeometry(QtCore.QRect(600, 320, 111, 41))
        self.addStudent.setObjectName("addStudent")
        self.addStudent.clicked.connect(self.addStudentClicked)

        self.findStudent = QtWidgets.QPushButton(self.centralwidget)
        self.findStudent.setGeometry(QtCore.QRect(600, 70, 111, 41))
        self.findStudent.setObjectName("findStudent")
        self.findStudent.clicked.connect(self.findStudentInfo)

        self.showList = QtWidgets.QPushButton(self.centralwidget)
        self.showList.setGeometry(QtCore.QRect(600, 20, 111, 41))
        self.showList.setObjectName("showList")
        self.showList.clicked.connect(self.showListClicked)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def findStudentInfo(self):
        self.f = delSt(self, 'f')
        self.f.show()

    def editInfoClicked(self):
        self.e = delSt(self, 'e')
        self.e.show()

    def addStudentClicked(self):
        self.b = addSt(self)
        self.b.show()
        
    def delStudentClicked(self):
        self.d = delSt(self, 'd')
        self.d.show()

    def showListClicked(self):
        students = getData()                                                #from csvHandling file.
        self.studentList.setRowCount(len(students) -1)
        row = 0
        for student in students:
            if student[0] == "id":
                continue
            self.studentList.setItem(row, 0, QtWidgets.QTableWidgetItem(str(student[0])))
            self.studentList.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{str(student[1])}, {str(student[2])} {str(student[3])}"))
            self.studentList.setItem(row, 2, QtWidgets.QTableWidgetItem(str(student[4])))
            self.studentList.setItem(row, 3, QtWidgets.QTableWidgetItem(str(student[5])))
            self.studentList.setItem(row, 4, QtWidgets.QTableWidgetItem(str(student[6])))
            row+=1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Student Information Sytem"))
        self.editInfo.setText(_translate("MainWindow", "Edit Information"))
        self.findStudent.setText(_translate("MainWindow", "Find Student"))
        self.delStudent.setText(_translate("MainWindow", "Delete Student"))
        self.addStudent.setText(_translate("MainWindow", "Add Sudent"))
        self.showList.setText(_translate("MainWindow", "Show All"))

class mainWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class addSt(QtWidgets.QMainWindow, addstudent.Ui_addStudentWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.setupUi(self)

class delSt(QtWidgets.QMainWindow, delStudent.Ui_delStud):
    def __init__(self, parent = None, source = None):
        super().__init__(parent)

        self.setupUi(self, source)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    a = mainWin()
    a.show()

    sys.exit(app.exec_())
