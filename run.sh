#!/bin/bash
sudo apt-get update -y
sudo apt-get install git -y
git clone https://github.com/rathourdevesh/capstone.git
cd capstone
git checkout typing-test
sudo apt-get install python3 -y
sudo apt-get -y install python3-pip -y
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000

# web server setup
sudo apt install nginx
gunicorn capstone.wsgi:application --bind 0.0.0.0:8000

sudo touch /etc/nginx/sites-available/capstone
sudo cp nginx /etc/nginx/sites-available/capstone
sudo ln -s /etc/nginx/sites-available/capstone /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx