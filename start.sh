#! /bin/bash

pyenv activate sportSocialBackend

pipenv shell

python manage.py runserver
