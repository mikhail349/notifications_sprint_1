Панель администратора для добавления запланированных рассылок и шаблонов для рассылок.

Локальный запуск:

1. Установить зависимости ```pip install requirements.txt```
2. Создать файл .env (по аналогии с .env.example)
3. Собрать статические файлы ```python manage.py collectstatic --no-input```
3. Применить миграции ```python manage.py migrate```
4. Создать пользователя ```python manage.py createsuperuser```

API:

/api/v1/templates/<template_id>: возвращает шаблон сообщения

{"template": ...}
