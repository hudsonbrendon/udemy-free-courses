web: gunicorn udemy.wsgi --log-file -
release: python manage.py migrate
worker: celery -A udemy worker -l info
beat: celery -A udemy beat -l info