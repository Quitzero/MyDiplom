import os, sys
from PyQt5 import QtWidgets, QtWebChannel, QtCore, QtGui
from PyQt5.QtCore import QDate, QThread, pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QProgressBar
from superqt import QDoubleRangeSlider
from shapely.geometry import Polygon, LineString, Point
from PyQt5.QtGui import QDoubleValidator, QMovie, QPixmap
import configparser
import keyring
import re
import zipfile
import py7zr

from widgets.MainWindow import Ui_MainWindow
from widgets.LoginWindow import Ui_Form
from widgets.snapshotWidget import Ui_snapshot
from widgets.infoWidget import Ui_Dialog
from widgets.coordsWidget import Ui_Coords
from widgets.addCoordsWidet import Ui_CoordsDialog
from widgets.pageWidget import Ui_Page
from widgets.errorDrive import Ui_error
from NetworkDrive import connectDrive
import dataBaseFolder.connect
import dataBaseFolder.crud


class Backend(QtCore.QObject):
    @QtCore.pyqtSlot(list)
    def getCoord(self, Coord):
        coord_tuples = [(d['lat'], d['lng']) for d in Coord[0]]
        window.myCoordList = []
        for coord in coord_tuples:
            window.myCoordList.append([coord[0], coord[1]])
        window.showCoords() 
        #QtWebEngineWidgets.QWebEngineView


class QueryThread(QThread):
    resultsReady = pyqtSignal(list)

    def __init__(self, dataset_satellite, Sensing_date_from, Sensing_date_to, cloudiness_min, cloudiness_max, Ingestion_date_from, Ingestion_date_to ,parent=None):
        super().__init__(parent)
        self.arg1 = dataset_satellite
        self.arg2 = Sensing_date_from
        self.arg3 = Sensing_date_to
        self.arg4 = cloudiness_min
        self.arg5 = cloudiness_max
        self.arg6 = Ingestion_date_from
        self.arg7 = Ingestion_date_to

    def run(self):
        if len(window.myCoordList) == 1:
            my_poly = Point(window.myCoordList)
        elif len(window.myCoordList) == 2:
            my_poly = LineString(window.myCoordList)
        else:
            my_poly = Polygon(window.myCoordList)
        self.geojson = dataBaseFolder.crud.read_table(engine, self.arg1, self.arg2, self.arg3, self.arg4, self.arg5, self.arg6 ,self.arg7)

        window.DBInfoList = []
        index = 0
        for geo in self.geojson:
            window.DBInfoList.append([])
            coordinates = re.findall(r"[\d.]+", geo[0])
            coordinatesList = []
            for i in range(0, len(coordinates), 2):
                coordinatesList.append([float(coordinates[i+1]), float(coordinates[i])])
            BD_poly = Polygon(coordinatesList)
            if BD_poly.contains(my_poly) or my_poly.contains(BD_poly) or my_poly.intersects(BD_poly):
                window.DBInfoList[index].append(coordinatesList)
                for value in range(2, len(geo),1):
                    window.DBInfoList[index].append(geo[value])
                index+=1
            else:
                window.DBInfoList.pop(index)

        window.PageСontent = [window.DBInfoList[i:i+10] for i in range(0, len(window.DBInfoList), 10)]

        self.resultsReady.emit(window.PageСontent)

        
class QueryThread_Drive(QThread):
    resultsReady = pyqtSignal(bool)
    def __init__(self, uername, password, parent=None):
        super().__init__(parent)
        self.uername = uername
        self.password = password

    def run(self):
        results = connectDrive(f'{self.uername}', f'{self.password}')
        self.resultsReady.emit(results)


class CopyThread(QThread):
    progressChanged = pyqtSignal(bool)

    def __init__(self, source, destination):
        super().__init__()
        self.source = source
        self.destination = destination

    def run(self):
        meta = fr'{self.source}'
        extension = meta.split('.')[-1]
        if extension == 'zip':
            self.progressChanged.emit(False)
            with zipfile.ZipFile(meta, 'r') as archive:
                archive.extractall(self.destination)
                self.progressChanged.emit(True)
        else:
            self.progressChanged.emit(False)
            with py7zr.SevenZipFile(self.source, 'r') as archive:
                archive.extractall(self.destination)
                self.progressChanged.emit(True)


