# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1263, 701)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AdvancedSearch = QtWidgets.QGroupBox(self.centralwidget)
        self.AdvancedSearch.setMinimumSize(QtCore.QSize(350, 0))
        self.AdvancedSearch.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AdvancedSearch.setFont(font)
        self.AdvancedSearch.setStyleSheet("/* Чекбоксы*/\n"
"QCheckBox::indicator{\n"
"width:24px;\n"
"height:24px;\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"background-image: url(:/blank/checked-blue.png);\n"
"}\n"
"QCheckBox::indicator:unchecked:hover, QCheckBox::indicator:unchecked:pressed{\n"
"background-image: url(:/blank/blank-red.png);\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"background-image: url(:/checked/blank-blue.png);\n"
"}\n"
"QCheckBox::indicator:checked:hover, QCheckBox::indicator:checked:pressed{\n"
"background-image: url(:/checked/checked-red.png);\n"
"}\n"
"\n"
"/* Календарь*/\n"
"QCalendarWidget QWidget{\n"
"alternate-background-color: #B8E2FF;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar{\n"
"background-color: rgb(255, 255, 255);\n"
"border:2px solid #B8E2FF;\n"
"border-bottom: 0px;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_prevmonth, QCalendarWidget QWidget#qt_calendar_nextmonth{\n"
"border: none;\n"
"qproperty-icon: none;\n"
"min-width: 13px;\n"
"max-width: 13px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"border-radius: 5px;\n"
"background color: transparent;\n"
"padding: 5px;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_prevmonth{\n"
"margin-top:5px;\n"
"margin-left:5px;\n"
"margin-bottom:3px;\n"
"image: url(:/arrow/arrow2.png);\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_nextmonth{\n"
"margin-top:5px;\n"
"margin-right:5px;\n"
"margin-bottom:3px;\n"
"image: url(:/arrow/arrow1.png);\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_prevmonth:hover, QCalendarWidget QWidget#qt_calendar_nextmonth:hover{\n"
"background-color: #B8E2FF;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_yearbutton{\n"
"border-radius:5px;\n"
"color: #000;\n"
"margin-top:5px;\n"
"margin-bottom:3px;\n"
"border-redis:5px;\n"
"font-size:13px;\n"
"padding: 0 10px;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_monthbutton{\n"
"border-radius:5px;\n"
"width:110px;\n"
"color: #000;\n"
"margin-top:5px;\n"
"margin-bottom:3px;\n"
"border-redis:5px;\n"
"font-size:13px;\n"
"padding: 0 2px;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_monthbutton:hover, QCalendarWidget QWidget#qt_calendar_yearbutton:hover{\n"
"background-color: #B8E2FF;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_monthbutton:pressed, QCalendarWidget QWidget#qt_calendar_yearbutton:pressed{\n"
"background-color: rgb(247, 247, 247);\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_yearedit{\n"
"margin-top:2px;\n"
"width:50px;\n"
"color:#000;\n"
"font-size:13px;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_yearedit:down-button{\n"
"border-image: url(:/arrow/arrow-down.png);\n"
"subcontrol-position:left;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_yearedit:up-button{\n"
"image: url(:/arrow/arrow-up.png);\n"
"subcontrol-position:right;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_yearedit:up-button:hover{\n"
"image: url(:/arrow/arrow-up-blue.png);\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_yearedit:down-button:hover{\n"
"image: url(:/arrow/arrow-down-blue.png);\n"
"}\n"
"QCalendarWidget QWidget QToolButton::menu-indicator{\n"
"image:none;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_calendarview {\n"
"outline: 0px;\n"
"selection-background-color: rgb(165, 204, 229);\n"
"}\n"
"")
        self.AdvancedSearch.setObjectName("AdvancedSearch")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.AdvancedSearch)
        self.verticalLayout_8.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_8.setSpacing(20)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.SatelliteSystem = QtWidgets.QFrame(self.AdvancedSearch)
        self.SatelliteSystem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SatelliteSystem.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SatelliteSystem.setObjectName("SatelliteSystem")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.SatelliteSystem)
        self.verticalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.SatelliteLabel = QtWidgets.QLabel(self.SatelliteSystem)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SatelliteLabel.setFont(font)
        self.SatelliteLabel.setObjectName("SatelliteLabel")
        self.horizontalLayout_4.addWidget(self.SatelliteLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.SatelliteComboBox = QtWidgets.QComboBox(self.SatelliteSystem)
        self.SatelliteComboBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SatelliteComboBox.setFont(font)
        self.SatelliteComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SatelliteComboBox.setObjectName("SatelliteComboBox")
        self.SatelliteComboBox.addItem("")
        self.SatelliteComboBox.addItem("")
        self.SatelliteComboBox.addItem("")
        self.verticalLayout_2.addWidget(self.SatelliteComboBox)
        self.verticalLayout_8.addWidget(self.SatelliteSystem)
        self.SensingPeriod = QtWidgets.QFrame(self.AdvancedSearch)
        self.SensingPeriod.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SensingPeriod.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SensingPeriod.setObjectName("SensingPeriod")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.SensingPeriod)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.SensingLabelHorizontalLayout = QtWidgets.QHBoxLayout()
        self.SensingLabelHorizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.SensingLabelHorizontalLayout.setSpacing(15)
        self.SensingLabelHorizontalLayout.setObjectName("SensingLabelHorizontalLayout")
        self.SensingLabel = QtWidgets.QLabel(self.SensingPeriod)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SensingLabel.setFont(font)
        self.SensingLabel.setObjectName("SensingLabel")
        self.SensingLabelHorizontalLayout.addWidget(self.SensingLabel)
        self.SensingCheckBox = QtWidgets.QCheckBox(self.SensingPeriod)
        self.SensingCheckBox.setMinimumSize(QtCore.QSize(0, 0))
        self.SensingCheckBox.setMaximumSize(QtCore.QSize(24, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.SensingCheckBox.setFont(font)
        self.SensingCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SensingCheckBox.setStyleSheet("")
        self.SensingCheckBox.setText("")
        self.SensingCheckBox.setChecked(True)
        self.SensingCheckBox.setObjectName("SensingCheckBox")
        self.SensingLabelHorizontalLayout.addWidget(self.SensingCheckBox)
        self.verticalLayout_6.addLayout(self.SensingLabelHorizontalLayout)
        self.SensingHorizontalLayout = QtWidgets.QHBoxLayout()
        self.SensingHorizontalLayout.setObjectName("SensingHorizontalLayout")
        self.SensingFromDateEdit = QtWidgets.QDateEdit(self.SensingPeriod)
        self.SensingFromDateEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.SensingFromDateEdit.setFont(font)
        self.SensingFromDateEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.SensingFromDateEdit.setCalendarPopup(True)
        self.SensingFromDateEdit.setObjectName("SensingFromDateEdit")
        self.SensingHorizontalLayout.addWidget(self.SensingFromDateEdit)
        self.SensingToDateEdit = QtWidgets.QDateEdit(self.SensingPeriod)
        self.SensingToDateEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.SensingToDateEdit.setFont(font)
        self.SensingToDateEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.SensingToDateEdit.setCalendarPopup(True)
        self.SensingToDateEdit.setObjectName("SensingToDateEdit")
        self.SensingHorizontalLayout.addWidget(self.SensingToDateEdit)
        self.verticalLayout_6.addLayout(self.SensingHorizontalLayout)
        self.verticalLayout_8.addWidget(self.SensingPeriod)
        self.IngestionPeriod = QtWidgets.QFrame(self.AdvancedSearch)
        self.IngestionPeriod.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.IngestionPeriod.setFrameShadow(QtWidgets.QFrame.Raised)
        self.IngestionPeriod.setObjectName("IngestionPeriod")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.IngestionPeriod)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.IngestionLabelHorizontalLayout = QtWidgets.QHBoxLayout()
        self.IngestionLabelHorizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.IngestionLabelHorizontalLayout.setSpacing(6)
        self.IngestionLabelHorizontalLayout.setObjectName("IngestionLabelHorizontalLayout")
        self.IngestionLabel = QtWidgets.QLabel(self.IngestionPeriod)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.IngestionLabel.setFont(font)
        self.IngestionLabel.setObjectName("IngestionLabel")
        self.IngestionLabelHorizontalLayout.addWidget(self.IngestionLabel)
        self.IngestionCheckBox = QtWidgets.QCheckBox(self.IngestionPeriod)
        self.IngestionCheckBox.setMinimumSize(QtCore.QSize(0, 0))
        self.IngestionCheckBox.setMaximumSize(QtCore.QSize(24, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.IngestionCheckBox.setFont(font)
        self.IngestionCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.IngestionCheckBox.setStyleSheet("")
        self.IngestionCheckBox.setText("")
        self.IngestionCheckBox.setChecked(True)
        self.IngestionCheckBox.setObjectName("IngestionCheckBox")
        self.IngestionLabelHorizontalLayout.addWidget(self.IngestionCheckBox)
        self.verticalLayout_3.addLayout(self.IngestionLabelHorizontalLayout)
        self.IngestionHorizontalLayout = QtWidgets.QHBoxLayout()
        self.IngestionHorizontalLayout.setObjectName("IngestionHorizontalLayout")
        self.IngestionFromDateEdit = QtWidgets.QDateEdit(self.IngestionPeriod)
        self.IngestionFromDateEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.IngestionFromDateEdit.setFont(font)
        self.IngestionFromDateEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.IngestionFromDateEdit.setStyleSheet("")
        self.IngestionFromDateEdit.setCalendarPopup(True)
        self.IngestionFromDateEdit.setObjectName("IngestionFromDateEdit")
        self.IngestionHorizontalLayout.addWidget(self.IngestionFromDateEdit)
        self.IngestionToDateEdit = QtWidgets.QDateEdit(self.IngestionPeriod)
        self.IngestionToDateEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.IngestionToDateEdit.setFont(font)
        self.IngestionToDateEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.IngestionToDateEdit.setCalendarPopup(True)
        self.IngestionToDateEdit.setObjectName("IngestionToDateEdit")
        self.IngestionHorizontalLayout.addWidget(self.IngestionToDateEdit)
        self.verticalLayout_3.addLayout(self.IngestionHorizontalLayout)
        self.verticalLayout_8.addWidget(self.IngestionPeriod)
        self.Cloudiness = QtWidgets.QFrame(self.AdvancedSearch)
        self.Cloudiness.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Cloudiness.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Cloudiness.setObjectName("Cloudiness")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Cloudiness)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.CloudinessLabel = QtWidgets.QLabel(self.Cloudiness)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CloudinessLabel.setFont(font)
        self.CloudinessLabel.setObjectName("CloudinessLabel")
        self.horizontalLayout_5.addWidget(self.CloudinessLabel)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout_8.addWidget(self.Cloudiness)
        self.frame = QtWidgets.QFrame(self.AdvancedSearch)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(24, 24))
        self.pushButton.setMaximumSize(QtCore.QSize(24, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border:none;\n"
"background-image: url(:/plus/plus-blue.png);\n"
"}\n"
"QPushButton:hover:!pressed{\n"
" \n"
"    background-image: url(:/plus/plus-red.png);\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea_2.setStyleSheet("\n"
"background-color: rgb(252, 252, 252);\n"
"")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 308, 193))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem1 = QtWidgets.QSpacerItem(20, 172, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.addWidget(self.scrollArea_2)
        self.verticalLayout_8.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.AdvancedSearch)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.map = QtWebEngineWidgets.QWebEngineView(self.groupBox)
        self.map.setMinimumSize(QtCore.QSize(500, 600))
        self.map.setObjectName("map")
        self.verticalLayout.addWidget(self.map)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SearchButton = QtWidgets.QPushButton(self.groupBox)
        self.SearchButton.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SearchButton.setFont(font)
        self.SearchButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SearchButton.setObjectName("SearchButton")
        self.horizontalLayout_2.addWidget(self.SearchButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setMinimumSize(QtCore.QSize(30, 30))
        self.label_3.setMaximumSize(QtCore.QSize(30, 30))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/load/loader.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setMinimumSize(QtCore.QSize(320, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(320, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox_4)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setObjectName("stackedWidget")
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.groupBox_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.SensingCheckBox.toggled['bool'].connect(self.SensingFromDateEdit.setEnabled) # type: ignore
        self.SensingCheckBox.toggled['bool'].connect(self.SensingToDateEdit.setEnabled) # type: ignore
        self.IngestionCheckBox.toggled['bool'].connect(self.IngestionFromDateEdit.setEnabled) # type: ignore
        self.IngestionCheckBox.toggled['bool'].connect(self.IngestionToDateEdit.setEnabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AdvancedSearch.setTitle(_translate("MainWindow", "Расширенный поиск"))
        self.SatelliteLabel.setText(_translate("MainWindow", "Спутниковая система"))
        self.SatelliteComboBox.setItemText(0, _translate("MainWindow", "Landsat 8"))
        self.SatelliteComboBox.setItemText(1, _translate("MainWindow", "Landsat 9"))
        self.SatelliteComboBox.setItemText(2, _translate("MainWindow", "Sentinel-2"))
        self.SensingLabel.setText(_translate("MainWindow", "Период зондирования"))
        self.IngestionLabel.setText(_translate("MainWindow", "Период приема"))
        self.CloudinessLabel.setText(_translate("MainWindow", "Облачность: 0% - 100%"))
        self.label.setText(_translate("MainWindow", "Координаты"))
        self.groupBox.setTitle(_translate("MainWindow", "Область интереса"))
        self.SearchButton.setText(_translate("MainWindow", "Найти"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Результаты"))
import resources.img.Resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
