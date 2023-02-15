# Севрис нотификации

- [Ссылка](https://github.com/mikhail349/notifications_sprint_1) на этот репозиторий
- [Ссылка](https://github.com/mikhail349/Auth_sprint_2) на репозиторий auth-сервиса

## Приложения:
1. [API-сервис приема событий](api/README.md)
2. [WebSocket-сервис для отравки сообщений](ws/README.md)
3. [Обработчик событий из очереди](worker/README.md)
4. [Генератор автоматических событий](scheduler/README.md)
5. [Панель администратора](admin_panel/README.md)

## Запуск в режиме dev

1. Создать файл `.env` с переменными окружения по аналогии с файлом `.env.example`
2. Запустить докер `docker compose -f docker-compose.dev.yml up -d`
3. Запустить [API-сервис приема событий](api/README.md)
4. Запустить [WebSocket-сервис для отравки сообщений](ws/README.md)
5. Запустить [Обработчик событий из очереди](worker/README.md)
6. Запустить [Генератор автоматических событий](scheduler/README.md)
7. Запустить [Панель администратора](admin_panel/README.md)

## Запуск в режиме prod

1. Создать файл `.env` с переменными окружения по аналогии с файлом `.env.example`
2. Запустить докер `docker compose up -d --build`