# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'snapshotWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_snapshot(object):
    def setupUi(self, snapshot):
        snapshot.setObjectName("snapshot")
        snapshot.resize(270, 80)
        snapshot.setMinimumSize(QtCore.QSize(250, 80))
        snapshot.setMaximumSize(QtCore.QSize(250, 80))
        snapshot.setStyleSheet("QFrame#snapshot{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(snapshot)
        self.horizontalLayout.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(snapshot)
        self.label.setMaximumSize(QtCore.QSize(35, 35))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resources/img/loader.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.moreButton = QtWidgets.QPushButton(snapshot)
        self.moreButton.setMinimumSize(QtCore.QSize(120, 30))
        self.moreButton.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.moreButton.setFont(font)
        self.moreButton.setStyleSheet("QPushButton{\n"
"border:3px solid rgb(0,157,255);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover:!pressed{\n"
"border:3px solid  rgb(175,0,0);\n"
"}")
        self.moreButton.setObjectName("moreButton")
        self.horizontalLayout.addWidget(self.moreButton)
        self.pushButton = QtWidgets.QPushButton(snapshot)
        self.pushButton.setMinimumSize(QtCore.QSize(24, 24))
        self.pushButton.setMaximumSize(QtCore.QSize(24, 24))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border:none;\n"
"background-image: url(:/loop/loop-blue.png);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-image: url(:/loop/loop-red.png);\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.LoadButton = QtWidgets.QPushButton(snapshot)
        self.LoadButton.setMinimumSize(QtCore.QSize(24, 24))
        self.LoadButton.setMaximumSize(QtCore.QSize(24, 24))
        self.LoadButton.setStyleSheet("QPushButton{\n"
"border:none;\n"
"width:24px;\n"
"height:24px;\n"
"}\n"
"QPushButton{\n"
"background-image: url(:/download/download-blue.png);\n"
"}\n"
"QPushButton:hover:!pressed{\n"
"background-image: url(:/download/download-red.png);\n"
"}\n"
"")
        self.LoadButton.setText("")
        self.LoadButton.setObjectName("LoadButton")
        self.horizontalLayout.addWidget(self.LoadButton)

        self.retranslateUi(snapshot)
        QtCore.QMetaObject.connectSlotsByName(snapshot)

    def retranslateUi(self, snapshot):
        _translate = QtCore.QCoreApplication.translate
        snapshot.setWindowTitle(_translate("snapshot", "Frame"))
        self.moreButton.setToolTip(_translate("snapshot", "Показать метаданные"))
        self.moreButton.setText(_translate("snapshot", "Подробнее"))
        self.pushButton.setToolTip(_translate("snapshot", "Установить след"))
        self.LoadButton.setToolTip(_translate("snapshot", "Загрузить на устройство"))
import resources.img.Resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    snapshot = QtWidgets.QFrame()
    ui = Ui_snapshot()
    ui.setupUi(snapshot)
    snapshot.show()
    sys.exit(app.exec_())
