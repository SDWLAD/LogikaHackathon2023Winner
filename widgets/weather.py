from settings import *

class WeatherTab(QWidget):
    '''Клас, який відповідає за показ сторінки "Погода" '''
    def __init__(self):
        super().__init__()

        # Створення головного Layout
        mainLayout = QVBoxLayout(self)

        try:
            with open(SETTINGS_FILE, 'r', encoding="UTF-8") as file:
                data = json.load(file)
                place = data[SETTINGS_LIST_ITEMS[2][1]] + ", Україна"
                city = data[SETTINGS_LIST_ITEMS[2][1]]
            mgr = owm.weather_manager()

            observation = mgr.weather_at_place(place)  

        except: 
            raise PermissionError("Перевірте підключення до інтернету")
        # Визначення погоди
        w = observation.weather
        status = w.detailed_status
        temp = w.temperature('celsius')['temp']
        humidity = w.humidity
        wind_speed = w.wind()['speed']

        # Створення UI елементів
        background_widget = QWidget(self)
        background_widget.setObjectName("WeatherBackground")
        weather_label = QLabel(f"У місті {city} зараз {status}", self)
        temp_label = QLabel(f"Температура повітря {str(round(temp))}°C", self)
        humidity_label = QLabel(f"Вологість повітря {str(humidity)}%", self)
        wind_speed_label = QLabel(f"Швидкість вітру {str(wind_speed)} м/с", self)
        weather_label.setAlignment(Qt.AlignCenter)
        temp_label.setAlignment(Qt.AlignCenter)
        humidity_label.setAlignment(Qt.AlignCenter)
        wind_speed_label.setAlignment(Qt.AlignCenter)

        # Розміщення UI елементів
        layout = QVBoxLayout()
        layout.addWidget(weather_label)
        layout.addWidget(temp_label)
        layout.addWidget(humidity_label)
        layout.addWidget(wind_speed_label)
        background_widget.setLayout(layout)
        
        mainLayout.addWidget(background_widget)