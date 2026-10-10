# settings/prod.py
from .base import *

# ============ 生产环境专属 ============

DEBUG = False

# 生产环境必须填写真实域名或服务器IP
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']

# 生产环境的 SECRET_KEY 绝对不能硬编码在代码里，要从环境变量读取
import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'fallback-key-change-me')

# 生产环境用 PostgreSQL（推荐）或 MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'qa_db'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# 生产环境的静态文件通过 Nginx 等服务器托管
STATIC_ROOT = BASE_DIR / 'staticfiles'

# 安全相关（生产必备）
SECURE_SSL_REDIRECT = True        # 强制 HTTPS
SESSION_COOKIE_SECURE = True      # Session 只通过 HTTPS 传输
CSRF_COOKIE_SECURE = True         # CSRF Cookie 只通过 HTTPS 传输
SECURE_HSTS_SECONDS = 31536000    # HSTS 一年