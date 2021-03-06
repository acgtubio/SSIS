from typing import Text
from PyQt5 import QtCore, QtGui, QtWidgets
from dbHandling import DBHandling
from MessageBox import MessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, parent, mode = "a", id = None):
        self.mode = mode
        self.parent = parent
        self.srcID = id
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(461, 274)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.headerLabel = QtWidgets.QLabel(self.centralwidget)
        self.headerLabel.setGeometry(QtCore.QRect(30, 30, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(30)
        self.headerLabel.setFont(font)
        self.headerLabel.setObjectName("headerLabel")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 90, 401, 101))
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.ccLabel = QtWidgets.QLabel(self.frame)
        self.ccLabel.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.ccLabel.setObjectName("ccLabel")
        self.cnLabel = QtWidgets.QLabel(self.frame)
        self.cnLabel.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.cnLabel.setObjectName("cnLabel")

        # Input Fields
        self.courseCode = QtWidgets.QLineEdit(self.frame)
        self.courseCode.setGeometry(QtCore.QRect(140, 20, 251, 20))
        self.courseCode.setObjectName("courseCode")

        self.courseName = QtWidgets.QLineEdit(self.frame)
        self.courseName.setGeometry(QtCore.QRect(140, 70, 251, 20))
        self.courseName.setObjectName("courseName")

        # Submit
        self.addCourseButton = QtWidgets.QPushButton(self.centralwidget)
        self.addCourseButton.setGeometry(QtCore.QRect(320, 200, 101, 31))
        self.addCourseButton.setObjectName("addCourseButton")
        self.addCourseButton.clicked.connect(self.__submitClicked)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        if self.mode == "e":
            self.__editStateUI()

    def __submitClicked(self):
        data = DBHandling.getCourseData(f"WHERE course_code = \'{self.courseCode.text()}\'")
        if data != [] and self.mode == "a":
            MessageBox.showInformationMessage(f"Course Code {self.courseCode.text()} already taken.", "Error")
            return

        if self.courseCode.text() == "" or self.courseName == "":
            MessageBox.showInformationMessage("No fields must be empty.", "Error")
            return
        
        txt = "Add Course?" if self.mode == "a" else "Update Course Information?"
        m = MessageBox.showConfirmationMessage(txt, "Confirmation")

        if m == QtWidgets.QMessageBox.Yes:
            if self.mode == "a":
                DBHandling.pushCourseData((self.courseCode.text(), self.courseName.text()))
                MessageBox.showInformationMessage("Course added.", "Information")
                self.__resetUI()
            else:
                DBHandling.updateCourseData((self.courseName.text(), self.srcID))
                MessageBox.showInformationMessage("Course updated.", "Information")

        self.parent.showCourseList()

    def __resetUI(self):
        self.courseName.setText("")
        self.courseCode.setText("")
    
    def __editStateUI(self):
        data = DBHandling.getCourseData(f"WHERE course_code = \'{self.srcID}\'")
        self.courseCode.setEnabled(False)
        self.courseCode.setText(data[0][0])
        self.courseName.setText(data[0][1])
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Course"))
        self.headerLabel.setText(_translate("MainWindow", "Course"))
        self.ccLabel.setText(_translate("MainWindow", "Course Code:"))
        self.cnLabel.setText(_translate("MainWindow", "Course Name:"))
        txt = "Add Course" if self.mode == "a" else "Edit Information"
        self.addCourseButton.setText(QtCore.QCoreApplication.translate("MainWindow", txt))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
