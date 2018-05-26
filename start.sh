#!/bin/bash
export PYTHONPATH=$pwd
export DJANGO_SETTINGS_MODULE=parking_service.db.settings.local
python parking_service/manage.py makemigrations
python parking_service/manage.py migrate
python parking_service/conf/service_app.py
