"""
Django settings for maclo project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&fmi_gxw86%5_tm-35_ell!d4rh2e8!bkfon4qq9(xh2d5y&f1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'adminpanel',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'drf_yasg',
    'storages',
    'channels',
    'django_cron',
    'chat',
    'src',
    'fcm_django',
    'django_celery_beat'
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

CRON_CLASSES = [
    "src.cron.MyCronJob",
]

ROOT_URLCONF = 'maclo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# REST_FRAMEWORK = {
#     'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
# }

WSGI_APPLICATION = 'maclo.wsgi.application'
ASGI_APPLICATION = 'maclo.routing.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [('127.0.0.1', 6379)],
#         },
#     },
# }
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}

# local Geo database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': 'maclo',
#         'USER': 'postgres',
#         'PASSWORD': 'test123',
#         'HOST': 'localhost',
#         'PORT': '5432'
#     }
# }
# Production Geo Database
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'dating',
        'USER': 'maclo',
        'PASSWORD': 'maclo',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False

AUTH_USER_MODEL = 'adminpanel.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# STATIC_URL = '/static/'
MEDIA_URL = '/media/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

DEFAULT_FROM_EMAIL = 'maclodatingapp@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'maclodatingapp@gmail.com'
EMAIL_HOST_PASSWORD = 'mahirkashyap'
EMAIL_PORT = 587
SERVER_EMAIL = 'maclodatingapp@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        # 'src.CustomTokenAuthentication.CustomTokenAuthentication'
    ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',)
}
# S3 BUCKETS CONFIG

AWS_ACCESS_KEY_ID = 'AKIAYC6UDNTP4JZJHA6C'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'maclobucket'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_FILE_OVERWRITE = False
AWS_S3_REGION_NAME = "ap-south-1"
AWS_S3_HOST = "s3.ap-south-1.amazonaws.com"
AWS_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
AWS_DEFAULT_ACL = None

AWS_QUERYSTRING_AUTH = False
FCM_DJANGO_SETTINGS = {
    "FCM_SERVER_KEY": "AAAAORwXGTc:APA91bFzV3R5Agp3wnrvhYwGbA4n-v5x-sBF9_nAgwPv6HVl92RyNontEw0A8RzNOQvVTOOKvKzpU_XrFFg--uAvkazmFfL03X71XjUe8CEZiLUmLtVfho4jtDVXdmm6rrfPkOqdroP6"
}
'''
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>POST</AllowedMethod>
    <AllowedMethod>PUT</AllowedMethod>
    <AllowedHeader>*</AllowedHeader>
</CORSRule>
</CORSConfiguration>
'''
# {
#     "Version": "2008-10-17",
#     "Statement": [
#         {
#             "Sid": "AllowEveryoneReadOnlyAccess",
#             "Effect": "Allow",
#             "Principal": "*",
#             "Action": [
#                 "s3:GetObject",
#                 "s3:ListBucket"
#             ],
#             "Resource": [
#                 "arn:aws:s3:::maclobucket",
#                 "arn:aws:s3:::maclobucket/*"
#             ]
#         }
#     ]
# }
# {
#     "Version": "2020-12-31",
#     "Statement": [
#         {
#             "Sid": "AllowEveryoneReadOnlyAccess",
#             "Effect": "Allow",
#             "Principal": "*",
#             "Action": [
#                 "s3:GetObject",
#                 "s3:ListBucket"
#             ],
#             "Resource": [
#                 "arn:aws:s3:::maclobucket",
#                 "arn:aws:s3:::maclobucket/*"
#             ]
#         }
#     ]
# }
# git push -u origin master
