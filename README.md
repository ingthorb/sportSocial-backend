## Sports Meetup

## Build Status
[![Heroku CI Status](https://heroku-ci-badge-app.herokuapp.com/last.svg)](https://dashboard.heroku.com/pipelines/b2b69ac6-0860-413d-af8f-efdf96c680ee/tests)


## Setup
Information how to install required dependencies to run this project, this was done through Mac.

First thing you need is pip for this project.
To check if you have pip installed:
python -m pip --version

If you don't have pip on your machine follow these steps:

1. Curl this: curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
2. Navigate to the folder where you got the file
3. Run python get-pip.py

pyenv:
brew install pyenv

With versions: 3.7.7, 3.8.2

Pyenv-virtualenv:
brew install pyenv-virtualenv

Create virtualenv with your own name using version 3.7.7:
pyenv virtualenv 3.7.7 {NAME}

Activate:
pyenv activate {NAME}

After that you can install pipenv:
pip install pipenv

Then use the commands
pipenv install

Run:
pipenv shell


## Start Server
python manage.py runserver

## Migrate
For some initial data you can run setup_database.sh


## Jenkins
Using Jenkins for build

## Heroku
Building and deployed with Heroku.
For updating live database 
heroku run python manage.py migrate


## For Windows Users

To run locally if you have windows:
heroku local web -f Procfile.windows
https://sport-social.herokuapp.com/

For updating live database 
heroku run python manage.py migrate

## Staging Environment
Everything that is pushed to branch develop will be deployed to the staging environment.
https://staging-api.sportsocial.is

## Production Environment
After testing and veryfing it works on the staging environment then there must be a pull request from develop to master branch. After the pull request is accepted it will be deployed to production.
http://api.sportsocial.is
