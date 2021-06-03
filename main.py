from PyQt5 import QtCore, QtGui, QtWidgets
from dbHandling import DBHandling
import sqlite3
import addstudent
import course
from MessageBox import MessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 537)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Table
        self.studentList = QtWidgets.QTableWidget(self.centralwidget)
        self.studentList.setGeometry(QtCore.QRect(20, 20, 710, 461))
        self.studentList.setColumnCount(5)
        self.studentList.setObjectName("studentList")
        self.studentList.setHorizontalHeaderLabels(["ID","Name","Year","Course","Gender"])
        self.studentList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.studentList.setShowGrid(False)
        self.studentList.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.studentList.doubleClicked.connect(self.openInfo)
        self.studentList.setColumnWidth(0, 70)
        self.studentList.setColumnWidth(1, 250)
        self.studentList.setColumnWidth(2, 60)
        self.studentList.setColumnWidth(3, 230)
        self.studentList.setColumnWidth(4, 80)

        #Buttons
        self.viewCourses = QtWidgets.QPushButton(self.centralwidget)
        self.viewCourses.setGeometry(QtCore.QRect(750, 385, 111, 41))
        self.viewCourses.setObjectName("viewCourses")
        self.viewCourses.clicked.connect(self.__viewCoursesClicked)

        self.delStudent = QtWidgets.QPushButton(self.centralwidget)
        self.delStudent.setGeometry(QtCore.QRect(870, 435, 111, 41))
        self.delStudent.setObjectName("delStudent")
        self.delStudent.clicked.connect(self.delStudentClicked)

        self.addStudent = QtWidgets.QPushButton(self.centralwidget)
        self.addStudent.setGeometry(QtCore.QRect(750, 435, 111, 41))
        self.addStudent.setObjectName("addStudent")
        self.addStudent.clicked.connect(self.addStudentClicked)

        self.prev = QtWidgets.QPushButton(self.centralwidget)
        self.prev.setGeometry(QtCore.QRect(350, 485, 40, 30))
        self.prev.setObjectName("prev")
        self.prev.clicked.connect(self.__prev)

        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(420, 485, 40, 30))
        self.next.setObjectName("next")
        self.next.clicked.connect(self.__next)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #SEARCH FIELD
        self.searchLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchLabel.setObjectName("searchLabel")
        self.searchLabel.setGeometry(QtCore.QRect(750, 20, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.searchLabel.setFont(font)

        self.pageNum = QtWidgets.QLabel(self.centralwidget)
        self.pageNum.setObjectName("searchLabel")
        self.pageNum.setGeometry(QtCore.QRect(400, 490, 21, 21))
        self.pageNum.setFont(font)

        #search button
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setObjectName("search")
        self.search.setGeometry(QtCore.QRect(750, 170, 75, 23))
        self.search.clicked.connect(self.__searchClicked)

        #checkbox search constraints
        self.idCB = QtWidgets.QCheckBox(self.centralwidget)
        self.idCB.setObjectName("idCB")
        self.idCB.setGeometry(QtCore.QRect(750, 50, 70, 17))
        self.idCB.toggled.connect(self.idCBToggled)

        self.nameCB = QtWidgets.QCheckBox(self.centralwidget)
        self.nameCB.setObjectName("nameCB")
        self.nameCB.setGeometry(QtCore.QRect(750, 80, 70, 17))
        self.nameCB.toggled.connect(self.nameCBToggled)

        self.yrCB = QtWidgets.QCheckBox(self.centralwidget)
        self.yrCB.setObjectName("yrCB")
        self.yrCB.setGeometry(QtCore.QRect(750, 110, 70, 17))
        self.yrCB.toggled.connect(self.yrCBToggled)

        self.ccCB = QtWidgets.QCheckBox(self.centralwidget)
        self.ccCB.setObjectName("ccCB")
        self.ccCB.setGeometry(QtCore.QRect(750, 140, 81, 17))
        self.ccCB.toggled.connect(self.ccCBToggled)

        #search constraints
        self.idIn = QtWidgets.QLineEdit(self.centralwidget)
        self.idIn.setObjectName("idIn")
        self.idIn.setGeometry(QtCore.QRect(840, 50, 141, 20))
        self.idIn.setEnabled(False)

        self.nameIn = QtWidgets.QLineEdit(self.centralwidget)
        self.nameIn.setObjectName("nameIn")
        self.nameIn.setGeometry(QtCore.QRect(840, 80, 141, 20))
        self.nameIn.setEnabled(False)

        self.yrIn = QtWidgets.QComboBox(self.centralwidget)
        self.yrIn.setObjectName("yrIn")
        self.yrIn.setGeometry(QtCore.QRect(840, 110, 141, 22))
        self.yrIn.setEnabled(False)

        self.courseComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.courseComboBox.setGeometry(QtCore.QRect(840, 140, 141, 22))
        self.courseComboBox.setObjectName("courseComboBox")
        self.courseComboBox.setEnabled(False)

        self.retranslateUi(MainWindow)
        self.showList()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.__courseList()
        self.__yrList()
        
        self.page = 1
        self.rowItems = None
    
    def __viewCoursesClicked(self):
        a = ViewCourses(self)
        a.show()

    def __next(self):
        self.page += 1

        self.showList([],self.page)

    def __prev(self):
        if self.page == 1:
            return

        self.page -= 1

        self.showList([],self.page)

    def __searchClicked(self):
        cond = ""
        prev = "WHERE"

        if self.idIn.text() != "":
            cond += f"{prev} students.id LIKE '%{self.idIn.text()}%' "
            prev = "AND"
        
        if self.nameIn.text():
            cond += f"{prev} (students.last_name LIKE '%{self.nameIn.text()}%' OR students.middle_name LIKE '%{self.nameIn.text()}%' OR students.first_name LIKE '%{self.nameIn.text()}%') "
            prev = "AND"

        if self.yrIn.currentText() != "":
            cond += f"{prev} students.year = '{self.yrIn.currentText()}' "
            prev = "AND"
        
        if self.courseComboBox.currentText() != "":
            cond += f"{prev} students.course = '{self.courseComboBox.currentText()}'"

        data = DBHandling.getStudentCourse(cond)
        self.showList(data)

    def __courseList(self):
        # Shows all available courses in the database
        courses = DBHandling.getCourseData()
        self.courseComboBox.addItem("")
        for course in courses:
            self.courseComboBox.addItem(f"{course[0]}")

    def __yrList(self):
        self.yrIn.addItem("")
        self.yrIn.addItem("1st Year")
        self.yrIn.addItem("2nd Year")
        self.yrIn.addItem("3rd Year")
        self.yrIn.addItem("4th Year")

    def openInfo(self, index):
        id = self.studentList.item(self.studentList.currentRow(), 0).text()
        self.b = addSt(self, "e", id)
        self.b.show()
    
    def idCBToggled(self):
        if not self.idIn.isEnabled():
            self.idIn.setEnabled(True)
        else:
            self.idIn.setEnabled(False)
            self.idIn.setText("")

    def nameCBToggled(self):
        if not self.nameIn.isEnabled():
            self.nameIn.setEnabled(True)
        else:
            self.nameIn.setEnabled(False)
            self.nameIn.setText("")

    def yrCBToggled(self):
        if not self.yrIn.isEnabled():
            self.yrIn.setEnabled(True)
        else:
            self.yrIn.setEnabled(False)
            self.yrIn.setCurrentIndex(0)

    def ccCBToggled(self):
        if not self.courseComboBox.isEnabled():
            self.courseComboBox.setEnabled(True)
        else:
            self.courseComboBox.setEnabled(False)
            self.courseComboBox.setCurrentIndex(0)

    def addStudentClicked(self):
        self.b = addSt(self)
        self.b.show()

    def delStudentClicked(self):
        if self.studentList.selectedItems() == []:
            return

        id = self.studentList.item(self.studentList.currentRow(), 0).text()

        m = MessageBox.showConfirmationMessage("Delete Student?", "Confirmation")
        
        if(m == QtWidgets.QMessageBox.Yes):
            DBHandling.delStudentData(id)
            self.showList()
        
        MessageBox.showInformationMessage("Student Deleted.", "Success")
        
    def showList(self, data = [], page = 1):
        if page == 1:
            self.page = 1
        self.pageNum.setText(str(page))
        if data != []:
            students = data
        else:
            students = DBHandling.getStudentCourse(f" LIMIT 15 OFFSET {(page-1)*15}")                                      #from dbHandling file.
        # print(students)
        self.studentList.setRowCount(len(students))
        row = 0
        for student in students:
            self.studentList.setItem(row, 0, QtWidgets.QTableWidgetItem(str(student[0])))
            self.studentList.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{student[1]}, {student[2]} {student[3]}"))
            self.studentList.setItem(row, 2, QtWidgets.QTableWidgetItem(str(student[4])))
            self.studentList.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{student[6]} | {student[8]}"))
            self.studentList.setItem(row, 4, QtWidgets.QTableWidgetItem(str(student[5])))
            row+=1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Information System V2"))
        self.searchLabel.setText(_translate("MainWindow", "Search"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.idCB.setText(_translate("MainWindow", "ID Number"))
        self.nameCB.setText(_translate("MainWindow", "Name"))
        self.yrCB.setText(_translate("MainWindow", "Year "))
        self.ccCB.setText(_translate("MainWindow", "Course Code"))
        self.viewCourses.setText(_translate("MainWindow", "Courses"))
        self.delStudent.setText(_translate("MainWindow", "Delete Student"))
        self.addStudent.setText(_translate("MainWindow", "Add Sudent"))
        self.prev.setText(_translate("MainWindow", "<"))
        self.next.setText(_translate("MainWindow", ">"))

#opens different windows
class mainWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class addSt(QtWidgets.QMainWindow, addstudent.Ui_addStudentWindow):
    def __init__(self, parent = None, mode = "a", srcID = None):
        super().__init__(parent)
        
        self.setupUi(self, parent, mode, srcID)

class ViewCourses(QtWidgets.QMainWindow, course.Ui_courses):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    a = mainWin()
    a.show()

    sys.exit(app.exec_())
