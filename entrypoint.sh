#!/bin/bash

set -e

cd /src

# coverage run manage.py test -v 2 && \
# coverage report
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000