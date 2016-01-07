/code/manage.py syncdb --noinput
./code/run.sh
#/usr/local/bin/gunicorn config.wsgi:application -w 2 -b :8000
