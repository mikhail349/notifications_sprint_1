# Панель администратора для добавления запланированных рассылок и шаблонов для рассылок.

## Локальный запуск:

1. Установить зависимости ```pip install requirements.txt```
2. Создать файл .env (по аналогии с .env.example)
3. Собрать статические файлы ```python manage.py collectstatic --no-input```
4. Применить миграции ```python manage.py migrate```
5. Создать пользователя ```python manage.py createsuperuser```
6. Запустить приложение ```python manage.py runserver```

## API:

1. `/api/v1/templates/<template_id>/` возвращает шаблон сообщения 
```
{"template": ...}
```

2. `api/v1/configs/<config_name>/` возвращает значение конфигурации
```
{"<config_name>": ...}
```
