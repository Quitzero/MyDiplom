# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infoWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 650)
        Dialog.setMinimumSize(QtCore.QSize(600, 650))
        Dialog.setMaximumSize(QtCore.QSize(600, 650))
        Dialog.setStyleSheet("QDialog{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(19, 0, 19, 20)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(200, 200))
        self.label.setMaximumSize(QtCore.QSize(200, 200))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resources/img/image-not-found.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setMinimumSize(QtCore.QSize(0, 380))
        self.frame.setStyleSheet("QFrame{\n"
"border: 1px solid rgb(208, 208, 208);\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.SatelliteLabel_2 = QtWidgets.QLabel(self.frame)
        self.SatelliteLabel_2.setMinimumSize(QtCore.QSize(280, 30))
        self.SatelliteLabel_2.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SatelliteLabel_2.setFont(font)
        self.SatelliteLabel_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.SatelliteLabel_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SatelliteLabel_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(66, 66, 66);")
        self.SatelliteLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.SatelliteLabel_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.SatelliteLabel_2.setObjectName("SatelliteLabel_2")
        self.horizontalLayout_10.addWidget(self.SatelliteLabel_2)
        self.Satellite_2 = QtWidgets.QLabel(self.frame)
        self.Satellite_2.setMinimumSize(QtCore.QSize(280, 0))
        self.Satellite_2.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Satellite_2.setFont(font)
        self.Satellite_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Satellite_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(66, 66, 66);")
        self.Satellite_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Satellite_2.setWordWrap(True)
        self.Satellite_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.Satellite_2.setObjectName("Satellite_2")
        self.horizontalLayout_10.addWidget(self.Satellite_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.SceneIdentifierLabel = QtWidgets.QLabel(self.frame)
        self.SceneIdentifierLabel.setMinimumSize(QtCore.QSize(150, 30))
        self.SceneIdentifierLabel.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SceneIdentifierLabel.setFont(font)
        self.SceneIdentifierLabel.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.SceneIdentifierLabel.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.SceneIdentifierLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.SceneIdentifierLabel.setObjectName("SceneIdentifierLabel")
        self.horizontalLayout_4.addWidget(self.SceneIdentifierLabel)
        self.SceneIdentifier = QtWidgets.QLabel(self.frame)
        self.SceneIdentifier.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SceneIdentifier.setFont(font)
        self.SceneIdentifier.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.SceneIdentifier.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.SceneIdentifier.setText("")
        self.SceneIdentifier.setWordWrap(True)
        self.SceneIdentifier.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.SceneIdentifier.setObjectName("SceneIdentifier")
        self.horizontalLayout_4.addWidget(self.SceneIdentifier)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.sensingTimeLabel = QtWidgets.QLabel(self.frame)
        self.sensingTimeLabel.setMinimumSize(QtCore.QSize(150, 30))
        self.sensingTimeLabel.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sensingTimeLabel.setFont(font)
        self.sensingTimeLabel.setStyleSheet("")
        self.sensingTimeLabel.setObjectName("sensingTimeLabel")
        self.horizontalLayout_9.addWidget(self.sensingTimeLabel)
        self.sensingTime = QtWidgets.QLabel(self.frame)
        self.sensingTime.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sensingTime.setFont(font)
        self.sensingTime.setStyleSheet("")
        self.sensingTime.setText("")
        self.sensingTime.setObjectName("sensingTime")
        self.horizontalLayout_9.addWidget(self.sensingTime)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.creationTimeLabel = QtWidgets.QLabel(self.frame)
        self.creationTimeLabel.setMinimumSize(QtCore.QSize(150, 0))
        self.creationTimeLabel.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.creationTimeLabel.setFont(font)
        self.creationTimeLabel.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.creationTimeLabel.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.creationTimeLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.creationTimeLabel.setObjectName("creationTimeLabel")
        self.horizontalLayout_6.addWidget(self.creationTimeLabel)
        self.creationTime = QtWidgets.QLabel(self.frame)
        self.creationTime.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.creationTime.setFont(font)
        self.creationTime.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.creationTime.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.creationTime.setText("")
        self.creationTime.setWordWrap(True)
        self.creationTime.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.creationTime.setObjectName("creationTime")
        self.horizontalLayout_6.addWidget(self.creationTime)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.satelliteLabel = QtWidgets.QLabel(self.frame)
        self.satelliteLabel.setMinimumSize(QtCore.QSize(150, 30))
        self.satelliteLabel.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.satelliteLabel.setFont(font)
        self.satelliteLabel.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.satelliteLabel.setStyleSheet("")
        self.satelliteLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.satelliteLabel.setObjectName("satelliteLabel")
        self.horizontalLayout_3.addWidget(self.satelliteLabel)
        self.satellite = QtWidgets.QLabel(self.frame)
        self.satellite.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.satellite.setFont(font)
        self.satellite.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.satellite.setStyleSheet("")
        self.satellite.setText("")
        self.satellite.setWordWrap(True)
        self.satellite.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.satellite.setObjectName("satellite")
        self.horizontalLayout_3.addWidget(self.satellite)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cloudPercentageLabel = QtWidgets.QLabel(self.frame)
        self.cloudPercentageLabel.setMinimumSize(QtCore.QSize(150, 30))
        self.cloudPercentageLabel.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.cloudPercentageLabel.setFont(font)
        self.cloudPercentageLabel.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.cloudPercentageLabel.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.cloudPercentageLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.cloudPercentageLabel.setObjectName("cloudPercentageLabel")
        self.horizontalLayout_2.addWidget(self.cloudPercentageLabel)
        self.cloudPercentage = QtWidgets.QLabel(self.frame)
        self.cloudPercentage.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cloudPercentage.setFont(font)
        self.cloudPercentage.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.cloudPercentage.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.cloudPercentage.setText("")
        self.cloudPercentage.setWordWrap(True)
        self.cloudPercentage.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.cloudPercentage.setObjectName("cloudPercentage")
        self.horizontalLayout_2.addWidget(self.cloudPercentage)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.DirectoryLabel = QtWidgets.QLabel(self.frame)
        self.DirectoryLabel.setMinimumSize(QtCore.QSize(150, 30))
        self.DirectoryLabel.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.DirectoryLabel.setFont(font)
        self.DirectoryLabel.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.DirectoryLabel.setStyleSheet("")
        self.DirectoryLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.DirectoryLabel.setObjectName("DirectoryLabel")
        self.horizontalLayout_5.addWidget(self.DirectoryLabel)
        self.Directory = QtWidgets.QLabel(self.frame)
        self.Directory.setMinimumSize(QtCore.QSize(238, 0))
        self.Directory.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Directory.setFont(font)
        self.Directory.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Directory.setStyleSheet("")
        self.Directory.setText("")
        self.Directory.setWordWrap(True)
        self.Directory.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.Directory.setObjectName("Directory")
        self.horizontalLayout_5.addWidget(self.Directory)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.forestidLabel = QtWidgets.QLabel(self.frame)
        self.forestidLabel.setMinimumSize(QtCore.QSize(280, 30))
        self.forestidLabel.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.forestidLabel.setFont(font)
        self.forestidLabel.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.forestidLabel.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.forestidLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.forestidLabel.setObjectName("forestidLabel")
        self.horizontalLayout_7.addWidget(self.forestidLabel)
        self.forestid = QtWidgets.QLabel(self.frame)
        self.forestid.setMinimumSize(QtCore.QSize(280, 0))
        self.forestid.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.forestid.setFont(font)
        self.forestid.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.forestid.setText("")
        self.forestid.setObjectName("forestid")
        self.horizontalLayout_7.addWidget(self.forestid)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Подробная информация"))
        self.SatelliteLabel_2.setText(_translate("Dialog", "Атрибут набора данных"))
        self.Satellite_2.setText(_translate("Dialog", "Значение атрибута"))
        self.SceneIdentifierLabel.setText(_translate("Dialog", "Идентификатор сцены"))
        self.sensingTimeLabel.setText(_translate("Dialog", "Период зондирования"))
        self.creationTimeLabel.setText(_translate("Dialog", "Период приема"))
        self.satelliteLabel.setText(_translate("Dialog", "Cпутник"))
        self.cloudPercentageLabel.setText(_translate("Dialog", "Облачность"))
        self.DirectoryLabel.setText(_translate("Dialog", "Директория"))
        self.forestidLabel.setText(_translate("Dialog", "forestid"))
import resources.img.Resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
