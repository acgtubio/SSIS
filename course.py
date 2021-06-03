from PyQt5 import QtCore, QtGui, QtWidgets
from dbHandling import DBHandling
from MessageBox import MessageBox
import addcourse

class Ui_courses(object):
    def setupUi(self, courses):
        courses.setObjectName("courses")
        courses.resize(605, 560)
        self.centralwidget = QtWidgets.QWidget(courses)
        self.centralwidget.setObjectName("centralwidget")

        #buttons
        self.addCourse = QtWidgets.QPushButton(self.centralwidget)
        self.addCourse.setGeometry(QtCore.QRect(440, 470, 131, 31))
        self.addCourse.setObjectName("addCourse")
        self.addCourse.clicked.connect(self.__addCourse)

        self.deleteCourse = QtWidgets.QPushButton(self.centralwidget)
        self.deleteCourse.setGeometry(QtCore.QRect(440, 430, 131, 31))
        self.deleteCourse.setObjectName("deleteCourse")
        self.deleteCourse.clicked.connect(self.__deleteCourseClicked)

        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(430, 140, 75, 23))
        self.search.setObjectName("search")
        self.search.clicked.connect(self.__searchClicked)

        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(515, 140, 75, 23))
        self.refresh.setObjectName("refresh")
        self.refresh.clicked.connect(self.__refreshClicked)
        
        #search fields
        self.searchIn = QtWidgets.QLineEdit(self.centralwidget)
        self.searchIn.setGeometry(QtCore.QRect(430, 60, 141, 20))
        self.searchIn.setObjectName("searchIn")

        self.searchLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchLabel.setGeometry(QtCore.QRect(430, 30, 51, 21))

        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.searchLabel.setFont(font)
        self.searchLabel.setObjectName("searchLabel")

        self.params = None

        #radio buttons for search fields
        self.ccradio = QtWidgets.QRadioButton(self.centralwidget)
        self.ccradio.setGeometry(QtCore.QRect(430, 90, 101, 17))
        self.ccradio.setObjectName("ccradio")
        self.ccradio.toggled.connect(self.courseRadioTriggered)

        self.cnradio = QtWidgets.QRadioButton(self.centralwidget)
        self.cnradio.setGeometry(QtCore.QRect(430, 110, 101, 17))
        self.cnradio.setObjectName("cnradio")
        self.cnradio.toggled.connect(self.courseRadioTriggered)

        self.group = QtWidgets.QButtonGroup(self.centralwidget)
        self.group.addButton(self.ccradio)
        self.group.addButton(self.cnradio)

        #table
        self.courseList = QtWidgets.QTableWidget(self.centralwidget)
        self.courseList.setGeometry(QtCore.QRect(20, 20, 391, 481))
        self.courseList.setObjectName("courseList")
        self.courseList.setColumnCount(2)
        self.courseList.setHorizontalHeaderLabels(["Course Code", "Course Name"])
        self.courseList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.courseList.setShowGrid(False)
        self.courseList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.courseList.setColumnWidth(1,250)
        self.courseList.doubleClicked.connect(self.__rowDoubleClicked)

        self.prev = QtWidgets.QPushButton(self.centralwidget)
        self.prev.setGeometry(QtCore.QRect(165, 512, 40, 30))
        self.prev.setObjectName("prev")
        self.prev.clicked.connect(self.__prev)

        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(235, 512, 40, 30))
        self.next.setObjectName("next")
        self.next.clicked.connect(self.__next)

        self.pageNum = QtWidgets.QLabel(self.centralwidget)
        self.pageNum.setObjectName("searchLabel")
        self.pageNum.setGeometry(QtCore.QRect(215, 517, 21, 21))
        self.pageNum.setFont(font)

        self.page = 1

        courses.setCentralWidget(self.centralwidget)

        self.showCourseList()

        self.retranslateUi(courses)
        QtCore.QMetaObject.connectSlotsByName(courses)

    def __next(self):
        self.page += 1

        self.showCourseList(None,self.page)

    def __prev(self):
        if self.page == 1:
            return

        self.page -= 1

        self.showCourseList(None,self.page)

    def __deleteCourseClicked(self):
        id = self.courseList.item(self.courseList.currentRow(),0).text()
        a = MessageBox.showConfirmationMessage(f"Date course with course code {id}?", "Confirm")

        if a == QtWidgets.QMessageBox.Yes:
            s = DBHandling.delCourseData(id)
            if s == -1:
                MessageBox.showInformationMessage("Course cannot be deleted. Students are enrolled in this course.", "Delete Failed.")
            else:
                MessageBox.showInformationMessage("Course deleted successfully.", "Alert")
            self.__refreshClicked()


    def __refreshClicked(self):
        self.showCourseList()

        self.group.setExclusive(False)
        self.ccradio.setChecked(False)
        self.cnradio.setChecked(False)
        self.group.setExclusive(True)

        self.searchIn.setText("")

    def __searchClicked(self):
        cond = ""
        if self.params == 1:
           cond = f"WHERE course_code LIKE '%{self.searchIn.text()}%'"
        elif self.params == 2:
            cond = f"WHERE course_name LIKE '%{self.searchIn.text()}%'"

        data = DBHandling.getCourseData(cond)
        self.showCourseList(data)

    def __rowDoubleClicked(self):
        # Opens Add Course window but with limitations to allow to update information.
        id = self.courseList.item(self.courseList.currentRow(), 0).text()
        self.a = AddCourse(None,"e", id)
        self.a.show()

    def courseRadioTriggered(self):
        # To determine which radio button is selected.
        if self.centralwidget.sender().text() == "By Course Code":
            self.params = 1
        else: 
            self.params = 2
        
    def showCourseList(self, args = None, page = 1):
        # Display course data provided by the caller, uses database by default
        if page == 1:
            self.page = 1

        self.pageNum.setText(str(page))
        if args != None:
            data = args
        else:
            data = DBHandling.getCourseData(f" LIMIT 15 OFFSET {(page-1)*15}")

        self.courseList.setRowCount(len(data))
        row = 0

        for course in data:
            self.courseList.setItem(row, 0, QtWidgets.QTableWidgetItem(course[0]))
            self.courseList.setItem(row, 1, QtWidgets.QTableWidgetItem(course[1]))
            row+=1

    def __addCourse(self):
        self.a = AddCourse(self)
        self.a.show()

    def retranslateUi(self, courses):
        _translate = QtCore.QCoreApplication.translate
        courses.setWindowTitle(_translate("courses", "Courses"))
        self.addCourse.setText(_translate("courses", "Add Course"))
        self.deleteCourse.setText(_translate("courses", "Delete Course"))
        self.searchLabel.setText(_translate("courses", "Search"))
        self.ccradio.setText(_translate("courses", "By Course Code"))
        self.cnradio.setText(_translate("courses", "By Course Name"))
        self.search.setText(_translate("courses", "Search"))
        self.refresh.setText(_translate("courses", "Clear"))
        self.next.setText(_translate("courses", ">"))
        self.prev.setText(_translate("courses", "<"))

class AddCourse(QtWidgets.QMainWindow, addcourse.Ui_MainWindow):
    def __init__(self, parent = None, mode = "a", id = None):
        super().__init__()

        self.setupUi(self, parent, mode, id)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    courses = QtWidgets.QMainWindow()
    ui = Ui_courses()
    ui.setupUi(courses)
    courses.show()
    sys.exit(app.exec_())
