from settings import *

class TravelsTab(QWebEngineView):
    '''Клас, який відповідає за показ сторінки "Подорожі" '''
    def __init__(self):
        super().__init__()
        self.setUrl(QUrl("https://www.google.com/travel/"))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)