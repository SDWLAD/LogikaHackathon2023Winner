from PyQt5.QtWebEngineWidgets import QWebEngineView 
from pyowm.utils.config import get_default_config
from PyQt5.QtGui import QImage, QPixmap
from pyowm.utils import timestamps
from pyowm.utils import config
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import Qt
from pyowm import OWM
from gtts import gTTS
import webbrowser
import threading
import playsound
import tempfile
import openai
import json
import fitz
import csv 

# Впишіть свій код від openAI-API, та OpenWeatherMap
openai.api_key = "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"
owm = OWM('c4bb700a457b50d5c8702a4cb696837b')

SETTINGS_LIST_ITEMS = [ # Список елементів налаштувань
    ('QCheckBox','Озвучування тексту бота'),
    ('QCheckBox','Світла тема'),
    ('QLineEdit','Місто проживання'),
]

SETTINGS_FILE = 'data/settings.json'

# Встановлення місця розташування
config_dict = get_default_config()
config_dict['language'] = 'ua'
