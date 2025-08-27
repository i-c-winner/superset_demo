# Superset Presentation - Демо дашборды с Apache Superset

Демонстрационное веб-приложение на Django, которое показывает возможности визуализации данных в стиле Apache Superset с использованием Plotly.

## 🚀 Особенности

- **Современный дизайн** с Bootstrap 5
- **Интерактивные дашборды** с Plotly
- **Адаптивная верстка** для всех устройств
- **Русская локализация**
- **Готовность к продакшену** с PostgreSQL

## 📊 Демо графики

- Линейные графики (динамика продаж)
- Столбчатые диаграммы (выручка по продуктам)  
- Круговые диаграммы (распределение бюджета)
- И многое другое!

## 🛠 Локальная установка

### Предварительные требования

- Python 3.9+
- pipenv

### Шаги установки

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/superset-presentation.git
   cd superset-presentation
   ```

2. **Создайте виртуальное окружение и установите зависимости:**
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Примените миграции базы данных:**
   ```bash
   python manage.py migrate
   ```

4. **Создайте суперпользователя (опционально):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Запустите сервер разработки:**
   ```bash
   python manage.py runserver
   ```

6. **Откройте в браузере:**
   http://127.0.0.1:8000/

## 🌐 Деплой на Render

### Шаг 1: Подготовка репозитория

1. **Создайте публичный репозиторий на GitHub** и загрузите туда код:
   ```bash
   git add .
   git commit -m "Initial commit for Render deployment"
   git push origin main
   ```

### Шаг 2: Настройка Render

1. **Создайте аккаунт на [render.com](https://render.com)** и подключите к GitHub

2. **Создайте PostgreSQL базу данных:**
   - Нажмите "New +" → "PostgreSQL" 
   - Name: `superset-presentation-db`
   - Выберите бесплатный план (Free)
   - Скопируйте `External Database URL` после создания

3. **Создайте Web Service:**
   - Нажмите "New +" → "Web Service"
   - Выберите ваш репозиторий `superset-presentation`
   - Заполните настройки:

   **Basic Settings:**
   - **Name:** `superset-presentation` (или любое другое)
   - **Environment:** `Python 3`
   - **Region:** выберите ближайший
   - **Branch:** `main`

   **Build & Deploy:**
   - **Build Command:** `./build.sh`
   - **Start Command:** `python manage.py migrate && gunicorn superset_presentation.wsgi:application`

### Шаг 3: Переменные окружения

В разделе **"Advanced"** → **"Environment Variables"** добавьте:

| Переменная | Значение | Описание |
|-----------|---------|----------|
| `SECRET_KEY` | `your-super-secret-key-here-make-it-long-and-random` | Сгенерируйте длинный случайный ключ |
| `DATABASE_URL` | `postgresql://user:pass@host:port/db` | URL PostgreSQL из шага 2 |
| `PYTHON_VERSION` | `3.9.6` | Версия Python |
| `RENDER` | `true` | Указывает, что приложение на Render |

**Генерация SECRET_KEY:**
```python
# Выполните в Python для генерации ключа
import secrets
print(secrets.token_urlsafe(50))
```

### Шаг 4: Деплой

1. **Нажмите "Create Web Service"**
2. **Render автоматически:**
   - Склонирует ваш репозиторий
   - Выполнит `build.sh` (установит зависимости, соберет статику)
   - Запустит миграции
   - Запустит приложение через Gunicorn

3. **После успешного деплоя:**
   - Ваше приложение будет доступно по адресу типа: `https://superset-presentation.onrender.com`
   - Автоматические деплои при пуше в `main` ветку

## 🔧 Технические детали

### Стек технологий

- **Backend:** Django 4.2
- **Frontend:** Bootstrap 5, Plotly.js  
- **База данных:** SQLite (разработка) / PostgreSQL (продакшн)
- **Визуализация:** Plotly
- **Деплой:** Render, Gunicorn, WhiteNoise

### Структура проекта

```
superset-presentation/
├── dashboard/                 # Основное приложение
│   ├── templates/            # HTML шаблоны
│   ├── views.py             # Логика представлений  
│   └── urls.py              # URL маршруты
├── superset_presentation/    # Настройки проекта
│   ├── settings.py          # Конфигурация Django
│   └── urls.py              # Главные URL маршруты
├── templates/               # Общие шаблоны
├── static/                  # Статические файлы
├── requirements.txt         # Python зависимости
├── Procfile                # Конфигурация для Render
├── build.sh                # Скрипт сборки
├── runtime.txt             # Версия Python
└── README.md               # Документация
```

## 🐛 Решение проблем

### Ошибка при деплое

1. **Проверьте логи в Render Dashboard**
2. **Убедитесь, что все переменные окружения заданы**
3. **Проверьте, что DATABASE_URL корректный**

### Статические файлы не загружаются

1. **Убедитесь, что WhiteNoise установлен**
2. **Проверьте настройки STATIC_* в settings.py**
3. **Выполните `python manage.py collectstatic` локально для тестирования**

### Графики Plotly не отображаются

1. **Проверьте консоль браузера на ошибки JavaScript**
2. **Убедитесь, что Plotly.js загружается (проверьте CDN)**
3. **Попробуйте обновить страницу**

## 🤝 Вклад в проект

1. Fork проекта
2. Создайте feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit изменения (`git commit -m 'Add some AmazingFeature'`)
4. Push в branch (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

## 📝 Лицензия

Этот проект распространяется под лицензией MIT. См. файл `LICENSE` для подробностей.

## 🔗 Полезные ссылки

- [Django Documentation](https://docs.djangoproject.com/)
- [Plotly Python Documentation](https://plotly.com/python/)
- [Apache Superset](https://superset.apache.org/)
- [Render Documentation](https://render.com/docs)

## 📞 Поддержка

Если у вас есть вопросы или проблемы, создайте issue в репозитории GitHub.