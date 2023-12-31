# OptiUkraine 2100

"OptiUkraine 2100" - це десктопний додаток, який створений щоб полегшити життя сучасного українця у далекому майбутньому.

![Image alt](https://github.com/SDWLAD/LogikaHackathon2023Winner/blob/main/screenshots/1.png)

## Встановлення
```pwsh
pip install PyQt5, PyQtWebEngine, PyMuPDF, openAI, gTTS, pyowm, playsound==1.2.2
```

## Про цей додаток
У цьому додатку є 4 основні функції, а саме подорожі, цифрові книги, погода та чат-бот.

Вкладка "Подорожі", це PyQtWebEngine із завантаженою сторінкою Google travels. Для використання PyQtWebEngine потрібно його встановити за допомогою pip. Тут ви можете знайти місце для подорожі та замовити білет.

![Image alt](https://github.com/SDWLAD/LogikaHackathon2023Winner/blob/main/screenshots/2.png)


Вкладка "Погода" може показати ваам погоду, температуру повітря, вологу повітря та швидкість вітру. Для встановлення місця розташування потрібно зайти в налаштування. Для роботи програми встановіть pyowm. Якщо у вас не запускається програма спробуйте вписати свій OpenWeatherMapAPI код.

![Image alt](https://github.com/SDWLAD/LogikaHackathon2023Winner/blob/main/screenshots/3.png)

Вкладка "Цифрові книги", це вкладка, у якій ви можете відкривати PDF файли. Також тут ви можете його завантажити з сайту junkybooks.com. І вам не потрібно кожен раз при запуску застосунку. Усі відкриті файли зберігаються в історії. Для Роботи програми вам потрібно встановити PyMuPDF.

![Image alt](https://github.com/SDWLAD/LogikaHackathon2023Winner/blob/main/screenshots/4.png)

Вкладка "Чат-бот" виконує функцію бота-помічника. У ролі цього бота використовується ChatGPT. Усі повідомлення та розмови зберігаються. Для очистки історії є кнопка "clear". Також бот може озвучувати свої повідомлення за допомогою gTTS та playsound==1.2.2. Для роботи потрібно встановити ці бібліотеки, а також бібліотеку OpenAI для самого ChatGPT. Якщо у вас не працює додаток, спробуйте вписати свій OpenAI API Key.
![Image alt](https://github.com/SDWLAD/LogikaHackathon2023Winner/blob/main/screenshots/5.png)
