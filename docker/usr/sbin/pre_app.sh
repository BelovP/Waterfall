#!/bin/bash

if [[ -a /var/log/waterfall/app.log ]] ; then
	mv /var/log/waterfall/app.log /var/log/waterfall/app.log_$(date +%F_%H-%M)_backup
fi

cd ./backend

python3 manage.py migrate --noinput 
python3 manage.py collectstatic <<<yes
