```mermaid
---
title: Воркер
---
flowchart
    service(UGC, Auth и др. сервисы)
    admin(Админ-панель)
    generator(Генератор\nавтоматических\nсобытий)
    api(API-фасад\nсервиса\nнотификации)
    mq[(RabbitMQ)]
    worker(Воркер)
    db[(База данных\nуведомлений)]
    db_html[(База данных\nшаблонов)]
    client(Клиент)
    
    generator -->|событие| api
    admin -->|событие| api
    service -->|событие| api

    api -->|событие в очередь| mq
    mq -->|события из очереди| worker
    service -->|доп. данные\nдля рассылки| worker
    db_html -->|html-шаблон| worker
    worker -->|добавить уведомление| db
    worker -->|email| client
```

```mermaid
---
title: Генератор автоматических событий
---
flowchart
    service(UGC, Auth и др. сервисы)
    generator(Генератор\nавтоматических\nсобытий)
    api(API-фасад\nсервиса\nнотификации)
    db[(База данных\nуведомлений)]
    q{Данные\nизменились?}
    
    generator -->|сравнение\nданных| q
    service -->|актуальные данные|generator
    db -->|история уведомлений| generator
    q -->|да| api
    q -->|нет| generator   
```

```mermaid
---
title: Админ-панель
---
flowchart
    admin(Админ-панель)
    api(API-фасад\nсервиса\nнотификации)
    db[(База данных\nhtml-шаблонов)]
    
    admin <-->|crud операции| db
    admin -->|событие с ИД шаблона| api
```