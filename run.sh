#!/bin/bash
sudo apt-get update -y
sudo apt-get install git -y
git clone https://github.com/rathourdevesh/capstone.git
cd capstone
git checkout typing-text
sudo apt-get install python3 -y
sudo apt-get -y install python3-pip -y
python3 -m venv venv
source venv/bin/activate
pip install requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver