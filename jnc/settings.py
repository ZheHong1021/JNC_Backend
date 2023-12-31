"""
Django settings for jnc project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-39jd814rlilr8!3chyh+c^=cpk#0hubma2^s6=20ot8)j&ha2k'

# SECURITY WARNING: don't run with debug turned on in production!
# 【系統模式】: 二選一
# DEBUG = True # Development Mode (測試開發)
DEBUG = False # Production Mode (正式發布)


# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*'] # 允許所有網域進入


# Application definition
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Thired party apps (第三方應用套件)
INSTALLED_APPS += [
    'corsheaders',
    'rest_framework', # rest_framework
    'django_extensions', # 可以使用一些專案查詢工具(EX: python manage.py show_urls)
]

# Custom apps (自定義)
INSTALLED_APPS += [
    'apps.devices_inspect', 
    'apps.notify', 
    'apps.system_app', 
]

# 如果要透過 apps來管理每個 appa，則必須加上這行，否則上方 INSTALLED_APPS則必須要加上前綴 <apps>
import sys, os
sys.path.append(os.path.join(BASE_DIR, 'apps')) # at the bottom of the fiS

# Middleware 中間件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 根路由
ROOT_URLCONF = 'jnc.urls'



# Template 模板樣式
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [os.path.join(BASE_DIR, "templates")], # 設定 Template路徑讓 Django可以讀取到模版
        'DIRS': [os.path.join(BASE_DIR, 'frontend/dist')], # 讀取 VueJS build後所生成的 dist檔
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

WSGI_APPLICATION = 'jnc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': { # MySQL(預設)
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'jnc', # MySQL 資料庫的名稱
        'USER': 'root', # 使用者名稱
        'PASSWORD': 'Ru,6e.4vu4wj/3', # 密碼
        'HOST': 'localhost', # IP 地址
        'PORT': '3306', # 埠號(mysql為 3306)
        'OPTIONS': { # 避免發生『MariaDB Strict Mode』問題
            'sql_mode': 'traditional',
        },
    },
    'greenhouse_db': { # MySQL(另一個資料庫)
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'feedsystem',
        'USER': 'root',
        'PASSWORD': 'Ru,6e.4vu4wj/3',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 語言設定(1)
LANGUAGE_CODE = 'zh-hant' #繁體中文
TIME_ZONE = 'Asia/Taipei' # 台北時區
USE_I18N = True
USE_L10N = True
# USE_TZ = True #【發生問題】 RuntimeWarning: DateTimeField JNCInspectHistoryModel.created_at received a naive datetime (2023-10-03 12:00:00) while time zone support is active
USE_TZ = False


# Vue project location
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend')

# Add for vuejs (放靜態檔案的路徑，將該路徑下的檔案蒐集到STATIC_ROOT。DEBUG is False會關閉)
STATICFILES_DIRS = [ 
    os.path.join(FRONTEND_DIR, 'dist', 'static'),
]


# 【Static files】(CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static') # 新增這一行(Heroku)

# 對外提供WEB訪問時的URL地址
STATIC_URL = '/static/'


# 【Media Config】
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 斜槓
# APPEND_SLASH=False


# settings.py
REST_FRAMEWORK = {
    # 【權限限制】
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ]
}