# Севрис нотификации

## Приложения:
1. [API-сервис приема событий](api/README.md)
2. [Обработчик событий из очереди](worker/README.md)

## Запуск в режиме dev

1. Запустить докер `docker compose -f docker-compose.dev.yml up -d`
2. Запустить [API-сервис приема событий](api/README.md)
3. Запустить [Обработчик событий из очереди](worker/README.md)

## Запуск в режиме prod

1. Запустить докер `docker compose up -d --build`