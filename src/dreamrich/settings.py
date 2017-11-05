"""
Django settings for dreamrich project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)
)))

sys.path.append(os.path.join(BASE_DIR, 'src'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8w5==8=#m-m1(qb@z!ki)gxp9%lp3+*4gfdovg0k&1xz-iygqe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# EMAIL Settings (Obs: is necessary export a environment variable EMAILPWD
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'marcelohpf@gmail.com'
EMAIL_HOST_PASSWORD = os.environ["EMAILPWD"]
DEFAULT_FROM_EMAIL = 'marcelohpf@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


ALLOWED_HOSTS = []


# Application definition

LOCAL_APPS = [
    'dreamrich',
    'client',
    'patrimony',
    'employee',
    'dr_auth',
    'goal',
    'financial_planning'
]

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'rolepermissions',
]

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'dreamrich.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dreamrich.urls'

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

WSGI_APPLICATION = 'dreamrich.wsgi.application'

CORS_WHITELIST = ('http://localhost:3000', 'http://127.0.0.1:3000')

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        #    'rest_framework.permissions.IsAuthenticated',
        "rest_framework.permissions.AllowAny",
    )
}

JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'dr_auth.utils.jwt_response_payload_handler',
    'JWT_ALLOW_REFRESH': True,
}

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.' +
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' +
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' +
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' +
                'NumericPasswordValidator',
    },
]

# Shell Plus
SHELL_PLUS_PRE_IMPORTS = [
    ("client.factories", ("*")),
    ("client.serializers", ("*")),
    ("employee.factories", ("*")),
    ("employee.serializers", ("*")),
    ("patrimony.factories", ("*")),
    ("patrimony.serializers", ("*")),
    ("goal.factories", ("*")),
    ("goal.serializers", ("*")),
    ("financial_planning.factories", ("*")),
    ("financial_planning.serializers", ("*")),
    ("dr_auth.serializers", ("*")),
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Setting path for files uploaded by the user
MEDIA_ROOT = os.path.join(BASE_DIR, 'public')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

ROLEPERMISSIONS_MODULE = 'dr_auth.roles'
