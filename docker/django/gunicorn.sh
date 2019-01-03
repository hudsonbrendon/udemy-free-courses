#!/bin/sh
python manage.py collectstatic --noinput
/usr/local/bin/gunicorn udemy.wsgi -w 2 -b 0.0.0.0:8000
