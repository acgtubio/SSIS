from PyQt5 import QtWidgets

class MessageBox:
    @staticmethod
    def showInformationMessage(message, title):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Information)
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        messageBox.setText(message)
        messageBox.setWindowTitle(title)
        res = messageBox.exec_()

        return res

    @staticmethod
    def showConfirmationMessage(message, title):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Question)
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        messageBox.setText(message)
        messageBox.setWindowTitle(title)
        res = messageBox.exec_()

        return res