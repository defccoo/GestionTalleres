#!/bin/bash
rm -rf talleres/migrations/
rm db.sqlite3 
python manage.py makemigrations
python manage.py migrate
