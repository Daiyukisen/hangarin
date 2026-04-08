import os
import socket
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-lmr#0b16px26g2+plr&y=z@nqdvwmujr9i#y=0+xi$y@x9(liu'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'unfold',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',        # ← add this
    'allauth',                     # ← add this
    'allauth.account',             # ← add this
    'allauth.socialaccount',       # ← add this
    'allauth.socialaccount.providers.google',  # ← add this
    'allauth.socialaccount.providers.github',  # ← add this
    'tasks',
    'pwa',
]

# Site ID — auto-detects local vs PythonAnywhere
if "pythonanywhere" in socket.gethostname():
    SITE_ID = 2  # production
else:
    SITE_ID = 1  # local

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # ← add this
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hangarin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'hangarin.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Auth redirects
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGIN_METHODS = {"username", "email"}
ACCOUNT_SIGNUP_FIELDS = [
    "username*",
    "email*",
    "password1*",
    "password2*",
]

# PWA Settings
PWA_APP_NAME = 'Hangarin Task To-Do'
PWA_APP_DESCRIPTION = "A Progressive Web App version of Hangarin"
PWA_APP_THEME_COLOR = '#0A0A0A'
PWA_APP_BACKGROUND_COLOR = '#FFFFFF'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'portrait'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {'src': '/static/img/logo.png', 'sizes': '512x512'},
    {'src': '/static/img/logo2.png', 'sizes': '512x512'}
]
PWA_APP_ICONS_APPLE = [
    {'src': '/static/img/logo.png', 'sizes': '512x512'},
    {'src': '/static/img/logo2.png', 'sizes': '512x512'}
]
PWA_APP_DIR = 'ltr'
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/js/serviceworker.js')