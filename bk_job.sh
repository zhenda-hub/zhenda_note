#!/bin/bash

web_dir=/www/wwwroot/zhenda_note
env_bin=/www/server/pyporject_evn/94d7bd8179533c59aca987c718472328_venv/bin
cd ${web_dir}
${env_bin}/python3 ./utils/db_backup.py

