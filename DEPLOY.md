# Быстрый деплой на Render

## 1. Подготовка репозитория
```bash
git add .
git commit -m "Готов к деплою на Render"
git push origin main
```

## 2. Настройка Render

### Создание PostgreSQL базы:
1. render.com → New → PostgreSQL
2. Name: superset-presentation-db
3. Plan: Free
4. Скопировать External Database URL

### Создание Web Service:
1. render.com → New → Web Service
2. Выбрать репозиторий
3. Настройки:
   - **Name:** superset-presentation
   - **Environment:** Python 3
   - **Build Command:** `./build.sh`
   - **Start Command:** `python manage.py migrate && gunicorn superset_presentation.wsgi:application`

### Environment Variables:
| Variable | Value |
|----------|-------|
| `SECRET_KEY` | `генерировать-длинный-случайный-ключ` |
| `DATABASE_URL` | `postgresql://...` (из шага PostgreSQL) |
| `PYTHON_VERSION` | `3.9.6` |
| `RENDER` | `true` |

## 3. Генерация SECRET_KEY
```python
import secrets
print(secrets.token_urlsafe(50))
```

## 4. Готово! 
Render автоматически задеплоит приложение.