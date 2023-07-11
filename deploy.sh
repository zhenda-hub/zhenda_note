#!/bin/bash

env_bin=/www/server/pyporject_evn/94d7bd8179533c59aca987c718472328_venv/bin

${env_bin}/pip install -r requirements.txt
${env_bin}/python3 manage.py makemigrations
${env_bin}/python3 manage.py migrate
${env_bin}/python3 manage.py collectstatic

# /www/server/pyporject_evn/94d7bd8179533c59aca987c718472328_venv/bin/python3 manage.py makemigrations
# /www/server/pyporject_evn/94d7bd8179533c59aca987c718472328_venv/bin/python3 manage.py migrate
# /www/server/pyporject_evn/94d7bd8179533c59aca987c718472328_venv/bin/python3 manage.py collectstatic

