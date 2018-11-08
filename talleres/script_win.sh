#!/bin/bash

rd /s /q talleres/migrations
del db.sqlite3

#Rellenar BBDD

python manage.py makemigrations
python manage.py makemigrations talleres
python manage.py migrate

python manage.py shell < populate.py 
