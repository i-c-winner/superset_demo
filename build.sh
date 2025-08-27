#!/usr/bin/env bash
# Exit immediately if a command fails
set -o errexit

# Устанавливаем зависимости из requirements.txt
pip install -r requirements.txt

# Выполняем коллекцию статических файлов
python manage.py collectstatic --noinput