# api_yatube

## Описание

*api_yatube* — это веб-приложение, предоставляющее API для управления постами, комментариями и подписками с поддержкой JWT аутентификации. Проект решает задачу организации платформы для обмена контентом, где пользователи могут взаимодействовать с постами и комментариями, а также управлять подписками на других пользователей.

### Основные возможности:

- *Управление JWT токенами*: получение, обновление и проверка токенов для аутентификации пользователей.
- *Доступ для неаутентифицированных пользователей*:
  - Чтение списка и отдельных постов.
  - Чтение списка и отдельных комментариев.
  - Чтение списка сообществ.
- *Функционал для аутентифицированных пользователей*:
  - Чтение, создание, редактирование и удаление собственных постов и комментариев.
  - Ограничение на редактирование и удаление постов и комментариев только владельцами.
  - Создание подписок на других пользователей (кроме себя) без повторений.
  - Просмотр всех подписок и поиск среди них выбранного пользователя.

*api_yatube* полезен для создания социальных платформ, блогов, форумов и других приложений, требующих управлениия контентом с разграничением прав доступа.

## Установка

### Требования

- *Python* версии 3.9

### Шаги установки

1. *Клонирование репозитория*

```bash
git clone git@github.com:Kesh113/api_final_yatube.git
cd postmaster
```

2. *Создание и активация виртуального окружения*

```bash
py -3.9 -m venv venv
source venv/Scripts/activate
```

3. *Установка зависимостей*

```bash
pip install -r requirements.txt
```

4. *Миграции базы данных*

```bash
cd yatube_api
python manage.py migrate
```

5. *Запуск сервера*

```bash
python manage.py runserver
```

Сервер будет доступен по адресу `http://127.0.0.1:8000/`

## Примеры запросов к API

### Аутентификация и получение JWT токена

*Запрос:*

```http
POST /api/v1/jwt/create/
Content-Type: application/json
```

```json
{
  "username": "string",
  "password": "string"
}
```

*Ответ:*

```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}
```

### Обновление JWT токена

*Запрос:*

```http
POST /api/v1/jwt/refresh/
Content-Type: application/json
```

```json
{
  "refresh": "jwt_refresh_token"
}
```

*Ответ:*

```json
{
  "access": "new_jwt_access_token"
}
```

### Получение списка постов (доступно всем)

*Запрос:*

```http
GET /api/v1/posts/
```

*Ответ:*

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    },
    {
      "id": 1,
      "author": "string",
      "text": "string",
      "pub_date": "2023-10-02T08:20:30Z",
      "image": "string",
      "group": 1
    }
  ]
}
```

### Создание нового поста (только для аутентифицированных пользователей)

*Запрос:*

```http
POST /api/v1/posts/
Authorization: Bearer jwt_access_token
Content-Type: application/json
```

```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

*Ответ:*

```json
{
  "id": 2,
  "author": "string",
  "text": "string",
  "pub_date": "2023-10-02T08:20:30Z",
  "image": "string",
  "group": 0
}
```

### Редактирование собственного поста

*Запрос:*

```http
PUT /api/v1/posts/2/
Authorization: Bearer jwt_access_token
Content-Type: application/json
```

```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

*Ответ:*

```json
{
  "id": 2,
  "author": "string",
  "text": "string",
  "pub_date": "2023-10-02T08:20:30Z",
  "image": "string",
  "group": 0
}
```

### Удаление собственного поста

*Запрос:*

```http
DELETE /api/v1/posts/3/
Authorization: Bearer jwt_access_token
```

*Ответ:*

Статус-код ответа 204

### Создание подписки на пользователя

*Запрос:*

```http
POST /api/v1/follow/
Authorization: Bearer jwt_access_token
Content-Type: application/json
```

```json
{
  "following": "string"
}
```

*Ответ:*

```json
{
  "following": "string",
}
```

### Получение списка подписок

*Запрос:*

```http
GET /api/v1/follow/
Authorization: Bearer jwt_access_token
```

*Ответ:*

```json
[
  {
    "user": "string",
    "following": "string"
  },
  {
    "user": "string",
    "following": "string"
  }
]
```

### Поиск подписки по имени пользователя

*Запрос:*

```http
GET /api/v1/follow/?search=root
Authorization: Bearer jwt_access_token
```

*Ответ:*

```json
[
  {
    "user": "string",
    "following": "string"
  }
]
```
