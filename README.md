# README для проекта «Новостной портал на Django»
## Описание

Проект представляет собой веб-приложение новостного портала с функционалом публикации новостей и статей, подписки пользователей на категории, оценкой постов и комментариев, а также отправкой уведомлений по email о новых публикациях.

## Особенности проекта:

Аутентификация и регистрация пользователей через Django Allauth (email-based)

Разграничение прав доступа (редактирование, удаление, создание постов для авторов)

Разделение контента на категории: новости и статьи

Подписка на категории и уведомления на email о новых постах

Система лайков/дизлайков для постов и комментариев

Фильтры для поиска и сортировки новостей

Логирование ошибок, событий и безопасности

Периодические задачи через Celery и Redis (очередь задач)

Административная панель Django для управления контентом и пользователями

## Технологии

Python 3.10+

Django 4.x

Django Filters

Django Allauth

Celery + Redis

SQLite (можно заменить на PostgreSQL)

HTML, CSS (шаблоны Django)

## Установка

Клонируйте репозиторий:
git clone <repo_url>
cd project


Создайте и активируйте виртуальное окружение:
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


Установите зависимости:
pip install -r requirements.txt


Настройте .env файл с SECRET_KEY и email:

SECRET_KEY=YOUR_SECRET_KEY
EMAIL_HOST_USER=YOUR_EMAIL
PASSWORD=YOUR_EMAIL_PASSWORD
EMAIL=YOUR_DEFAULT_FROM_EMAIL


Примените миграции:
python manage.py migrate


Создайте суперпользователя:
python manage.py createsuperuser


Запустите сервер:
python manage.py runserver

Запуск Celery
celery -A project worker -l info

Запуск Redis
redis-server
