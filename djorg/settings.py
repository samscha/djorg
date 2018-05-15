"""
Django settings for djorg project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from decouple import config
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')

# CSRF_COOKIE_NAME = config("CSRF_COOKIE_NAME")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # packages
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'corsheaders',
    'rest_framework',
    # apps
    'bookmarks',
    'notes',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djorg.urls'

TEMPLATES = [  # TODO: turn into .env
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
                'django.template.context_processors.request',
            ],
        },
    },
]

CORS_ALLOW_CREDENTIALS = config(
    "CORS_ALLOW_CREDENTIALS", default=False, cast=bool)
CORS_ORIGIN_WHITELIST = config('CORS_ORIGIN_WHITELIST').split(',')

SITE_ID = config("SITE_ID", default=1, cast=int)

LOGIN_REDIRECT_URL = config("LOGIN_REDIRECT_URL")

AUTHENTICATION_BACKENDS = config("AUTHENTICATION_BACKENDS").split(',')

REST_FRAMEWORK = {
    # use django's standard `django.contrib.auth`` permissions,
    # or allow read-only access for unauthenticated users
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

WSGI_APPLICATION = 'djorg.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {}

DATABASES['default'] = dj_database_url.config(default=config("DATABASE_URL"))


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/1.9/howto/static-files/
# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
# STATIC_URL = '/static/'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# # Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
#     os.path.join(BASE_DIR, 'bookmarks/static'),
#     os.path.join(BASE_DIR, 'bookmarks/static/bookmarks'),
#     os.path.join(BASE_DIR, 'djorg'),
#     os.path.join(BASE_DIR, ''),
#     os.path.join(PROJECT_ROOT, 'staticfiles'),
# )

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
