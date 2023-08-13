from settings import *

class MenuTab(QWidget):
    '''Клас, який відповідає за показ головного меню'''
    def __init__(self, mainWidget):
        super().__init__()
        layout = QVBoxLayout(self)

        # Список, який зберігає назви усіх кнопок у меню
        names = ["Подорожі", "Погода", "Цифрові книги", "Чат-бот", "Налаштування"]

        menu_buttons = [QPushButton(i, self) for i in names] # Створення кнопок

        # Встановлення мінімальних та максимальних розмірів кнопки
        for i in menu_buttons:
            i.setMinimumHeight(100)
            # i.setMaximumSize(400, 400)
            i.setStyleSheet("border-radius:50px")

        # Під'єднання до кнопки функції переходу на іншу сторінку
        menu_buttons[0].clicked.connect(lambda: mainWidget.changeTab(0)) 
        menu_buttons[1].clicked.connect(lambda: mainWidget.changeTab(1)) 
        menu_buttons[2].clicked.connect(lambda: mainWidget.changeTab(2)) 
        menu_buttons[3].clicked.connect(lambda: mainWidget.changeTab(3)) 
        
        # Відкриття окремого вікна налаштувань
        menu_buttons[4].clicked.connect(lambda: mainWidget.settingsTab.exec_()) 
        
        # Розміщення кнопок
        [layout.addWidget(i) for i in menu_buttons]