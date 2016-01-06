#!/bin/bash

rm -f db.sqlite3

python manage.py migrate
python manage.py createsuperuser --username=jackon --email=jiekunyang@gmail.com

python manage.py check_permissions  # required by userena

python manage.py loaddata init_data/initial_data.json

rm -rf media
cp -R init_data media
