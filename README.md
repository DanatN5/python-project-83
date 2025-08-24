### Hexlet tests and linter status:
[![Actions Status](https://github.com/DanatN5/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DanatN5/python-project-83/actions)

[![Python CI](https://github.com/DanatN5/python-project-83/actions/workflows/build.yml/badge.svg)](https://github.com/DanatN5/python-project-83/actions/workflows/build.yml)

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=DanatN5_python-project-83&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=DanatN5_python-project-83)

# Анализатор страниц

> Веб-приложение для анализа SEO-параметров сайтов
> Позволяет сохранять URL-адреса, выполнять проверки и собирать информацию о заголовках и метаданных


## Установка и запуск:
# Клонировать репозиторий
``` 
git clone git@github.com:DanatN5/python-project-83.git
```
````
cd python-project-83
````

# Сконфигурируйте файл .env с со следущими переменными:

SECRET_KEY
DATABASE_URL

# Установка зависимостей и создание таблиц в базе данных
`````
make build
``````

# Запуск приложения
````````
make start
````````

