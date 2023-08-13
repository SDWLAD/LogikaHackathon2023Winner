from settings import *

class SettingsTab(QDialog):
    '''Клас, який відповідає за показ сторінки "Налаштування" '''
    def __init__(self, mainWidget):
        super().__init__()
        self.mainWidget = mainWidget
        self.setGeometry(150, 150, 300, 200)

        # Створення кнопки збереження
        self.save_button = QPushButton('Зберегти', self)
        self.save_button.clicked.connect(self.save_settings)

        # Створення кнопки імпорту
        self.import_button = QPushButton('Імпортувати', self)
        self.import_button.clicked.connect(lambda: self.load_settings(QFileDialog.getOpenFileName(self, "Виберіть файл")))

        # Створення кнопки експорту
        self.export_button = QPushButton('Екпортувати', self)
        self.export_button.clicked.connect(lambda: self.save_settings(QFileDialog.getExistingDirectory(self, "Виберіть папку")+"settings.json"))

        # Створення головного Layout-у
        layout = QVBoxLayout()

        self.setting_inputs = {}

        # Створення пунктів налаштувань
        for setting in SETTINGS_LIST_ITEMS:
            label = QLabel(setting[1] + ':', self)
            if setting[0] == 'QLineEdit': input_field = QLineEdit(self)
            if setting[0] == 'QCheckBox': input_field = QCheckBox(self)
            input_field.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

            label_input_layout = QHBoxLayout()
            label_input_layout.addWidget(label)
            label_input_layout.addWidget(input_field)

            layout.addLayout(label_input_layout)

            self.setting_inputs[setting[1]] = input_field

        # Розміщення усіх елементів на головному Layout
        layout.addWidget(self.save_button)
        layout.addWidget(self.import_button)
        layout.addWidget(self.export_button)
        self.setLayout(layout)

        self.load_settings() # Завантаження данних

    def load_settings(self, path=SETTINGS_FILE):
        '''Функція, яка відповідає за завантаження данних'''
        try:
            with open(path, 'r', encoding="UTF-8") as file:
                setting = json.load(file)
                for setting_name, input_field in self.setting_inputs.items():
                    value = setting.get(setting_name, '')
                    if isinstance(input_field, QLineEdit):
                        input_field.setText(value)
                    elif isinstance(input_field, QCheckBox):
                        input_field.setChecked(value)
        except:
            self.save_settings()
        self.mainWidget.init_UI()

    def save_settings(self, path=SETTINGS_FILE):
        '''Функція, яка відповідає за збереження данних'''
        settings = {}

        for setting_name, input_field in self.setting_inputs.items():
            if isinstance(input_field, QLineEdit):
                value = input_field.text()
            elif isinstance(input_field, QCheckBox):
                value = input_field.isChecked()
            settings[setting_name] = value
            
        if path:
            with open(path, 'w', encoding="UTF-8") as file:
                json.dump(settings, file)
        else:
            with open(SETTINGS_FILE, 'w', encoding="UTF-8") as file:
                json.dump(settings, file)
        del self.mainWidget.weatherTab
        self.mainWidget.init_UI()
        QMessageBox.information(self, 'Успіх', 'Налаштування збережено.')