class ErrorWidget(QtWidgets.QDialog, Ui_error):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.myConnectDrive)

    def myConnectDrive(self):
        window.pushButton_2.setEnabled(False)
        window.label_3.setVisible(True)
        window.queryThreadDrive = QueryThread_Drive(self.lineEdit.text(), self.lineEdit_2.text(), window)
        window.queryThreadDrive.resultsReady.connect(window.onLoadReady)
        window.queryThreadDrive.start()
        window.startAnimation()
        window.pushButton_2.setText("Идет подключение к сетевым дискам...")
        self.close()
    
class InformWidget(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
      

class AddCoordsDialog(QtWidgets.QDialog, Ui_CoordsDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Добавление координат")
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.pushButton.clicked.connect(self.addCoords)

        validator = QDoubleValidator()
        validator.setNotation(QDoubleValidator.StandardNotation)
        validator.setDecimals(6)
        self.lineEdit.setValidator(validator)
        self.lineEdit_2.setValidator(validator)
        
    
    def addCoords(self):
        self.lat = self.lineEdit.text().replace(',', '.')
        self.lng = self.lineEdit_2.text().replace(',', '.')
        window.coords_widget = CoordsWidget(self)
        window.coords_widget.lineEdit.setText(f'{self.lat}')
        window.coords_widget.lineEdit_2.setText(f'{self.lng}')
        index = window.verticalLayout_10.count() - 1
        window.verticalLayout_10.insertWidget(index, window.coords_widget)
        window.myCoordList = []
        for index in range(window.verticalLayout_10.count() - 1):
            window.myCoordList.append([])
            widget = window.verticalLayout_10.itemAt(index).widget()
            window.myCoordList[index].append(float(widget.lineEdit.text()))
            window.myCoordList[index].append(float(widget.lineEdit_2.text()))
        window.map.page().runJavaScript(f"setNewBounds({window.myCoordList})")
        self.close()


class PageWidget(QtWidgets.QWidget, Ui_Page):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.next.clicked.connect(self.nextPage)
        self.back.clicked.connect(self.previousPage)

    def nextPage(self):
        if len(window.PageСontent) < window.stackedWidget.currentIndex()+2:
            pass
        else:
            window.page = PageWidget(window)
            window.stackedWidget.addWidget(window.page)
            if window.stackedWidget.widget(window.stackedWidget.currentIndex()+1).verticalLayout_4.count() != 1:
                pass
            else:
                for i in range(len(window.PageСontent[window.stackedWidget.currentIndex()+1])):
                        window.snapshot = SnapshotWidget(window)
                        window.stackedWidget.widget(window.stackedWidget.currentIndex()+1).verticalLayout_4.insertWidget(i, window.snapshot)
            window.stackedWidget.setCurrentIndex(window.stackedWidget.currentIndex()+1)
            window.stackedWidget.widget(window.stackedWidget.currentIndex()).label_2.setText(f'{window.stackedWidget.currentIndex()+1} из {len(window.PageСontent)}')


    def previousPage(self):
        window.stackedWidget.setCurrentIndex(window.stackedWidget.currentIndex()-1)
        window.stackedWidget.widget(window.stackedWidget.currentIndex()).label_2.setText(f'{window.stackedWidget.currentIndex()+1} из {len(window.PageСontent)}')

class CoordsWidget(QtWidgets.QWidget, Ui_Coords):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.removeWidget)

    def removeWidget(self):
        index = window.verticalLayout_10.indexOf(self.sender().parent())
        widgetToRemove = window.verticalLayout_10.takeAt(index)
        widget = widgetToRemove.widget()
        widget.deleteLater()
        window.myCoordList = []
        for index in range(window.verticalLayout_10.count() - 1):
            window.myCoordList.append([])
            widget = window.verticalLayout_10.itemAt(index).widget()
            window.myCoordList[index].append(float(widget.lineEdit.text()))
            window.myCoordList[index].append(float(widget.lineEdit_2.text()))
        window.map.page().runJavaScript(f"setNewBounds({window.myCoordList})")


class SnapshotWidget(QtWidgets.QWidget, Ui_snapshot):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.displayPoly)
        self.moreButton.clicked.connect(self.openInfo)
        self.LoadButton.clicked.connect(self.download)
        self.label.setVisible(False)
        if window.status == False:
            self.LoadButton.setToolTip("Не подключены сетевые диски!")
        else:
            self.LoadButton.setToolTip("Загрузить на устройство")
        
    def download(self):
        if window.status == False:
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Не подключены сетевые диски", QtWidgets.QMessageBox.Ok)
        else:
            index = window.stackedWidget.widget(window.stackedWidget.currentIndex()).verticalLayout_4.indexOf(self.sender().parent())
            openPage = window.stackedWidget.currentIndex()
            path = window.PageСontent[openPage][index][13]
            dir_path, file_name = os.path.split(path)
            meta = fr'{dir_path}\{file_name}'
            fname = QFileDialog.getExistingDirectory(self, 'Сохранить', '/')
            if fname == '':
                pass
            else:
                self.copy_thread = CopyThread(f'{meta}', f'{fname}')
                self.copy_thread.progressChanged.connect(self.update_progress)
                self.copy_thread.start()

    def update_progress(self, status):
        if status == False:
            print('open')
            self.label.setVisible(True)
        else:
            print('close')
            self.label.setVisible(False)


    def displayPoly(self):
        index = window.stackedWidget.widget(window.stackedWidget.currentIndex()).verticalLayout_4.indexOf(self.sender().parent())
        openPage = window.stackedWidget.currentIndex()
        if self.pushButton.isChecked():
            window.map.page().runJavaScript(f"displayGeoList({window.PageСontent[openPage][index][0]})")
        else:
            latlngs = [f'LatLng({round(lat, 6)}, {round(lng, 6)})' for lat, lng in window.PageСontent[openPage][index][0][:-1]]
            latlng_str = ','.join(latlngs)
            window.map.page().runJavaScript(f"removeGeoList('{latlng_str}')")

    def openInfo(self):
        index = window.stackedWidget.widget(window.stackedWidget.currentIndex()).verticalLayout_4.indexOf(self.sender().parent())
        openPage = window.stackedWidget.currentIndex()
        window.OpenInfoWindow.satellite.setText(f'{window.PageСontent[openPage][index][1]}')
        window.OpenInfoWindow.SceneIdentifier.setText(f'{window.PageСontent[openPage][index][2]}')
        window.OpenInfoWindow.sensingTime.setText(f'{window.PageСontent[openPage][index][4]}')
        window.OpenInfoWindow.creationTime.setText(f'{window.PageСontent[openPage][index][5]}')
        window.OpenInfoWindow.cloudPercentage.setText(f'{window.PageСontent[openPage][index][10]}')
        window.OpenInfoWindow.forestid.setText(f'{window.PageСontent[openPage][index][12]}')
        path = window.PageСontent[openPage][index][13]
        dir_path, file_name = os.path.split(path)
        window.OpenInfoWindow.Directory.setText(f'{dir_path}')
        window.OpenInfoWindow.show()


