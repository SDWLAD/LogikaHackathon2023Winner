from settings import *

class EducationTab(QWidget):
    '''Клас, який відповідає за показ сторінки "Цифрові книги" '''
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        

        # Створення віджету для прогортання pdf-файла.
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_widget = QWidget(self)
        self.scroll_widget.setObjectName("ScrollWidget")
        self.scroll_layout = QVBoxLayout()
        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(self.scroll_widget)

        self.coef = 1 # Коєфіцієнт розміру одної сторінки PDF файлу

        buttons_layout = QHBoxLayout()

        # Створення кнопок
        open_button = QPushButton("Відкрити", self)
        download_button = QPushButton("Завантажити", self)
        button_plus = QPushButton("+", self)
        button_plus.setMaximumWidth(20)
        button_minus =QPushButton("-", self)
        button_minus.setMaximumWidth(20)
        self.history_combo_box= QComboBox(self)

    
        # Розміщення елементів
        layout.addWidget(self.scroll_area)
        layout.addLayout(buttons_layout)
        buttons_layout.addWidget(open_button)
        buttons_layout.addWidget(download_button)
        buttons_layout.addWidget(button_plus)
        buttons_layout.addWidget(button_minus)
        layout.addWidget(self.history_combo_box)

        # Під'єднання функцій до кнопок
        open_button.clicked.connect(self.openPDF)
        download_button.clicked.connect(self.openURL)
        button_plus .clicked.connect(self.plus_coef)
        button_minus.clicked.connect(self.minus_coef)
        self.history_combo_box.activated[str].connect(self.on_combo_box_activated)

        self.pdf_images = [] # Список для зберігання створених віджетів
        self.file_path = ''  # Змінна для зберігання шляху до відкритого PDF файлу\

        self.load_history()

    def load_history(self):
        '''Функція для завантаження історії'''
        with open("data/pdf_history_data.txt", 'r', encoding='utf-8') as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines]
            for line in lines:
                self.history_combo_box.addItem(line)
    def on_combo_box_activated(self, text):
        '''Функція, яка відслідковує натискання на якийсь елемент в history_combo_box'''
        index = self.history_combo_box.findText(text)
        self.history_combo_box.removeItem(index)
        self.history_combo_box.insertItem(0, text)
        self.history_combo_box.setCurrentIndex(0)
        if self.file_path != text:
            self.file_path = text
            self.display_pdf(self.file_path)
    def openURL(self):
        '''Функція для відкривання посилань у браузері'''
        webbrowser.open('https://www.junkybooks.com/books')
    def plus_coef(self): 
        '''Функція для збільшення коєфіцієнту розміру одної сторінки'''
        self.coef+=0.25
        self.display_pdf(self.file_path)
        # self.resizePDF()
    def minus_coef(self):
        '''Функція для зменшення  коєфіцієнту розміру одної сторінки'''
        self.coef-=0.25
        self.display_pdf(self.file_path)
        # self.resizePDF()
    def openPDF(self):
        print("Loading...")
        '''Функція, яка отримує шлях до PDF-файла та зберігає історію відкритих файлів'''
        self.file_path = QFileDialog().getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf)")[0]

        if self.file_path:
            history_combo_box_values = [self.history_combo_box.itemText(i) for i in range(self.history_combo_box.count())]

            if self.file_path not in history_combo_box_values: 
                self.history_combo_box.insertItem(0, self.file_path)
                self.history_combo_box.setCurrentIndex(0)
            
            self.display_pdf(self.file_path)
    def display_pdf(self, file_path):
        '''Функція, яка показує PDF-файл'''
        self.clear_images()
        self.doc = fitz.open(file_path)

        for i in range(self.doc.page_count):
            label = QLabel(self)
            self.load_page(i)

        with open("data/pdf_history_data.txt", 'w', encoding='utf-8') as f:
            for index in range(self.history_combo_box.count()):
                f.write(self.history_combo_box.itemText(index)+'\n')
    def load_page(self, i):
        page = self.doc.load_page(i)
        pix = page.get_pixmap()
        image = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)

        label = QLabel(self)
        label.setPixmap(QPixmap.fromImage(image.scaled(int(pix.width*self.coef), int(pix.height*self.coef))))
        
        self.pdf_images.append(label)
        self.scroll_layout.insertWidget(i, label)
    def clear_images(self):
        '''Функція, яка овидаляє зайві сторінки PDF'''
        for i in range(len(self.pdf_images)):
            try:
                self.scroll_layout.removeWidget(self.pdf_images[i-1])
                self.pdf_images[i].deleteLater()
                self.pdf_images.pop(i)
            except IndexError:pass