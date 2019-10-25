#! /bin/bash

python manage.py migrate API zero
python manage.py migrate
python manage.py loaddata data.json