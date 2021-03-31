from PyQt5 import QtCore, QtGui, QtWidgets
from csvHandling import pushData

class Ui_addStudentWindow(object):
    def setupUi(self, addStudentWindow):
        addStudentWindow.setObjectName("addStudentWindow")
        addStudentWindow.resize(496, 444)
        self.centralwidget = QtWidgets.QWidget(addStudentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 451, 81))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 80, 461, 301))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.id = QtWidgets.QLabel(self.frame)
        self.id.setGeometry(QtCore.QRect(20, 15, 111, 31))

        font = QtGui.QFont()
        font.setPointSize(12)

        #labels
        self.id.setFont(font)
        self.id.setObjectName("id")
        self.lname = QtWidgets.QLabel(self.frame)
        self.lname.setGeometry(QtCore.QRect(20, 60, 111, 41))
        self.lname.setObjectName("lname")
        self.fname = QtWidgets.QLabel(self.frame)
        self.fname.setGeometry(QtCore.QRect(20, 95, 111, 31))
        self.fname.setObjectName("fname")
        self.mname = QtWidgets.QLabel(self.frame)
        self.mname.setGeometry(QtCore.QRect(20, 130, 131, 21))
        self.mname.setObjectName("mname")
        self.course = QtWidgets.QLabel(self.frame)
        self.course.setGeometry(QtCore.QRect(20, 205, 81, 31))
        self.course.setObjectName("course")
        self.year = QtWidgets.QLabel(self.frame)
        self.year.setGeometry(QtCore.QRect(20, 180, 101, 21))
        self.year.setObjectName("year")
        self.gender = QtWidgets.QLabel(self.frame)
        self.gender.setGeometry(QtCore.QRect(20, 250, 101, 31))
        self.gender.setObjectName("gender")

        #Inputs
        self.lnameIn = QtWidgets.QLineEdit(self.frame)
        self.lnameIn.setGeometry(QtCore.QRect(130, 70, 321, 20))
        self.lnameIn.setObjectName("lnameIn")

        self.idIn = QtWidgets.QLineEdit(self.frame)
        self.idIn.setGeometry(QtCore.QRect(130, 20, 321, 20))
        self.idIn.setObjectName("idIn")

        self.fnameIn = QtWidgets.QLineEdit(self.frame)
        self.fnameIn.setGeometry(QtCore.QRect(130, 100, 321, 20))
        self.fnameIn.setObjectName("fnameIn")

        self.mnameIn = QtWidgets.QLineEdit(self.frame)
        self.mnameIn.setGeometry(QtCore.QRect(130, 130, 321, 20))
        self.mnameIn.setObjectName("mnameIn")

        self.courseIn = QtWidgets.QLineEdit(self.frame)
        self.courseIn.setGeometry(QtCore.QRect(130, 210, 321, 20))
        self.courseIn.setObjectName("courseIn")

        self.yearIn = QtWidgets.QLineEdit(self.frame)
        self.yearIn.setGeometry(QtCore.QRect(130, 180, 321, 20))
        self.yearIn.setObjectName("yearIn")

        #Radio Buttons
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(130, 260, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.toggled.connect(self.selectedGender)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(190, 260, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(self.selectedGender)
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(270, 260, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.toggled.connect(self.selectedGender)

        #Submit
        self.addStudentButton = QtWidgets.QPushButton(self.centralwidget)
        self.addStudentButton.setGeometry(QtCore.QRect(360, 390, 101, 31))
        self.addStudentButton.setObjectName("addStudentButton")
        self.addStudentButton.clicked.connect(self.submitButton)

        addStudentWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(addStudentWindow)
        QtCore.QMetaObject.connectSlotsByName(addStudentWindow)
    
    def submitButton(self):
        if(self.idIn.text() != "" and self.lnameIn.text() !="" and self.fnameIn.text() != "" and self.mname.text() != "" and self.yearIn.text() != "" and self.courseIn.text() != "" and self.gen != ""):
            studentData = [self.idIn.text(), self.lnameIn.text(), self.fnameIn.text(), self.mname.text(), self.yearIn.text(), self.courseIn.text(), self.gen]
            pushData(studentData)

        else:
            alert = QtWidgets.QMessageBox()
            alert.setIcon(QtWidgets.QMessageBox.Information)
            alert.setText("No fields must be empty.")
            alert.setStandardButtons(QtWidgets.QMessageBox.Ok)
            alert.setWindowTitle("Error")

            a = alert.exec_()
    
    def selectedGender(self):
        self.gen = self.frame.sender().text()               #set gender variable from radio button signal

    def retranslateUi(self, addStudentWindow):
        _translate = QtCore.QCoreApplication.translate
        addStudentWindow.setWindowTitle(_translate("addStudentWindow", "Add Student"))
        self.label.setText(_translate("addStudentWindow", "Student Information"))
        self.id.setText(_translate("addStudentWindow", "ID Number:"))
        self.lname.setText(_translate("addStudentWindow", "Last Name:"))
        self.fname.setText(_translate("addStudentWindow", "First Name:"))
        self.mname.setText(_translate("addStudentWindow", "Middle Name:"))
        self.course.setText(_translate("addStudentWindow", "Course:"))
        self.year.setText(_translate("addStudentWindow", "Year:"))
        self.gender.setText(_translate("addStudentWindow", "Gender:"))
        self.radioButton.setText(_translate("addStudentWindow", "Male"))
        self.radioButton_2.setText(_translate("addStudentWindow", "Female"))
        self.radioButton_3.setText(_translate("addStudentWindow", "Others"))
        self.addStudentButton.setText(_translate("addStudentWindow", "Add Student"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addStudentWindow = QtWidgets.QMainWindow()
    ui = Ui_addStudentWindow()
    ui.setupUi(addStudentWindow)
    addStudentWindow.show()
    sys.exit(app.exec_())
