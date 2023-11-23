# Arom

## Комерческий проект для отслеживания испорченых продуктов

## Проект Arom умеет:

- Отображает продукцию, на которую нужно наклеить 30% стикер
- Отображает продукцию, которую нужно убрать с прилавка
- Добавление новых продуктов доставке
- Удаление уже испортившихся продуктов
- Доступ выдается только админом для сотрудников магазина
- Просмотр и добавление актуальной планограммы

## Развертка уведомления 

Клонируйте репозиторий

```
git clone https://github.com/AlexSimnov/Arom.git
```

## Собирите проект

```
docker build -t your_docker_username/backend ./backend
docker build -t your_docker_username/frontend ./frontend
```
## Настройте docker-compose.yml и .envfile

```
POSTGRES_USER=aroma_user
POSTGRES_PASSWORD=password
POSTGRES_DB=aroma
DB_HOST=db
DB_PORT=5432
```

### Запуск проекта

```
sudo docker compose -f docker-compose.yml pull
sudo docker compose -f docker-compose.yml down
sudo docker compose -f docker-compose.yml up -d
sudo docker compose -f docker-compose.yml exec backend python manage.py migrate
sudo docker compose -f docker-compose.yml exec backend python manage.py collectstatic --no-input
sudo docker compose -f docker-compose.yml exec backend cp -r /app/static/. /app/backend_static/static/
```
