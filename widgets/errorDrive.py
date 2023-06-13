# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'errorDrive.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_error(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(340, 380)
        Dialog.setMinimumSize(QtCore.QSize(340, 380))
        Dialog.setMaximumSize(QtCore.QSize(340, 380))
        Dialog.setStyleSheet("QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit{\n"
"border:2px solid #B8E2FF;\n"
"border-radius:5px;\n"
"background-color: rgb(250, 250, 250);\n"
"}\n"
"QLineEdit:focus{\n"
"border:3px solid rgb(0,157,255);\n"
"border-radius:5px;\n"
"}")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 180, 250, 30))
        self.lineEdit.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 240, 250, 30))
        self.lineEdit_2.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 320, 161, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border:3px solid rgb(0,157,255);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover:!pressed{\n"
"border:3px solid  rgb(175,0,0);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Имя пользователя"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Пароль"))
        self.label.setText(_translate("Dialog", "При подключении к сетевым дискам произошла ошибка. Скорее всего были введены неправильные учетные данные."))
        self.pushButton.setText(_translate("Dialog", "Подключить"))
        self.label_2.setText(_translate("Dialog", "Для исправления этой проблемы введите свои учетные данные:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_error()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