class LoginWindow(QtWidgets.QDialog, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Авторизация")
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.config = configparser.ConfigParser()  # создаём объекта парсера
        self.config.read(".ini")  # читаем конфиг
        self.service_id = "my_service"
        self.username = self.config["Database"]["USERNAME"]
        

        if self.config["App"]["REMEMBERME"] == 'True':
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)

        if self.username != '':
            self.UserNameLineEdit.setText(f'{self.config["Database"]["USERNAME"]}')
            password = keyring.get_password(self.service_id, self.username)
            self.PasswordLineEdit.setText(f'{password}')

        self.LoginButton.clicked.connect(lambda: self.Authorization(self.UserNameLineEdit.text(), self.PasswordLineEdit.text()))
        self.authorized = False

    # Авторизация пользователя
    ###############################################################
    def Authorization(self, Username, Password):
        global engine
        self.password = self.PasswordLineEdit.text()
        engine = dataBaseFolder.connect.connect_to_db(Username, Password)
        if engine == False:
            self.UserNameLineEdit.setStyleSheet(stylesheet)
            self.PasswordLineEdit.setStyleSheet(stylesheet)
            self.ErrorLabel.setText("Неверно введено имя пользователя/пароль")
        else:

            if self.checkBox.isChecked() == True:
                self.config["Database"]["USERNAME"] = self.UserNameLineEdit.text()
                self.config["App"]["REMEMBERME"] = 'True'
                keyring.set_password(self.service_id, self.username, self.password)
            else:
                self.config["Database"]["USERNAME"] = ''
                self.config["App"]["REMEMBERME"] = 'False'
                try:
                    keyring.delete_password(self.username, self.password)
                except:
                    pass
            with open('.ini', 'w') as config_file:
                self.config.write(config_file)
            
            self.authorized = True 
            print("Подключение успешно")
            window.queryThreadDrive = QueryThread_Drive(window, None, None)
            window.queryThreadDrive.resultsReady.connect(window.onLoadReady)
            window.queryThreadDrive.start()
            window.startAnimation()
            window.pushButton_2.setText("Идет подключение к сетевым дискам...")
            self.close()

    def closeEvent(self, event):
        if self.authorized == True:                                     # Проверка авторизации пользователя
            print(f'Состояние пользователя: {self.authorized}')
        else:
            self.parent().close()        # Если пользователь не авторизован, то закрыть так же родительское окно
            print('Работа завершена! (Login Window)')

            
