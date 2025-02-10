#!/bin/bash
set -o errexit  # Stop script on error

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py makemigrations users
python manage.py makemigrations myprojects
python manage.py migrate

# Automatically create superuser if CREATE_SUPERUSER is set
if [[ "$CREATE_SUPERUSER" == "true" ]]; then
    python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi
