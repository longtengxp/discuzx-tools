#!/usr/bin/env python
#  coding: utf-8

"""
Django settings for govern project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MEDIA_ROOT = os.path.join(BASE_DIR, '../media').replace('\\', '/')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, '../static').replace('\\', '/')
STATIC_URL = '/static/'

# ADMIN_MEDIA_PREFIX = '/static/admin/'
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

SITE_ID = 1
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']
INTERNAL_IPS = ['127.0.0.1']

# ###########
# EMAIL #
# ###########

EMAIL_PORT = '25'
EMAIL_USE_TLS = True
EMAIL_HOST = os.getenv('email_host')
EMAIL_HOST_USER = os.getenv('email_host_user')
EMAIL_HOST_PASSWORD = os.getenv('email_host_password')

# Default email address to use for various automated correspondence from
# the site managers.
DEFAULT_FROM_EMAIL = os.getenv('default_from_email')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Subject-line prefix for email messages send with django.core.mail.mail_admins
# or ...mail_managers.  Make sure to include the trailing space.
EMAIL_SUBJECT_PREFIX = '[Django] '

ADMINS = MANAGERS = os.getenv('admins_email')

# Email address that error messages come from.
SERVER_EMAIL = DEFAULT_FROM_EMAIL
ADMIN_HONEYPOT_EMAIL_ADMINS = True

# 发现一个死链接时, 是否发送一封邮件给 MANAGERS
SEND_BROKEN_LINK_EMAILS = True

DEBUG_TOOLBAR_PATCH_SETTINGS = True

# Application definition
INSTALLED_APPS = (
    # 'grappelli',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',
    'admin_honeypot',

    # widget modules
    'import_export',

    'gunicorn',
    'govern.apps.roboter',

    # 'xadmin',
    # 'crispy_forms',
    # 'reversion',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'govern.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'govern.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'roboter',
        'USER': os.getenv('mysql_user'),
        'PASSWORD': os.getenv('mysql_password'),
        'HOST': os.getenv('mysql_host'),
        'PORT': os.getenv('mysql_port'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# USE_TZ = True 报以下错误:
# Database returned an invalid value in QuerySet.datetimes().
# Are time zone definitions for your database and pytz installed?

# django-debug-toolbar
DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': 'http://code.jquery.com/jquery-2.1.0.min.js',
}
