# Django diploma site - TechMarket

Проект сделан под критерии дипломной работы: дизайн, каталог, страница товара, корзина, оформление заказа, избранное, регистрация, авторизация, форма обратной связи, фильтр, тёмная/светлая тема, таблица данных, документация по установке и эксплуатации.

## Что внутри

- Django-проект `diploma_site`.
- Приложение `shop`.
- Каталог товаров и услуг с поиском и фильтром.
- Отдельная страница каждого товара.
- Корзина на Django sessions.
- Оформление заказа с сохранением в базу данных.
- Таблицы `Order` и `OrderItem` в Django admin.
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

В админке можно управлять:
- товарами;
- сообщениями из формы контактов;
- заказами;
- составом заказов.

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
4. Открыть подробную страницу товара кнопкой `Подробнее`.
5. Добавить товары в корзину или избранное.
6. Перейти в корзину.
7. Нажать `Оформить заказ`.
8. Заполнить форму заказа.
9. Проверить сохранённый заказ в Django admin.
10. Зарегистрироваться, указав Email.
11. Войти в аккаунт.
12. Отправить сообщение через страницу контактов.
13. Переключить тему кнопкой в шапке сайта.
14. Очистить корзину через кнопку `Очистить корзину`.

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
    ├── static/shop/img/products/
    └── templates/shop/*.html
```
