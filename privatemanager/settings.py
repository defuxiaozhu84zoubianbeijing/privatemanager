"""
Django settings for privatemanager project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gc7#bc0(dsc#%&l(r-$46ds(h%dmz0^8r!fe45vt%iu2cfl=mm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pagination_bootstrap',
    'chartit',
    'simplejson',
    'crispy_forms',
    'procedure_article',
    'common',
    'accounts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination_bootstrap.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'privatemanager.urls'

WSGI_APPLICATION = 'privatemanager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'privatemanager',
        'USER': 'root',
        'PASSWORD' : 'wx19840905',
        'HOST' : '127.0.0.1',
        'PORT' : '3306'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = '/media/'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates'), ]

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# log
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
            'datefmt' : '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'default' : {
            'level' : 'DEBUG' ,
            'class' : 'logging.handlers.RotatingFileHandler',
            'formatter' : 'verbose' ,
            'filename' : os.path.join(BASE_DIR, 'logs/all.log'),
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'file':{
            'level' : 'DEBUG' ,
            'class' : 'logging.handlers.RotatingFileHandler',
            'formatter' : 'verbose' ,
            'filename' : os.path.join(BASE_DIR, 'logs/debug.log'),
        },
        'scprits_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter':'simple',
        },
                 
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'accounts': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate' : True
        },
        'procedure_article': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate' : True
        },
        'script' : {
            'handlers':['scprits_handler'],
            'level' : 'DEBUG' ,
            'propagate' : True
        
        },
    }
}

# email setting
EMAIL_HOST = 'smtp.163.com'  # SMTP addr
EMAIL_PORT = 25  # SMTP port
EMAIL_HOST_USER = 'privatemanager_1@163.com'  # user email
EMAIL_HOST_PASSWORD = 'shangqiuhenan'  # user pwd
EMAIL_SUBJECT_PREFIX = u'[privatemanager WEB]'            
EMAIL_USE_TLS = True                             
# admin site
SERVER_EMAIL = 'privatemanager_1@163.com' 


