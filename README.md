# Запуск проекта:
## В проекте используется Poetry (https://python-poetry.org/docs/)
### Клонируйте репозиторий:
git clone git@github.com:pdyakovlev/itsoltest.git
### Установите зависимости:
poetry install
### Запустите виртуальное окружение:
poetry shell
### Запустите проект:
uvicorn app.main:app
## Документация swagger доступна по адресу http://127.0.0.1:8000/docs
