release: python manage.py makemigrations analytics
release: python manage.py makemigrations marketing
release: python manage.py makemigrations users
release: python manage.py migrate
web: gunicorn base.wsgi.prod --log-file -