"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from decouple import config
import os

""" VAR ----------------------------------------------------------------------------------------"""
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'asdasasdsadasdsad2231231'
ROOT_URLCONF = 'core.urls'
AUTH_USER_MODEL = 'accounts.User'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

SERVER = False
DEBUG = True

if SERVER:
    ALLOWED_HOSTS = ['maihandost.com']
    GOOGLE_CALLBACK_ADDRESS = "http://maihandost.com/accounts/google/login/callback/"
    SITE_ID = 3
else:
    ALLOWED_HOSTS = ['*']
    GOOGLE_CALLBACK_ADDRESS = "http://127.0.0.1:8000/accounts/google/login/callback/"
    SITE_ID = 1

""" APPS ---------------------------------------------------------------------------------------"""
INSTALLED_APPS = [
    # 'src.admins.apps.AppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',

    # REQUIRED_APPLICATIONS
    'crispy_forms',
    'ckeditor',
    'django_filters',

    'rest_framework',
    'rest_framework.authtoken',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # CUSTOM APPS
    'src.website',
    'src.accounts',
    'src.api',

    'src.admins',
    'src.customer',

    # MUST BE AT THE END
    'notifications'

]

""" MIDDLE WARES ----------------------------------------------------------------------------"""
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

""" TEMPLATES -------------------------------------------------------------------------------"""
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

WSGI_APPLICATION = 'core.wsgi.application'

""" DATABASES ------------------------------------------------------------------------------------"""
if not SERVER:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'myproject',
            'USER': 'myprojectuser',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

""" VALIDATORS -----------------------------------------------------------------------------------"""

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

""" INTERNATIONALIZATION -------------------------------------------------------------------------"""

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_L10N = True
USE_TZ = True

""" STATIC AND MEDIA ----------------------------------------------------------------------------"""

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

""" OTHER APPS SYSTEM ----------------------------------------------------------------------------"""
CRISPY_TEMPLATE_PACK = 'bootstrap4'

""" LOGIN SYSTEM ---------------------------------------------------------------------------------"""
LOGIN_REDIRECT_URL = '/accounts/cross-auth/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

""" EMAIL SYSTEM ---------------------------------------------------------------------------------"""

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'donald.duck0762@gmail.com'
EMAIL_HOST_PASSWORD = 'ugtykpnhepxvchqz'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'Support-Team <themaihandost01@gmail.com>'

# EMAIL_HOST = 'smtp.office365.com'
# EMAIL_HOST_USER = 'themaihandost01@gmail.com'
# EMAIL_HOST_PASSWORD = 'poiu098765'
# SERVER_EMAIL = EMAIL_HOST_USER
# EMAIL_PORT = 587
# EMAIL_USE_SSL = False
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'Support-Team <support@maihandostmentpro.com>'

""" RESIZER IMAGE --------------------------------------------------------------------------------"""
DJANGORESIZED_DEFAULT_SIZE = [1920, 1080]
DJANGORESIZED_DEFAULT_QUALITY = 75
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'JPEG'
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {
    'JPEG': ".jpg",
    'PNG': ".png",
    'GIF': ".gif"
}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True

""" ALL-AUTH SETUP --------------------------------------------------------------------------------"""

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

ACCOUNT_LOGOUT_ON_GET = True
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
OLD_PASSWORD_FIELD_ENABLED = True
LOGOUT_ON_PASSWORD_CHANGE = False
ACCOUNT_EMAIL_VERIFICATION = 'none'

