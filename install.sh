#!/usr/bin/env bash

BASE_DIR='/opt/echo'

echo 'updating server'
sudo apt-get update && apt-get upgrade

echo 'install dependencies'
sudo apt-get install python3-pip git nginx -y

echo 'download echo(outline wreapper)'
git clone https://github.com/shabane/echo.git $BASE_DIR

echo 'install libraries'
pip3 install -r $BASE_DIR/requirements.txt
pip3 install gunicorn
git clone https://github.com/shabane/pysbin.git $BASE_DIR/outline/core/pysbin

echo 'create direcgtory to save QRs'
mkdir $BASE_DIR/static/

echo 'migrate db'
python3 $BASE_DIR/manage.py makemigrations
python3 $BASE_DIR/manage.py migrate

echo 'run the web site'
cp -v $BASE_DIR/conf/echo.conf /etc/nginx/conf.d/
sudo systemctl restart nginx.service
cd $BASE_DIR && nohup gunicorn -c conf/gunicorn_config.py echo.wsgi &
