"""
Django settings for website_2 project.

Generated by 'django-admin startproject' using Django 2.2.3.

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
SECRET_KEY = '))l#)vsarebwstlvmlf$-8=co%=dr-$!m^pbrho=3p2@8vl$xw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', '142.93.148.139', 'danpapa.com', 'www.danpapa.com']


# Application definition

INSTALLED_APPS = [
    'social_django',
    'a_thing.apps.AThingConfig',

    'django_plotly_dash.apps.DjangoPlotlyDashConfig',

    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'two_factor',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Always include for two-factor auth
    'django_otp.middleware.OTPMiddleware',
    # Include for twilio gateway
    'two_factor.middleware.threadlocals.ThreadLocals'


]

ROOT_URLCONF = 'website_2.urls'

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

WSGI_APPLICATION = 'website_2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

LOGIN_REDIRECT_URL = 'a_thing:home'
#To activate 2FA (command the line above)
# LOGIN_REDIRECT_URL = 'a_thing:phone_verification'

LOGIN_URL = 'a_thing:login'
LOGOUT_URL = 'a_thing:logout'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'a_thing.authentication.EmailAuthBackend',


    'social_core.backends.google.GoogleOAuth2',
]

# social auth settings
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='811359602269-5h2v4v2ior5pf2tmj88teglmot6ck6hq.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET='hAuPiwfPf5PpRjHCbeJJ4UMr'

# Authy application Key
ACCOUNT_SECURITY_API_KEY = 'r4TzQiViAkzMcEz0Pk4d7ONXjTAhi4Zz'