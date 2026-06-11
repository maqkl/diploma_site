# Django diploma site - TechMarket

Проект сделан под критерии дипломной работы: дизайн, каталог, корзина, избранное, регистрация, авторизация, форма обратной связи, фильтр, тёмная/светлая тема, таблица данных, документация по установке и эксплуатации.

## Что внутри

- Django-проект `diploma_site`.
- Приложение `shop`.
- Каталог товаров и услуг с поиском и фильтром.
- Корзина на Django sessions.
- Избранное на Django sessions.
- Регистрация с обязательным Email.
- Авторизация и выход через стандартную систему Django.
- Форма обратной связи с проверкой Email.
- Светлая и тёмная тема с сохранением в `localStorage`.

## Запуск

```bash
cd django_diploma_site
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

Открыть сайт: `http://127.0.0.1:8000/`

## Админ-панель

```bash
python manage.py createsuperuser
```

После создания администратора открыть: `http://127.0.0.1:8000/admin/`

## Минимальные требования к оборудованию

- CPU: 2 ядра, 2.0 GHz или выше.
- RAM: 4 GB минимум, 8 GB желательно.
- Disk: 1 GB свободного места для проекта, базы SQLite и зависимостей.
- OS: Windows 10/11, Linux или macOS.
- Browser: Chrome, Edge, Firefox или Safari последних версий.

## Инструкция эксплуатации

1. Перейти на главную страницу.
2. Открыть каталог через меню.
3. Использовать поиск и фильтр по категории.
4. Добавить товары в корзину или избранное.
5. Зарегистрироваться, указав Email.
6. Войти в аккаунт.
7. Отправить сообщение через страницу контактов.
8. Переключить тему кнопкой в шапке сайта.
9. Очистить корзину через кнопку `Очистить корзину`.

## Структура

```text
django_diploma_site/
├── manage.py
├── requirements.txt
├── diploma_site/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── shop/
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── urls.py
    ├── admin.py
    ├── migrations/
    ├── management/commands/seed_demo.py
    ├── static/shop/css/external.css
    ├── static/shop/img/*.svg
    └── templates/shop/*.html
```
