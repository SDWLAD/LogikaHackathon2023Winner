from settings import *
# Імпорт важливих класів
from widgets.qsettings import SettingsTab
from widgets.communication import CommunicationTab
from widgets.travels import TravelsTab
from widgets.menu import MenuTab
from widgets.education import EducationTab
from widgets.weather import WeatherTab
import sys

class MainWindow(QMainWindow):
    '''Головний клас програми, який 
       відповідає за головне вікно та 
       розміщеня інших сторінок'''
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.Drawer)

        # Налштування вікна
        self.setMinimumSize(540, 650)
        self.resize(540, 650)
        self.setWindowTitle("OptiUkraine 2100")
        self.setObjectName("MainWindow")

        # Створення найважливіших віджетів
        self.tabWidget = QTabWidget(self)
        self.settingsTab = SettingsTab(self)
        self.create_back_button()

        self.setCentralWidget(self.tabWidget)
        self.show() #Показ екрана
    
    def init_UI(self):
        '''Функція, яка налаштовує UI програми, та систему показу сторінок додатка'''

        with open(SETTINGS_FILE, 'r', encoding="UTF-8") as file:
            setting = json.load(file)[SETTINGS_LIST_ITEMS[1][1]]
            if setting: self.setStyleSheet(open("light_theme_style.css", "r").read())
            else: self.setStyleSheet(open("dark_theme_style.css", "r").read())

        self.setObjectName("MainTabWidget")
        
        self.menuTab = MenuTab(self)
        self.travelsTab = TravelsTab()
        self.educationTab = EducationTab()
        self.weatherTab = WeatherTab()
        self.communicationTab = CommunicationTab()

        self.tabWidget.addTab(self.menuTab, "0")
        self.tabWidget.addTab(self.travelsTab, "1")
        self.tabWidget.addTab(self.weatherTab, "2")
        self.tabWidget.addTab(self.educationTab, "3")
        self.tabWidget.addTab(self.communicationTab, "4")
        self.tabWidget.tabBar()

        self.tabWidget.tabBar().hide()

    def create_back_button(self):
        '''Функція, яка створює кнопку "Назад"'''
        self.back_button = QPushButton("❮", self)
        self.back_button.move(-100, -100)
        self.back_button.resize(20, 21)
        self.back_button.clicked.connect(lambda: self.changeTab(-1))

    def changeTab(self, tab):
        '''Змінює сторінку (вкладку) в програмі'''
        self.tabWidget.setCurrentIndex(tab+1)
        if tab == -1: 
            self.back_button.move(-100, -100)
        else: self.back_button.move(1, 1)

# Запуск програми
if __name__ == '__main__':
    app = QApplication(sys.argv)
    sc = MainWindow()
    app.exec_()
    exit()