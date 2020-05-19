# Django CBV + Django REST CBV + Charts.js
Example of using Django + Django REST Framework + Chart.js to generate graphs

## Main Requirements
Python3.x.x
Django
Django REST Framework
Chart.js


## How to use
Create a folder to store this project. Open this folder on terminal and run the following commands

### 1. Clone the project
`git clone https://github.com/rodrigoddc/charts.git`

### 2. Create a virtual environment
`python3 -m venv venv`

### 3. Activate the the virtual environment previously created
on linux: `source ./venv/bin/activate`
on windows: `./venv/Scripts/activate.bat`

### 4. Installing libs
`pip install -r requirements.txt`

### 5. Creating database
`python manage.py makemigrations`

### 6. Migrating database models
`python manage.py migrate`

### 7. Creating superuser
`python manage.py createsuperuser`

### 8. Running
`python manage.py runserver`

After that, you'll be able to access the project at 127.0.0.1:8000 or localhost:8000/ on your browser.

At the adress 127.0.0.1:8000/admin or localhost:8000/admin you'll be able to login to populate data that will be rendered as chart

##### This application is just a case study, so SECRET_KEY, DEBUG and DATABASES are present as plain text

##### Never do this in production! 