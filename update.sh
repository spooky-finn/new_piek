#! /bin/bash

source ../venv/bin/activate
git status
git pull 
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py compress --force
sudo supervisorctl restart piek
