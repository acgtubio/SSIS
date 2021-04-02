from PyQt5 import QtCore, QtGui, QtWidgets
from csvHandling import getData, pushData

#maybe change file name?

class Ui_delStud(object):
    def setupUi(self, delStud, src = None):
        self.src = src
        delStud.setObjectName("delStud")
        delStud.resize(420, 410)
        self.centralwidget = QtWidgets.QWidget(delStud)
        self.centralwidget.setObjectName("centralwidget")
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(20, 20, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.l1.setFont(font)
        self.l1.setObjectName("l1")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 80, 380, 270))
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        #labels
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 153, 51, 31))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 199, 51, 31))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 233, 61, 31))
        self.label_5.setObjectName("label_5")

        #name labels
        font.setPointSize(8)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setFont(font)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 51, 21))
        self.label_2.setObjectName("label_2")

        self.flabel_2 = QtWidgets.QLabel(self.frame)
        self.flabel_2.setFont(font)
        self.flabel_2.setGeometry(QtCore.QRect(10, 91, 51, 21))
        self.flabel_2.setObjectName("label_2")

        self.mlabel_2 = QtWidgets.QLabel(self.frame)
        self.mlabel_2.setFont(font)
        self.mlabel_2.setGeometry(QtCore.QRect(10, 122, 51, 21))
        self.mlabel_2.setObjectName("label_2")
    
        #Read-only QLineEdits if delete, can write if otherwise
        
        self.idCheck = QtWidgets.QLineEdit(self.frame)
        self.idCheck.setGeometry(QtCore.QRect(100, 20, 161, 20))
        self.idCheck.setFont(font)
        self.idCheck.setObjectName("idCheck")
        
        self.lnameRE = QtWidgets.QLineEdit(self.frame)
        self.lnameRE.setGeometry(QtCore.QRect(100, 60, 161, 20))
        self.lnameRE.setFont(font)
        self.lnameRE.setObjectName("nameRE")
        self.lnameRE.setEnabled(False)

        self.fnameRE = QtWidgets.QLineEdit(self.frame)
        self.fnameRE.setGeometry(QtCore.QRect(100, 90, 161, 20))
        self.fnameRE.setFont(font)
        self.fnameRE.setObjectName("nameRE")
        self.fnameRE.setEnabled(False)

        self.mnameRE = QtWidgets.QLineEdit(self.frame)
        self.mnameRE.setGeometry(QtCore.QRect(100, 120, 161, 20))
        self.mnameRE.setFont(font)
        self.mnameRE.setObjectName("nameRE")
        self.mnameRE.setEnabled(False)
        
        self.yrRE = QtWidgets.QLineEdit(self.frame)
        self.yrRE.setGeometry(QtCore.QRect(100, 160, 161, 20))
        self.yrRE.setFont(font)
        self.yrRE.setObjectName("yrRE")
        self.yrRE.setEnabled(False)

        self.courseRE = QtWidgets.QLineEdit(self.frame)
        self.courseRE.setGeometry(QtCore.QRect(100, 200, 161, 20))
        self.courseRE.setFont(font)
        self.courseRE.setObjectName("courseRE")
        self.courseRE.setEnabled(False)

        self.genderRE = QtWidgets.QLineEdit(self.frame)
        self.genderRE.setGeometry(QtCore.QRect(100, 240, 161, 20))
        self.genderRE.setFont(font)
        self.genderRE.setObjectName("genderRE")
        self.genderRE.setEnabled(False)

        #Buttons
        self.recordCheck = QtWidgets.QPushButton(self.frame)
        self.recordCheck.setGeometry(QtCore.QRect(280, 19, 100, 23))
        self.recordCheck.setFont(font)
        self.recordCheck.setObjectName("recordCheck")
        self.recordCheck.clicked.connect(self.checkID)

        self.delButton = QtWidgets.QPushButton(self.centralwidget)
        self.delButton.setGeometry(QtCore.QRect(290, 360, 101, 31))
        self.delButton.setObjectName("delButton")
        if self.src == 'd':  
            self.delButton.clicked.connect(self.delStudConfirm)
        elif self.src == 'e':
            self.delButton.clicked.connect(self.editConfirm)
        else:
            self.delButton.hide()
        self.delButton.setEnabled(False)
        

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
                    self.lnameRE.setText(f"{student[1]}")
                    self.fnameRE.setText(f"{student[2]}")
                    self.mnameRE.setText(f"{student[3]}")
                    self.yrRE.setText(f"{student[4]}")
                    self.courseRE.setText(f"{student[5]}")
                    self.genderRE.setText(f"{student[6]}")
                    
                    self.delButton.setEnabled(True)

                    if self.src == 'e':
                        self.enableFields(True)
                        self.idCheck.setEnabled(False)
                        

            if(not found):
                self.cAlert.setText("ID not found.")
                a = self.cAlert.exec_()
        else:
            self.cAlert.setText("Enter ID #")
            a = self.cAlert.exec_()

    def editConfirm(self):
        self.delStudConfirm()                               #Deletes existing record, then appends an updated information.

        if(self.idCheck.text() != "" and self.lnameRE.text() !="" and self.fnameRE.text() != "" and self.mnameRE.text() != "" and self.yrRE.text() != "" and self.courseRE.text() != "" and self.genderRE != ""):
            pushData([self.idCheck.text(), self.lnameRE.text(), self.fnameRE.text(), self.mnameRE.text(), self.yrRE.text(), self.courseRE.text(), self.genderRE.text()], 'a')
            self.cAlert.setText("Information updated successfully.")
            a = self.cAlert.exec_()
        else:
            self.cAlert.setText("No field must be empty.")
            a = self.cAlert.exec_()
        self.resetUI()
        self.enableFields(False)
        self.idCheck.setEnabled(True)
    
    def delStudConfirm(self):
        mode = 'w'
        for student in self.studList:                             #Basically rewrites the entire csv file.
            if student[0] != self.delID:
                pushData(student, mode)
                mode = 'a'
        
        if self.src != 'e':
            self.cAlert.setText("User deleted successfully.")
            a = self.cAlert.exec_()
            self.resetUI()

    def resetUI(self):
        self.delButton.setEnabled(False)
        self.idCheck.setText("")
        self.lnameRE.setText("")
        self.fnameRE.setText("")
        self.mnameRE.setText("")
        self.yrRE.setText("")
        self.courseRE.setText("")
        self.genderRE.setText("")
        self.studList = None

    def enableFields(self,b):
        self.fnameRE.setEnabled(b)
        self.lnameRE.setEnabled(b)
        self.mnameRE.setEnabled(b)
        self.yrRE.setEnabled(b)
        self.courseRE.setEnabled(b)
        self.genderRE.setEnabled(b)
            
    def retranslateUi(self, delStud):
        _translate = QtCore.QCoreApplication.translate
        if(self.src == 'd' or self.src == None):
            title = "Delete Student"
        elif self.src == 'e':
            title = "Edit Information"
        else:
            title = "Student Information"
        delStud.setWindowTitle(_translate("delStud", f"{title}"))
        self.l1.setText(_translate("delStud", f"{title}")) 
        self.l1.adjustSize()
        self.label.setText(_translate("delStud", "Enter ID #:"))
        self.recordCheck.setText(_translate("delStud", "Check Record"))
        self.label_2.setText(_translate("delStud", "Last Name:"))
        self.label_2.adjustSize()
        self.flabel_2.setText(_translate("delStud", "First Name:"))
        self.flabel_2.adjustSize()
        self.mlabel_2.setText(_translate("delStud", "Middle Name:"))
        self.mlabel_2.adjustSize()
        self.label_3.setText(_translate("delStud", "Year:"))
        self.label_4.setText(_translate("delStud", "Course:"))
        self.label_4.adjustSize()
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
