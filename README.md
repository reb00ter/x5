# Containers

> Система поиска свободных контейнеров

## Сборка

Для сборка состоит из двух этапов: 
### Сборка JS
``` bash
cd js

# Установить зависимости
npm install

# Сборка для продакшн, с минификацией
npm run build

# Сборка для продакшн, с отчётом
npm run build --report
```
Результат сборки сразу положится в /static
Про остальные варианты сборки js можно почитать README.md в папке JS

### Подготовка окружения для Django
``` bash
# от корня проекта (cd .. после предыдущего шага)
# установка зависимостей
pip install -r requirements.txt

# сборка статики
python manage.py collectstatic

# равёртывание БД
python manage.py migrate
```

В целом всё стандартно для Django

## Описание системы
Верх сделан полностью на Vue.js. Отдаётся с корня сайта и дальше работают внутренние маршруты Vue (js/src/router/index.js)

Всё API живёт на /api

Админка стандарно на /admin 
