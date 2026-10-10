# settings/dev.py
from .base import *  # 先继承所有公共配置

# ============ 开发环境专属 ============

DEBUG = True

# 开发环境允许所有主机访问（方便手机调试等）
ALLOWED_HOSTS = ['*']

# 开发环境的密钥（可以随便写，只要不泄露到生产环境）
SECRET_KEY = 'django-insecure-dev-only-key-do-not-use-in-prod'

# 开发环境用轻量的 SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 开发环境打印 SQL 日志（非常重要！让你看到 ORM 生成的 SQL）
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',  # 想看SQL就打开，不想看改成 WARNING
        },
    },
}