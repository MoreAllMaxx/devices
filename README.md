Для запуска приложения 
1. В папку [devices/devices](devices/devices) добавьте файл settings.py, скопируйте в него содержимое 
файла [settings.py.default](devices/devices/settings.py.default). Добавьте соответствующую информацию 
в SECRET_KEY, DATABASES, REDIS_HOST, REDIS_PORT, REDIS_PASSWORD.
2. Установите необходимые пакеты:

`pip install -r requirements.txt`

3. Включите локально redis-client и postgresql:

`$ sudo service redis-client start`

`$ sudo service postgresql start`

(изменить настройки подключения можно в [settings.py](devices/devices/settings.py))

4. Запустите веб-приложение:

`cd devices`

`python manage.py runserver`

5. По адресу http://127.0.0.1:8000/api/ будет запущена API с заданиями. 
Для удобства также добавил в папке [clients](clients/) клиенты для подключения.

В файлах [10 devices and 15 endpoints.sql](10 devices and 15 endpoints.sql) и 
[query.sql](query.sql) добавил запросы к БД по 2 и 3 заданиям
