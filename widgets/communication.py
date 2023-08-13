from settings import *

class CommunicationTab(QWidget):
    '''Клас, який відповідає за показ сторінки "Чат-бот" '''
    def __init__(self):
        super().__init__()

        # Створення Layout
        self.main_layout = QVBoxLayout(self)
        self.input_layout = QHBoxLayout()

        # Створення віджетів
        self.list_messages_widget = QListWidget(self)
        self.text_input_edit = QLineEdit(self)
        self.send_button = QPushButton("send", self)
        self.clear_button = QPushButton("clear", self)

        # Розміщення елементів
        self.main_layout.addWidget(self.list_messages_widget)
        self.input_layout.addWidget(self.text_input_edit)
        self.input_layout.addWidget(self.send_button)
        self.input_layout.addWidget(self.clear_button)
        self.main_layout.addLayout(self.input_layout)
        # Під'єднання функцій до кнопок
        self.send_button.clicked.connect(self.send)
        self.send_button.setAutoDefault(True)
        self.text_input_edit.returnPressed.connect(self.send_button.click)
        self.clear_button.clicked.connect(self.clear)

        self.messages = [] # Список усіх повідомлень
        self.load_data() # Завантаження данних

    def clear(self):
        '''Очищення від усіх повідомлень'''
        self.messages = []
        for i in range(self.list_messages_widget.count()):
            (self.list_messages_widget.takeItem(0))
        self.save_data()
    def load_data(self):
        '''Завантаження данних'''
        with open("data/bot_data.txt", encoding='UTF-8') as f:
            for j, i in enumerate(f.readlines()):
                role = "assistant"
                item = QListWidgetItem()
                if j%2==0:
                    item.setTextAlignment(Qt.AlignRight)
                    role = "user"
                self.messages.append({"role": role, "content": i})

                item.setText(self.edit_text(i))
                self.list_messages_widget.addItem(item)
    def save_data(self):
        '''Збереження данних'''
        with open("data/bot_data.txt", mode='w', encoding='UTF-8') as f:
            for i in self.messages:
                data = i["content"].replace("\n", "")
                f.write(data+"\n")
    def send(self):
        '''Функція для надсилання повідомлення'''

        # Виведення на екран запитання
        item = QListWidgetItem()
        item.setTextAlignment(Qt.AlignRight)
        text = self.text_input_edit.text()
        item.setText(self.text_input_edit.text())
        self.list_messages_widget.addItem(item)
        self.text_input_edit.setText("")

        # Створення окремого потоку для роздумів бота
        self.wait_item = QListWidgetItem()
        self.wait_item.setText("Зачекайте, поки буде згенерована відповідь...")
        self.list_messages_widget.addItem(self.wait_item) 

        t = threading.Thread(target=lambda: self.generate_answer(text))
        t.start()

        self.save_data()
    def generate_answer(self, text):
        '''Функція для генерації відповіді'''
        # Генерація відповіді
        self.messages.append({"role": "user", "content": text})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = self.messages)
        reply = chat.choices[0].message.content

        # Показ та озвучування відповіді
        item = QListWidgetItem()

        temp_file = tempfile.NamedTemporaryFile(delete=True)
        gTTS(text=reply, lang='uk').save(f"{temp_file.name}.mp3")
        reply = self.edit_text(reply, 50)
        item.setText(reply)
        self.list_messages_widget.takeItem(self.list_messages_widget.count()-1)
        self.list_messages_widget.addItem(item)

        self.messages.append({"role":"assistant", "content": reply})
        self.save_data()

        with open(SETTINGS_FILE, 'r', encoding="UTF-8") as file:
            setting = json.load(file)[SETTINGS_LIST_ITEMS[0][1]]
            if setting:
                playsound.playsound(f"{temp_file.name}.mp3")

    def edit_text(self, text, max_characters_per_line=50) -> str:
        '''Функція для переносу тексту'''
        words = text.split()  # Розбиваємо текст на окремі слова
        lines = []  # Список рядків
        current_line = ""  # Поточний рядок

        for word in words:
            if len(current_line) + len(word) <= max_characters_per_line:
                current_line += word + " "
            else:
                lines.append(current_line.strip())  # Додаємо поточний рядок до списку рядків
                current_line = word + " "

        lines.append(current_line.strip())  # Додаємо останній поточний рядок до списку рядків

        return "\n".join(lines)  # Об'єднуємо рядки за допомогою символу нового рядка