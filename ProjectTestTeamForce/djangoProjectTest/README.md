# Онлайн-список кандидатов на позицию Python-разработчика

Для начала работы с программным кодом онлайн-списка необходимо
установить Django версии 3.2.8:

### Инструкция по установке и первому запуску 

Установить сторонние библиотеки:

```
pip install -r requirements.txt
```

Провести миграцию:

```bash
python manage.py makemigrations
python manage.py migrate
```

Создать суперпользователя:

```bash
python manage.py createsuperuser
```

Запустить веб-сервер проекта:

```bash
python manage.py runserver
```