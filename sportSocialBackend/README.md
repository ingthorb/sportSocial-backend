## Sports Meetup

Information how to install required dependencies to run this project, this was done through Windows.

Start by installing pipenv through pip
pip install pipenv

Then use the commands
pipenv install

Run:
pipenv shell


## Start Server
python manage.py runserver

## Migrate
python manage.py migrate

## Jenkins
Using Jenkins for build

## Heroku

To run locally if you have windows:
heroku local web -f Procfile.windows
https://sport-social.herokuapp.com/

For updating live database 
heroku run python manage.py migrate