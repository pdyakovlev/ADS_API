# Важная информация:
### Проект реализован на FastAPI.
### Для удобства база с данными закинута сразу в репозиторий.
### Пользователи и разграничение доступа реализовано с использованием библиотеки FastAPI Users:
В базе данных содержится два пользователя: \
superuser - username: super@user.com, пароль: pass \
обычный пользователь - username: standart@user.com, пароль: pass \
Для проверки работы через Postman необходимо получить токен post запросом на http://127.0.0.1:8000/auth/jwt/login \
передав поля username и password
# Запуск проекта:
## В проекте используется Poetry (https://python-poetry.org/docs/)
### Настройте файл .env (или просто переименуйте .env_example в .env):
### Клонируйте репозиторий:
git clone git@github.com:pdyakovlev/itsoltest.git
### Установите зависимости:
poetry install
### Запустите виртуальное окружение:
poetry shell
### Запустите проект:
uvicorn app.main:app
## Документация swagger доступна по адресу http://127.0.0.1:8000/docs
