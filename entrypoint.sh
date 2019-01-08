#!/bin/sh

python manage.py migrate --noinput

if [ "$DEBUG" = "on" ]; then
    echo "starting gunicorn for development"
    gunicorn --bind 0.0.0.0:8002 --reload ecommerce.wsgi:application
else
    echo "starting gunicorn"
    gunicorn --bind 0.0.0.0:8002 ecommerce.wsgi:application
fi