import os, sys
from PyQt5 import QtGui, QtWidgets, QtWebChannel, QtCore
from PyQt5.QtCore import QDate
from superqt import QDoubleRangeSlider
from shapely.geometry import Polygon
import re
from PyQt5.QtCore import QThread, pyqtSignal


from widgets.MainWindow import Ui_MainWindow
from widgets.LoginWindow import Ui_Form
from widgets.snapshotWidget import Ui_snapshot
from widgets.infoWidget import Ui_Dialog
from widgets.coordsWidget import Ui_Coords
from DataBase import connect, crud


class Backend(QtCore.QObject):
    @QtCore.pyqtSlot(list)
    def getCoord(self, Coord):
        global myCoordList
        coord_tuples = [(d['lat'], d['lng']) for d in Coord[0]]
        myCoordList = []
        for coord in coord_tuples:
            myCoordList.append([coord[0], coord[1]])
        window.showCoords()  
        #QtWebEngineWidgets.QWebEngineView


class QueryThread(QThread):
    progressChanged = pyqtSignal(int)
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
        DBInfoList = []
        index = 0
        my_poly = Polygon(myCoordList)
        self.geojson =  crud.read_table(engine, self.arg1, self.arg2, self.arg3, self.arg4, self.arg5, self.arg6 ,self.arg7)
        for geo in self.geojson:
            result.append([])
            coordinates = re.findall(r"[\d.]+", geo[0])
            for i in range(0, len(coordinates), 2):
                result[index].append([float(coordinates[i+1]), float(coordinates[i])])
            BD_poly = Polygon(result[index])

            if BD_poly.contains(my_poly) or my_poly.contains(BD_poly) or my_poly.intersects(BD_poly):
                    
                
                DBInfoList.append(self.geojson[index])
                
            else:
                result.pop(index)
                index-=1
            index+=1
        self.resultsReady.emit(DBInfoList)
        #self.resultsReady.emit([DBInfoList, widgetsIndex])


class InformWidget(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class CoordsWidget(QtWidgets.QWidget, Ui_Coords):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        



class SnapshotWidget(QtWidgets.QWidget, Ui_snapshot):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.displayPoly)
        self.moreButton.clicked.connect(self.openInfo)


    def displayPoly(self):
        index = window.verticalLayout_4.indexOf(self.sender().parent())
        if self.pushButton.isChecked():
            window.map.page().runJavaScript(f"displayGeoList({result[index]})")
        else:
            latlngs = [f'LatLng({round(lat, 6)}, {round(lng, 6)})' for lat, lng in result[index][:-1]]
            latlng_str = ','.join(latlngs)
            window.map.page().runJavaScript(f"removeGeoList('{latlng_str}')")

    def openInfo(self):
        index = window.verticalLayout_4.indexOf(self.sender().parent())
        print(index)
        window.OpenInfoWindow.show()                                      # Отобразить окно InformWidget
        


class LoginWindow(QtWidgets.QDialog, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Авторизация")
        # self.UserNameLineEdit.setText('students_read_only')
        # self.PasswordLineEdit.setText('Sf_=42jn*^3')
        self.UserNameLineEdit.setText('postgres')
        self.PasswordLineEdit.setText('89519821')
        self.LoginButton.clicked.connect(lambda: self.Authorization(self.UserNameLineEdit.text(), self.PasswordLineEdit.text()))
        self.authorized = False

    # Авторизация пользователя
    ###############################################################
    def Authorization(self, Username, Password):
        global engine
        engine = connect.connect_to_db(Username, Password)
        if engine == False: 
            print("База данных не существует или неверно введено имя пользователя/пароль")
        else:
            self.authorized = True 
            print("Подключение успешно")
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

    def showCoords(self):
        for point in myCoordList:
            self.coords_widget = CoordsWidget(self)

            self.coords_widget.lineEdit.setText(f'{round(point[0], 4)}')
            self.coords_widget.lineEdit_2.setText(f'{round(point[1], 4)}')
            self.verticalLayout_10.insertWidget(0, self.coords_widget)

    def display_coords(self):
        try:
            myCoordList
        except NameError:
            print('Не выделена область поиска!')
        else:
            for point in myCoordList:
                print(point)

    def display_cloud(self):
        min, max = self.DoubleSlider.value()
        self.CloudinessLabel.setText(f"Облачность: {round(min)}% - {round(max)}%")


    def search(self):
        self.map.page().runJavaScript(f"removeAllGeoList()")
        result.clear()
            
        while self.verticalLayout_4.count() != 1:
            widget_item = self.verticalLayout_4.takeAt(0)
            widget = widget_item.widget()
            widget.deleteLater()

        try:
            myCoordList
        except NameError:
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
            self.queryThread.progressChanged.connect(self.onProgressChanged)
            self.queryThread.resultsReady.connect(self.onResultsReady)
            self.queryThread.start()

    def onProgressChanged(self):
        print('start')

    def onResultsReady(self, snapshot):
        for i in range(len(snapshot)):
            print(i)
            self.snapshot = SnapshotWidget(self)
            self.verticalLayout_4.insertWidget(i, self.snapshot)
            
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
    
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())