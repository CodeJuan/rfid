#!/bin/bash

mkdir -p shops/fixtures/
mkdir -p equipments/fixtures/

python manage.py dumpdata --indent=4 shops > shops/fixtures/initial_data.json
python manage.py dumpdata --indent=4 equipments > equipments/fixtures/initial_data.json

rm -rf init_data
cp -R media init_data
