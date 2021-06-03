from PyQt5 import QtCore, QtGui, QtWidgets
from dbHandling import DBHandling
from MessageBox import MessageBox
import re

class Ui_addStudentWindow(object):
    def setupUi(self, addStudentWindow, parent = None, source = "a", sourceID = None):
        self.p = parent
        self.src = source
        self.srcID = sourceID
        addStudentWindow.setObjectName("addStudentWindow")
        addStudentWindow.resize(500, 523)
        self.centralwidget = QtWidgets.QWidget(addStudentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 451, 81))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")

        #frame
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 80, 491, 371))
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.group1 = QtWidgets.QButtonGroup(self.centralwidget)
        self.group2 = QtWidgets.QButtonGroup(self.centralwidget)

        #labels
        self.id = QtWidgets.QLabel(self.frame)
        self.id.setGeometry(QtCore.QRect(20, 10, 111, 31))
        self.id.setFont(font)
        self.id.setObjectName("id")
        self.fname = QtWidgets.QLabel(self.frame)
        self.fname.setGeometry(QtCore.QRect(20, 101, 111, 20))
        self.fname.setObjectName("fname")
        self.mname = QtWidgets.QLabel(self.frame)
        self.mname.setGeometry(QtCore.QRect(20, 131, 131, 20))
        self.mname.setObjectName("mname")
        self.course = QtWidgets.QLabel(self.frame)
        self.course.setGeometry(QtCore.QRect(20, 180, 101, 21))
        self.course.setObjectName("course")
        self.year = QtWidgets.QLabel(self.frame)
        self.year.setGeometry(QtCore.QRect(20, 230, 81, 31))
        self.year.setObjectName("year")
        self.gender = QtWidgets.QLabel(self.frame)
        self.gender.setGeometry(QtCore.QRect(20, 330, 101, 31))
        self.gender.setObjectName("gender")
        self.lname = QtWidgets.QLabel(self.frame)
        self.lname.setGeometry(QtCore.QRect(20, 70, 111, 20))
        self.lname.setObjectName("lname")

        #inputs
        self.idIn = QtWidgets.QLineEdit(self.frame)
        self.idIn.setGeometry(QtCore.QRect(130, 20, 321, 20))
        self.idIn.setObjectName("idIn")
        self.lnameIn = QtWidgets.QLineEdit(self.frame)
        self.lnameIn.setGeometry(QtCore.QRect(130, 70, 321, 20))
        self.lnameIn.setObjectName("lnameIn")
        self.fnameIn = QtWidgets.QLineEdit(self.frame)
        self.fnameIn.setGeometry(QtCore.QRect(130, 100, 321, 20))
        self.fnameIn.setObjectName("fnameIn")
        self.mnameIn = QtWidgets.QLineEdit(self.frame)
        self.mnameIn.setGeometry(QtCore.QRect(130, 130, 321, 20))
        self.mnameIn.setObjectName("mnameIn")

        self.courseComboBox = QtWidgets.QComboBox(self.frame)
        self.courseComboBox.setGeometry(QtCore.QRect(130, 180, 321, 22))
        self.courseComboBox.setObjectName("courseComboBox")
        self.courseComboBox.addItem("")

        self.yr1 = QtWidgets.QRadioButton(self.frame)
        self.yr1.setGeometry(QtCore.QRect(130, 230, 82, 17))
        self.yr1.setObjectName("yr1")
        self.yr1.toggled.connect(self.__yrRadioToggled)
        self.yr2 = QtWidgets.QRadioButton(self.frame)
        self.yr2.setGeometry(QtCore.QRect(260, 230, 82, 17))
        self.yr2.setObjectName("yr2")
        self.yr2.toggled.connect(self.__yrRadioToggled)
        self.yr3 = QtWidgets.QRadioButton(self.frame)
        self.yr3.setGeometry(QtCore.QRect(130, 270, 82, 17))
        self.yr3.setObjectName("yr3")
        self.yr3.toggled.connect(self.__yrRadioToggled)
        self.yr4 = QtWidgets.QRadioButton(self.frame)
        self.yr4.setGeometry(QtCore.QRect(260, 270, 82, 17))
        self.yr4.setObjectName("yr4")
        self.yr4.toggled.connect(self.__yrRadioToggled)

        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(130, 330, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.toggled.connect(self.__genderRadioToggled)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(190, 330, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(self.__genderRadioToggled)
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(270, 330, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.toggled.connect(self.__genderRadioToggled)

        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(350, 330, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEnabled(False)

        # Radio Button Groups
        self.group1.addButton(self.radioButton)
        self.group1.addButton(self.radioButton_2)
        self.group1.addButton(self.radioButton_3)
        
        self.group2.addButton(self.yr1)
        self.group2.addButton(self.yr2)
        self.group2.addButton(self.yr3)
        self.group2.addButton(self.yr4)
        
        # Submit button
        self.addStudentButton = QtWidgets.QPushButton(self.centralwidget)
        self.addStudentButton.setGeometry(QtCore.QRect(350, 460, 130, 31))
        self.addStudentButton.setObjectName("addStudentButton")
        self.addStudentButton.clicked.connect(self.__submitButtonClicked)

        addStudentWindow.setCentralWidget(self.centralwidget)

        self.gen = ""
        self.yr = ""

        self.retranslateUi(addStudentWindow)
        self.__courseList()
        QtCore.QMetaObject.connectSlotsByName(addStudentWindow)

        self.__editState()
    
    def __editState(self):
        if self.src == "e":
            self.addStudentButton.setText(QtCore.QCoreApplication.translate("addStudentWindow", "Edit Information"))
            # self.editInfo.setText(QtCore.QCoreApplication.translate("addStudentWindow", "Enable Fields"))
            # self.editInfo.setVisible(True)

            self.__setEditStateValues()

            self.idIn.setEnabled(False)
            # self.lnameIn.setReadOnly(True)
            # self.fnameIn.setReadOnly(True)
            # self.mnameIn.setReadOnly(True)
            # self.courseComboBox.setEnabled(False)
            # self.yr1.setEnabled(False)
            # self.yr2.setEnabled(False)
            # self.yr3.setEnabled(False)
            # self.yr4.setEnabled(False)
            # self.radioButton.setEnabled(False)
            # self.radioButton_2.setEnabled(False)
            # self.radioButton_3.setEnabled(False)
            
        else:
            # self.editInfo.setVisible(False)
            # self.editInfo.setEnabled(False)
            self.addStudentButton.setText(QtCore.QCoreApplication.translate("addStudentWindow", "Add Student"))            

    def __setEditStateValues(self):
        data = DBHandling.getStudentData(f"WHERE id = \'{self.srcID}\'")
        
        if data != []:
            self.idIn.setText(data[0][0])
            self.lnameIn.setText(data[0][1])
            self.fnameIn.setText(data[0][2])
            self.mnameIn.setText(data[0][3])

            if self.yr1.text() == data[0][4]:
                self.yr1.toggle()
            elif self.yr2.text() == data[0][4]:
                self.yr2.toggle()
            elif self.yr3.text() == data[0][4]:
                self.yr3.toggle()
            else: 
                self.yr4.toggle()
            
            if self.radioButton.text() == data[0][5]:
                self.radioButton.toggle()
            elif self.radioButton_2.text() == data[0][5]:
                self.radioButton_2.toggle()
            else:
                self.radioButton_3.toggle()
                self.lineEdit.setText(data[0][5])

            for i in range(self.courseComboBox.count()):
                c = self.courseComboBox.itemText(i)
                d = c.split("-")[0].strip()
                if d == data[0][6]:
                    self.courseComboBox.setCurrentIndex(i)
                    break

    def __courseList(self):
        # Shows all available courses in the database
        courses = DBHandling.getCourseData()
        for course in courses:
            self.courseComboBox.addItem(f"{course[0]} - {course[1]}")        

    def __yrRadioToggled(self):
        # Takes year value from the toggle signal
        self.yr = self.frame.sender().text()
    
    def __genderRadioToggled(self):
        # Takes gender value from the toggle signal
        self.gen = self.frame.sender().text()
        if (self.gen != "Others"):
            self.lineEdit.setEnabled(False)
        else:
            self.lineEdit.setEnabled(True)

    def __submitButtonClicked(self):
        if self.gen == "Others":
            self.gen = self.lineEdit.text()

        # Checks if ID follows the specified regex format, else return.
        match = re.fullmatch(r"\d\d\d\d-\d\d\d\d", self.idIn.text())
        if match == None:
            MessageBox.showInformationMessage("ID must follow a YYYY-NNNN format.", "Invalid ID format")
            return 

        # Check for duplicate ID.
        idList = DBHandling.getStudentData(f"WHERE id = \'{self.idIn.text()}\'")
        if idList != [] and self.src == "a":
            MessageBox.showInformationMessage("ID already taken.", "Duplicate ID")
            return

        # Check for empty fields.
        noEmptyField = self.lnameIn.text() != "" and self.fnameIn.text() != "" and self.mnameIn.text() != "" and self.courseComboBox.currentText() != "" and self.gen != ""  and self.yr != ""
        if not noEmptyField:
            MessageBox.showInformationMessage("All fields must be accomplished.", "Error")
            return
        
        course = self.courseComboBox.currentText().split("-")
        courseCode = course[0].strip()

        alertText = "Add Student?" if self.src != "e" else "Update Information?"
        c = MessageBox.showConfirmationMessage(alertText, "Confirmation")

        if c == QtWidgets.QMessageBox.Yes:
            if self.src == "a":
                DBHandling.pushStudentData((self.idIn.text(), self.lnameIn.text(), self.fnameIn.text(), self.mnameIn.text(), self.yr, self.gen, courseCode))
                MessageBox.showInformationMessage("Student added.", "Success")
                self.__resetIn()
            else: 
                DBHandling.updateStudentData((self.lnameIn.text(), self.fnameIn.text(), self.mnameIn.text(), self.yr, self.gen, courseCode, self.srcID))
                MessageBox.showInformationMessage("Student data updated.", "Success")
        
        self.p.showList()

    def __resetIn(self):
        #resets input fields
        self.idIn.setText("")
        self.lnameIn.setText("")
        self.fnameIn.setText("")
        self.mnameIn.setText("")

        self.group1.setExclusive(False)
        self.group2.setExclusive(False) 

        
        self.yr1.setChecked(False)
        self.yr2.setChecked(False)    
        self.yr3.setChecked(False)
        self.yr4.setChecked(False)
        
        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.lineEdit.setText("")

        self.group1.setExclusive(True)
        self.group2.setExclusive(True)

        self.courseComboBox.setCurrentIndex(0)

    def retranslateUi(self, addStudentWindow):
        _translate = QtCore.QCoreApplication.translate
        addStudentWindow.setWindowTitle(_translate("addStudentWindow", "Add Student"))
        self.label.setText(_translate("addStudentWindow", "Student Information"))
        self.id.setText(_translate("addStudentWindow", "ID Number:"))
        self.fname.setText(_translate("addStudentWindow", "First Name:"))
        self.mname.setText(_translate("addStudentWindow", "Middle Name:"))
        self.course.setText(_translate("addStudentWindow", "Course:"))
        self.year.setText(_translate("addStudentWindow", "Year:"))
        self.gender.setText(_translate("addStudentWindow", "Gender:"))
        self.radioButton.setText(_translate("addStudentWindow", "Male"))
        self.radioButton_2.setText(_translate("addStudentWindow", "Female"))
        self.radioButton_3.setText(_translate("addStudentWindow", "Others"))
        self.yr1.setText(_translate("addStudentWindow", "1st Year"))
        self.yr2.setText(_translate("addStudentWindow", "2nd Year"))
        self.yr3.setText(_translate("addStudentWindow", "3rd Year"))
        self.yr4.setText(_translate("addStudentWindow", "4th Year"))
        self.lname.setText(_translate("addStudentWindow", "Last Name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addStudentWindow = QtWidgets.QMainWindow()
    ui = Ui_addStudentWindow()
    ui.setupUi(addStudentWindow)
    addStudentWindow.show()
    sys.exit(app.exec_())
