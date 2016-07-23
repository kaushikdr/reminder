"""
Django settings for reminder project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!ucxp9*f=juqn!n%i)!5jeb_k#z!775xztnz#88#@68pmzx%8h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'drip',
    'rest_framework',
    "anymail",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'reminder.urls'

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

WSGI_APPLICATION = 'reminder.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'reminder',
        'USER': 'lastfmuser',
        'PASSWORD': 'lastfmpass',
        'HOST': 'localhost',
    }
}

REST_FRAMEWORK = {
    'PAGE_SIZE': 15,
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
   # 'DEFAULT_AUTHENTICATION_CLASSES': (
   #     'rest_framework.authentication.BasicAuthentication',
   #     'rest_framework.authentication.SessionAuthentication',
   #  ),
   # 'EXCEPTION_HANDLER': 'music.fmauth.fm_exception_handler',
   # # 'DEFAULT_PARSER_CLASSES': (
   #  #    'rest_framework.parsers.JSONParser',
   #  #)
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


ANYMAIL = {
    "MAILGUN_API_KEY": "key-b0967e5a628b69ab067005e4d072fda5",
    "MAILGUN_SEND_DEFAULTS":{
        "esp_extra": {"sender_domain": "sandboxb305d1f4ac80424eb41cc271e738e9c7.mailgun.org"}
    }
}

EMAIL_BACKEND = "anymail.backends.mailgun.MailgunBackend"
DEFAULT_FROM_EMAIL = "no-reply@sandboxb305d1f4ac80424eb41cc271e738e9c7.mailgun.org"

SENDSMS_BACKEND = 'drip.mysmsbackend.SmsBackend'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_USE = True


SMS_DEVICE_ID = ''    #'25851'
