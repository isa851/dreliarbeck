
# Backend — готовый скелет проекта

Это **готовая структура (skeleton)** для быстрого старта проектов: от простых сайтов до админок/CRM.

Скелет уже содержит базовую инфраструктуру:

- Docker / docker-compose (отдельно dev и prod)
- Postgres + Redis
- Django backend
- пример отдельного сервиса (telegram bot) в том же образе

## Что нужно настроить под себя

В репозитории используются плейсхолдеры вида `*_dreliar`. Перед стартом желательно заменить их на свои значения.

### 1) Переменные окружения (.env)

В корне `Backend/` есть файл `.envtest` — это пример того, какие переменные нужны.

Сделай файл `.env` на его основе:

```bash
cp .envtest .env
```

Проверь и отредактируй минимум:

- `SECRET_KEY` — ключ Django
- `DEBUG` — `True` только для разработки
- `ALLOWED_HOSTS` — домены/хосты
- `LANGUAGE_CODE`, `TIME_ZONE`
- `PROJECT_DRELIAR` — имя проекта (используется как общий нейминг)

Postgres:

- `POSTGRES_DB` — имя базы
- `POSTGRES_USER` — пользователь
- `POSTGRES_PASSWORD` — пароль
- `POSTGRES_HOST` — **должен совпадать с именем сервиса БД в docker-compose** (по умолчанию `db_dreliar`)
- `POSTGRES_PORT` — обычно `5432` внутри сети docker

### 2) docker-compose: нейминг сервисов/контейнеров/volume/network

Файлы:

- `docker/docker-compose.yml` — dev
- `docker/docker-compose.prod.yml` — prod

Там есть плейсхолдеры, которые стоит заменить под проект:

- `db_dreliar` (service dreliar) — имя сервиса Postgres
- `container_dreliar: postgres_db_dreliar` — имя контейнера Postgres
- `postgres_data_dreliar` — имя volume для данных Postgres
- `redis_dreliar` / `container_dreliar: redis_dreliar` — Redis
- `web_dreliar` / `container_dreliar: django_web_dreliar` — Django контейнер
- `telegram_bot` / `container_dreliar: telegram_bot_dreliar` — бот
- `portfolio_network` / `portfolio_network_dreliar` — docker network

Важно:

- `POSTGRES_HOST` в `.env` должен совпадать с **именем сервиса Postgres** (например `db_dreliar`).
- В dev-compose проброшены порты:
  - Postgres: `5433:5432` (снаружи 5433)
  - Redis: `6389:6379` (снаружи 6389)
  - Django: `127.0.0.1:8084:8082` (снаружи 8084)
  При необходимости поменяй внешние порты, если заняты.

## Структура проекта

- `app/` — Django проект
- `docker/` — Dockerfile и docker-compose
- `scripts/entrypoint.sh` — entrypoint для контейнера
- `.envtest` — пример переменных окружения

## Запуск в разработке (docker-compose)

1) Создай `.env`:

```bash
cp .envtest .env
```

2) Запусти dev-сборку:

```bash
docker compose -f docker/docker-compose.yml up --build
```

По умолчанию `web_dreliar` запускает:

- миграции
- `collectstatic`
- dev server Django на `0.0.0.0:8082` (наружу проброшен `127.0.0.1:8084`)

Открывай:

- `http://127.0.0.1:8084`

## Запуск в продакшне

```bash
docker compose -f docker/docker-compose.prod.yml up --build -d
```

В прод-конфиге `web_dreliar` запускается через gunicorn и слушает `0.0.0.0:8000`.

## Типовые проблемы

- Если Postgres не поднимается — проверь `POSTGRES_*` в `.env` и что `POSTGRES_HOST` совпадает с сервисом БД.
- Если порты заняты — поменяй внешние порты в `docker-compose.yml`.

