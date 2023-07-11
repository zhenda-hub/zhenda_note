"""
Django settings for zd_note project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1naf1o8(e_#@i0)+mc48ye^u3$=kmsh8m^#cev!1u5fj62(4+b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
    'http://134.175.124.152'
]

CORS_ORIGIN_WHITELIST = [
    'http://134.175.124.152',
    # 其他受信任的来源
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

# 配置redis
REDIS_HOST = ''
REDIS_PORT = 6379
REDIS_DB = 0


# 配置celery
CELERY_BROKER_URL = 'redis://{}:{}/{}'.format(REDIS_HOST, REDIS_PORT, REDIS_DB)
CELERY_RESULT_BACKEND = 'redis://{}:{}/{}'.format(REDIS_HOST, REDIS_PORT, REDIS_DB)
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# 配置django-celery-beat
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_apscheduler',
    # 'dbbackup',

    'search',
    'update_notice',
    'user',
    'web',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'zd_note.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 根templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'zd_note.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

# USE_TZ = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # 其他静态资源地址
STATIC_ROOT = BASE_DIR / 'collected_static'  # 生成环境 使用 collection

# 配置media
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 用户邮箱
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.163.com'
# EMAIL_PORT = 25
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_SUBJECT_PREFIX = '[zd_note]'
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# ACCOUNT_ACTIVATONI_REQUIRED = False

# # 创建log文件的文件夹
# LOG_PATH = BASE_DIR / "logs"
# LOG_PATH.mkdir(parents=True, exist_ok=True)
# 配置日志
# LOGGING = {
#     'version': 1,  # 保留字
#     'disable_existing_loggers': False,  # 禁用已经存在的logger实例
#     # 日志文件的格式
#     'formatters': {
#         # 详细的日志格式
#         'standard': {
#             'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d][%(levelname)s][%(message)s]'
#         },
#         # 简单的日志格式
#         'simple': {
#             'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] %(message)s',
#             # 'format': '[%(levelname)s][%(asctime)s][%(funcName)s:%(lineno)d] %(message)s',
#             # 'format': '[%(levelname)s][%(asctime)s][%(pathname)s:%(lineno)d] %(message)s',
#         },
#     },
#     # 过滤器
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     # 处理器
#     'handlers': {
#         'console': {     # 在终端打印
#             'level': 'INFO',
#             'filters': ['require_debug_true'],  # 只有在Django debug为True时才在屏幕打印日志
#             'class': 'logging.StreamHandler',  #
#             'formatter': 'simple',
#         },
#         'default': {    # 默认的
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
#             'filename': LOG_PATH / "all.log",  # 日志文件
#             'maxBytes': 1024 * 1024 * 5,                    # 日志大小 5M
#             'backupCount': 3,                                # 最多备份几个
#             'formatter': 'simple',
#             'encoding': 'utf-8',
#         },
#         'error': {   # 专门用来记错误日志
#             'level': 'ERROR',
#             'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
#             'filename': LOG_PATH / "error.log",  # 日志文件
#             'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
#             'backupCount': 5,
#             'formatter': 'simple',
#             'encoding': 'utf-8',
#         },
#     },
#     'loggers': {
#         'django': {             # 默认的logger应用如下配置
#             'handlers': ['default', 'console', 'error'],  # 上线之后可以把'console'移除
#             'level': 'INFO',
#             'propagate': False,  # 向不向 父logger传递
#         },
#     },
#     'root': {
#             'handlers': ['default', 'console', 'error'],  # 上线之后可以把'console'移除
#             'level': 'INFO',
#     }
# }
try:
    from .local_settings import *  # 最后导入本地配置
except ImportError:
    pass
