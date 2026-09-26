# Установка

### Настраиваем `.env файл`. 

В корне проекта файл `.env.example` копируем в `.env` и подставляем актуальные данные:
1) Изменяем `COMPOSE_PROJECT_NAME` на название проекта
2) При необходимости меняем порт (при смене нужно будет поменять порт на нужный в ссылках ниже)



### Поднимаем контейнеры в фоне через docker-compose:

```bash
$ docker-compose up -d --build
```
---


# Интерактивная Swagger-документация:

- **http://127.0.0.1:8000/docs**

---

# Список пользователей:

- **http://127.0.0.1:8000/users**

---



## Как пользоваться API

### Через Swagger (визуально)

1. Откройте **http://127.0.0.1:8000/docs**
2. Нажмите на нужный эндпоинт -> кнопка **"Try it out"**
3. Для `POST /users` введите JSON и нажмите **"Execute"**

### Через curl (терминал)

**Создать пользователя:**
```bash
curl -X POST http://127.0.0.1:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Иван","age":30,"sex":"M","job":"Developer"}'
```

**Получить всех пользователей:**
```bash
curl http://127.0.0.1:8000/users
```


## Структура проекта

```
fastapi-main/

├── app/                         # Основной код приложения
│   ├── __init__.py
│   ├── main.py                  # Точка входа FastAPI
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py            # Маршруты API (эндпоинты)
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py            # Настройки приложения
│   ├── database/
│   │   ├── __init__.py
│   │   └── db.py                # Подключение к базе данных
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py              # SQLAlchemy модель (таблица БД)
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── user_repo.py         # Репозиторий (работа с БД)
│   └── schemas/
│       ├── __init__.py
│       └── user.py              # Pydantic схемы (валидация)

├── docker/                      # Конфигурация для Docker
│   ├── web/                     # Контейнер для основного кода приложения
│   │   ├── Dockerfile           # Конфигурация Docker-образа

├── sqlite/                      # Data для sqlite
│   ├── users.db                 # bd sqlite

             
├── .env.example                 # образец файла для переменных окружения
├── .env                         # файл для переменных окружения
├── Makefile                     # Команды для Docker
├── requirements.txt             # Зависимости Python
├── .dockerignore                # Файлы, исключённые из Docker
└── .gitignore                   # Файлы, исключённые из Git
```
