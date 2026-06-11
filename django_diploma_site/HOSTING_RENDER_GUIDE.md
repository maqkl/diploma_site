# Размещение Django-проекта на Render

## Что уже подготовлено

- `requirements.txt` содержит Django, Gunicorn и WhiteNoise.
- `settings.py` читает `DEBUG`, `SECRET_KEY`, `ALLOWED_HOSTS` из переменных окружения.
- Static files собираются через `collectstatic`.
- `build.sh` выполняет установку зависимостей, сбор статических файлов и миграции.
- `render.yaml` описывает бесплатный Web Service.

## Команды перед деплоем

```powershell
cd C:\Django_projects\Diplom_project\django_diploma_site
py manage.py check
py manage.py collectstatic --no-input
```

Потом сохранить изменения:

```powershell
cd C:\Django_projects\Diplom_project
git add .
git commit -m "Prepare project for Render hosting"
git push
```

## Настройка Render вручную

1. Render Dashboard -> New -> Web Service.
2. Подключить GitHub repository.
3. Repository: `maqkl/diploma_site`.
4. Root Directory: `django_diploma_site`.
5. Build Command: `./build.sh`.
6. Start Command: `gunicorn diploma_site.wsgi:application`.
7. Environment Variables:
   - `DEBUG=False`
   - `SECRET_KEY=сгенерированная-длинная-строка`
   - `ALLOWED_HOSTS=.onrender.com,localhost,127.0.0.1`

## После деплоя

Render выдаст ссылку вида:

```text
https://diploma-site.onrender.com
```

Для диплома этого достаточно. SQLite подходит для демонстрации, но при реальном коммерческом использовании лучше подключить PostgreSQL.