class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Главное окно")
        self.is_first_show = True
        self.SensingFromDateEdit.setDate(QDate.currentDate())
        self.SensingToDateEdit.setDate(QDate.currentDate())
        self.IngestionFromDateEdit.setDate(QDate.currentDate())
        self.IngestionToDateEdit.setDate(QDate.currentDate())
        
        self.OpenInfoWindow = InformWidget(self)
        self.OpenInfoWindow.setWindowModality(QtCore.Qt.WindowModal)

        self.OpenCoordsWindow = AddCoordsDialog(self)
        self.OpenCoordsWindow.setWindowModality(QtCore.Qt.WindowModal)
        self.movie = QMovie("resources\img\loader.gif")
        self.label_3.setMovie(self.movie)
        self.pushButton_2.setEnabled(False)

        #Добавление QDoubleRangeSlider
        #########################################################################################
        self.DoubleSlider = QDoubleRangeSlider(QtCore.Qt.Orientation.Horizontal)
        self.DoubleSlider.setRange(0, 100)
        self.DoubleSlider.setValue((0, 100))
        self.DoubleSlider.valueChanged.connect(self.display_cloud)
        self.verticalLayout_7.addWidget(self.DoubleSlider)


        #Отображение карты leaflet
        #########################################################################################
        self.current_dir = os.path.dirname(os.path.realpath(__file__))          # Получение расположения текущей папки
        self.filename = os.path.join(self.current_dir, "./map/index.html")      # Создания пути до html файла
        self.url = QtCore.QUrl.fromLocalFile(self.filename)                     # Преобразования файла в QUrl
        self.map.load(self.url)                                                 # Загрузка файла
        self.map.setContextMenuPolicy(QtCore.Qt.NoContextMenu)                  # Отключить контекстное меню

        #Backend
        #########################################################################################
        self.backend = Backend()
        self.channel = QtWebChannel.QWebChannel()
        self.map.page().setWebChannel(self.channel)
        self.channel.registerObject("backend", self.backend)

        #Подключение функций к кнопкам
        #########################################################################################
        self.SearchButton.clicked.connect(self.search)
        self.pushButton.clicked.connect(self.display_coords)
        self.pushButton_2.clicked.connect(self.openErrorWindow)


    def openErrorWindow(self):
        self.OpenErrorWindow = ErrorWidget(self)
        self.OpenErrorWindow.setWindowModality(QtCore.Qt.WindowModal)
        self.OpenErrorWindow.show()

    def startAnimation(self):
        self.movie.start()
  
    def stopAnimation(self):
        self.movie.stop()

    def showCoords(self):
        while self.verticalLayout_10.count() != 1:
                widget_coords_item = self.verticalLayout_10.takeAt(0)
                widget = widget_coords_item.widget()
                widget.deleteLater()

        index = 0 
        for point in self.myCoordList:
            self.coords_widget = CoordsWidget(self)
            self.coords_widget.lineEdit.setText(f'{round(point[0], 6)}')
            self.coords_widget.lineEdit_2.setText(f'{round(point[1], 6)}')
            self.verticalLayout_10.insertWidget(index, self.coords_widget)
            index+=1


    def display_coords(self):
        self.OpenCoordsWindow.show()


    def display_cloud(self):
        min, max = self.DoubleSlider.value()
        self.CloudinessLabel.setText(f"Облачность: {round(min)}% - {round(max)}%")


    def search(self):
        self.map.page().runJavaScript(f"removeAllGeoList()")
        result.clear()
        
        try:
            self.myCoordList
        except AttributeError:
            print('Не выделена область поиска!')
        else:
            print('-'*5 + 'Параметры' + '-'*5)

            #Спутниковая система
            dataset_satellite = self.SatelliteComboBox.currentText()
            print(f'Спутник: {dataset_satellite}')

            #Период зондирования
            if self.SensingCheckBox.isChecked() == False:
                Sensing_date_from = None
                Sensing_date_to = None
            else:
                Sensing_date_from = self.SensingFromDateEdit.date().toPyDate()
                Sensing_date_to = self.SensingToDateEdit.date().toPyDate()
                print(f'Период зондирования:\nОт: {Sensing_date_from} До: {Sensing_date_to}')

            #Период приема
            if self.IngestionCheckBox.isChecked() == False:
                Ingestion_date_from = None
                Ingestion_date_to = None
            else:
                Ingestion_date_from = self.IngestionFromDateEdit.date().toPyDate()
                Ingestion_date_to = self.IngestionToDateEdit.date().toPyDate()
                print(f'Период приема:\nОт: {Ingestion_date_from} До: {Ingestion_date_to}')

            #Облачность
            cloudiness_min, cloudiness_max = self.DoubleSlider.value()
            print(f'Облачность: {round(cloudiness_min)}% - {round(cloudiness_max)}%')
            print('='*5 + 'Результат' + '='*5)
            self.queryThread = QueryThread(dataset_satellite, Sensing_date_from, Sensing_date_to, cloudiness_min, cloudiness_max, Ingestion_date_from, Ingestion_date_to, self)
            self.queryThread.resultsReady.connect(self.onResultsReady)
            self.queryThread.start()

    def onLoadReady(self, connectStatus):
        self.status = connectStatus
        self.stopAnimation()
        self.label_3.setVisible(False)
        if self.status == False:
            #-----------
            self.pushButton_2.setText("Ошибка подключения к дискам!")
            self.pushButton_2.setEnabled(True)
            self.pushButton_2.setStyleSheet(stylesheetDrive)
        else:
            self.pushButton_2.setEnabled(False)
            self.pushButton_2.setText("")

    def onResultsReady(self, snapshot):
        while self.stackedWidget.count() > 0:
                widget = self.stackedWidget.widget(0)
                self.stackedWidget.removeWidget(widget)
                widget.deleteLater()
        if snapshot == []:
            print('Ничего не найдено!')
        else:
            
            self.page = PageWidget(self)
            self.stackedWidget.addWidget(self.page)

            self.stackedWidget.widget(0).label_2.setText(f'{self.stackedWidget.currentIndex()+1} из {len(self.PageСontent)}')

            for i in range(len(self.PageСontent[0])):
                self.snapshot = SnapshotWidget(self)
                self.stackedWidget.widget(0).verticalLayout_4.insertWidget(i, self.snapshot)

            
    def showEvent(self, event):
        print('Открыто окно! (Main Window)')
        if self.is_first_show == True:
            self.OpenModalWindow = LoginWindow(self)
            self.OpenModalWindow.setWindowModality(QtCore.Qt.WindowModal)    # Задать окно LoginWindow как модальное
            self.OpenModalWindow.show()                                      # Отобразить окно LoginWindow
            self.is_first_show = False
        else:
            pass


if __name__ == "__main__":
    result = []
    stylesheet = '''
                QLineEdit{
                    border:2px solid rgb(250, 50, 50);
                    border-radius:5px;
                    background-color: rgb(250, 250, 250);
                }
                QLineEdit:focus{
                    border:3px solid rgb(255, 138, 138);;
                    border-radius:5px;
                }
                '''
    stylesheetDrive = '''
                QPushButton{
                    background-color: rgb(255, 255, 255);
                    border:none;
                }
                QPushButton:hover{
                    color: rgb(1, 196, 255);
                    text-decoration: underline;
                }
    '''
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())