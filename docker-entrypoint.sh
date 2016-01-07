/code/manage.py syncdb --noinput
bash /code/install.sh
bash /code/run.sh
#/usr/local/bin/gunicorn config.wsgi:application -w 2 -b :8000
