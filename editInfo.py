from PyQt5 import QtCore, QtGui, QtWidgets
from csvHandling import pushData, getData


# WILL PROBABLY CHANGE delStudent.py TO ACCOMODATE EDIT INFO

class Ui_delStud(object):
    def setupUi(self, delStud):
        delStud.setObjectName("delStud")
        delStud.resize(398, 347)
        self.centralwidget = QtWidgets.QWidget(delStud)
        self.centralwidget.setObjectName("centralwidget")
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(20, 30, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.l1.setFont(font)
        self.l1.setObjectName("l1")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 80, 351, 211))
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        #Labels
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 51, 21))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 51, 31))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 51, 31))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 61, 31))
        self.label_5.setObjectName("label_5")
        
        #Read-only LineEdits
        font.setPointSize(8)
        self.idCheck = QtWidgets.QLineEdit(self.frame)
        self.idCheck.setGeometry(QtCore.QRect(100, 20, 161, 20))
        self.idCheck.setFont(font)
        self.idCheck.setObjectName("idCheck")

        self.nameRE = QtWidgets.QLineEdit(self.frame)
        self.nameRE.setGeometry(QtCore.QRect(100, 60, 161, 20))
        self.nameRE.setFont(font)
        self.nameRE.setObjectName("nameRE")
        self.nameRE.setEnabled(False)
        
        self.yrRE = QtWidgets.QLineEdit(self.frame)
        self.yrRE.setGeometry(QtCore.QRect(100, 100, 161, 20))
        self.yrRE.setFont(font)
        self.yrRE.setObjectName("yrRE")
        self.yrRE.setEnabled(False)

        self.courseRE = QtWidgets.QLineEdit(self.frame)
        self.courseRE.setGeometry(QtCore.QRect(100, 130, 161, 20))
        self.courseRE.setFont(font)
        self.courseRE.setObjectName("courseRE")
        self.courseRE.setEnabled(False)

        self.genderRE = QtWidgets.QLineEdit(self.frame)
        self.genderRE.setGeometry(QtCore.QRect(100, 170, 161, 20))
        self.genderRE.setFont(font)
        self.genderRE.setObjectName("genderRE")
        self.genderRE.setEnabled(False)


        #buttons
        self.recordCheck = QtWidgets.QPushButton(self.frame)
        self.recordCheck.setGeometry(QtCore.QRect(270, 20, 81, 23))
        self.recordCheck.setFont(font)
        self.recordCheck.setObjectName("recordCheck")

        self.delButton = QtWidgets.QPushButton(self.centralwidget)
        self.delButton.setGeometry(QtCore.QRect(270, 300, 101, 31))
        self.delButton.setObjectName("delButton")

        delStud.setCentralWidget(self.centralwidget)

        self.retranslateUi(delStud)
        QtCore.QMetaObject.connectSlotsByName(delStud)

        #MessageBox for alerts
        self.cAlert = QtWidgets.QMessageBox()
        self.cAlert.setIcon(QtWidgets.QMessageBox.Information)
        self.cAlert.setStandardButtons(QtWidgets.QMessageBox.Ok)

    def checkID(self):
        self.cAlert.setWindowTitle("Alert")

        if(self.idCheck.text() != ""):
            self.studList = getData()
            found = 0
            for student in self.studList:
                if student[0] == self.idCheck.text():                               #compares IDs. If true, set Read-only line edits to its corresponding information.
                    self.delID = student[0]
                    found = 1
                    self.nameRE.setText(f"{student[1]}, {student[2]} {student[3]}")
                    self.yrRE.setText(f"{student[4]}")
                    self.courseRE.setText(f"{student[5]}")
                    self.genderRE.setText(f"{student[6]}")

                    self.delButton.setEnabled(True)
            if(not found):
                self.cAlert.setText("ID not found.")
                a = self.cAlert.exec_()
        else:
            self.cAlert.setText("Enter ID #")
            a = self.cAlert.exec_()

    def retranslateUi(self, delStud):
        _translate = QtCore.QCoreApplication.translate
        delStud.setWindowTitle(_translate("delStud", "Delete Student"))
        self.l1.setText(_translate("delStud", "Delete Student"))
        self.label.setText(_translate("delStud", "Enter ID #:"))
        self.recordCheck.setText(_translate("delStud", "Check Record"))
        self.label_2.setText(_translate("delStud", "Name:"))
        self.label_3.setText(_translate("delStud", "Year:"))
        self.label_4.setText(_translate("delStud", "Course:"))
        self.label_5.setText(_translate("delStud", "Gender:"))
        self.delButton.setText(_translate("delStud", "Confirm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    delStud = QtWidgets.QMainWindow()
    ui = Ui_delStud()
    ui.setupUi(delStud)
    delStud.show()
    sys.exit(app.exec_())
