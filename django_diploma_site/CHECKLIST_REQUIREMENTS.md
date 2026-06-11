# Соответствие критериям из Excel

## A1 - Дизайн и макет

- Шапка сайта: `templates/shop/base.html`.
- Логотип: блок `.logo` и `.logo-mark` в `base.html`.
- Навигационное меню: `base.html`, ссылки на все основные страницы.
- Главная страница: `templates/shop/home.html`.
- Подвал сайта: `base.html`, блок `<footer>`.
- Единая цветовая гамма: CSS-переменные в `base.html`.
- Единый стиль оформления: общий базовый шаблон `base.html`.
- Заголовки и отступы: стили `h1`, `h2`, `h3`, `.section`, `.card`.
- Изображения: SVG-файлы в `shop/static/shop/img/`.
- Таблица данных: `home.html`, `catalog.html`, `docs.html`.
- Форма ввода данных: `contacts.html`, `register.html`, `login.html`.
- Карточки товаров/услуг: `catalog.html`, `home.html`, `favorites.html`.
- Мобильная адаптация: media queries в `base.html`.
- CSS-стили: основной CSS внутри `base.html`.
- Внешний CSS-файл: `shop/static/shop/css/external.css`.
- Кнопка «Очистить корзину»: `cart.html`, view `clear_cart`.
- Авторизация: `LoginView` в `shop/urls.py`, шаблон `login.html`.
- Регистрация: view `register`, форма `RegistrationForm`.
- Поле Email при регистрации: `RegistrationForm.email`.
- Форма обратной связи: `ContactForm` и модель `ContactMessage`.
- Социальные сети: footer и `contacts.html`.
- Фильтр поиска: `catalog` view и JS-поле `liveSearch`.
- Подвал и навигация на всех страницах: наследование от `base.html`.
- Избранное: session list `favorites`, view `toggle_favorite`.

## A2 - Базовая функциональность

- Переход между страницами: `shop/urls.py` и навигация.
- Кнопка «Главная»: nav link в `base.html`.
- Кнопка «О нас»: nav link в `base.html`.
- Кнопка «Назад»: `home.html`, `about.html`.
- Кнопка «Наверх»: JS в `base.html`.
- Кнопка «Контакты»: nav link в `base.html`.
- Выпадающее меню: `.dropdown` и JS в `base.html`.
- Гиперссылки: меню, footer, social links.
- Проверка Email: Django `EmailField` в `ContactForm` и `RegistrationForm`.
- Сообщение об ошибке: Django messages + field errors.
- Сообщение об успешной отправке: `messages.success` в `contacts`.
- Поиск по странице: `liveSearch` в `catalog.html`.
- Слайдер изображений: `.slider`, `.slide`, `.dot` в `home.html` и JS в `base.html`.
- Галерея изображений: карточки товаров с изображениями в каталоге.

## B1 - Расширенная функциональность

- Тёмная тема: `body.dark-theme` в `base.html`.
- Светлая тема: CSS-переменные `:root`.
- Переключение тем: кнопка `themeToggle`.
- Сохранение темы: `localStorage`.
- Всплывающие подсказки: `.tooltip` в CSS и пример в `about.html`.
- JS без сторонних библиотек: весь JS расположен в `base.html`.

## B2 - Код и архитектура

- Больше 5 комментариев: комментарии есть в Python-коде, JS и CSS.
- Предупреждения/подтверждения: `data-confirm` для удаления и очистки корзины.
- Отступы и форматирование: файлы разделены по Django-структуре.
- Понятные имена переменных: `cart_data`, `favorites`, `products`, `query`, `category`.
- Популярные браузеры: используются стандартные HTML/CSS/JS без нестабильных библиотек.
- Удобный интерфейс: карточки, кнопки, сообщения, адаптивная сетка.
- Заполняемость каталога: команда `python manage.py seed_demo` создаёт 10 позиций.

## C1-C3 - Документация

- Требования к оборудованию: `README.md` и страница `docs.html`.
- Инструкция установки: `README.md` и `docs.html`.
- Инструкция эксплуатации: `README.md` и `docs.html`.
- Схема работы: таблица «Схема работы» в `docs.html`.
