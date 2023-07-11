from datetime import datetime

from django.shortcuts import render
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job

from utils.run_cmd import run_cmd2
from utils.path_manager import create_dir



# # 实例化调度器
# scheduler = BackgroundScheduler()
# # 调度器使用DjangoJobStore()
# scheduler.add_jobstore(DjangoJobStore(), "default")
#
#
# # @register_job(scheduler, "interval", seconds=5, replace_existing=True)
# # def my_job():
# #     print("hello world")
#
#
# @register_job(scheduler, "cron", day_of_week='mon-fri', hour=23, minute=21, replace_existing=True)
# def backup_db():
#     print("start backup db")
#
#     create_dir('dbback')
#     curtime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
#     cmd = f'python manage.py dumpdata > dbback/db{curtime}.json --indent=4'
#
#     stdout, stderr = run_cmd2(cmd)
#     print(stdout, stderr)
#
#
# scheduler.start()
