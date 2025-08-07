## Запуск

1. Заполнить .env файл.
2. Применить миграции `python manage.py migrate`.
3. Запуск сервера (можно тестового) `python manage.py runserver`.
4. Запуск Celery `celery -A config worker -l INFO` или `celery -A config worker -l INFO -P gevent`.
5. Запуск Redis - любым удобным способом.
