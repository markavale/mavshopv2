'''Use this for production'''
import os
import dj_database_url
from .base import *

DEBUG = False
ALLOWED_HOSTS += [ 'markanthonyvale.herokuapp.com'] # PUT HERE YOUR DOMAIN NAME WHEN YOU DEPLOY YOUR WEB APP
SECRET_KEY = config('SECRET_KEY')#
WSGI_APPLICATION = 'base.wsgi.prod.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'db_name',
#         'USER': 'db_user',
#         'PASSWORD': 'db_password',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

############
# DATABASE #
############
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}
CORS_ALLOWED_ORIGINS = [
    'https://markanthonyvale.herokuapp.com',
    # 'http://markanthonyvale.herokuapp.com',
    # 'http://markanthonyvale.herokuapp.com'
    # 'http://localhost:8080',
    # 'http://localhost:8081',
    # 'http://localhost:3307',
    # 'http://localhost:3306'
]

CSRF_TRUSTED_ORIGINS = [
    'https://markanthonyvale.herokuapp.com',
    # 'http://markanthonyvale.herokuapp.com',
]
CORS_ALLOW_ALL_ORIGINS = False
CORS_ORIGIN_WHITELIST = [
    'https://markanthonyvale.herokuapp.com',
    # 'http://markanthonyvale.herokuapp.com',
    # 'http://localhost:8080',
    # 'http://localhost:8081',
    # 'http://localhost:3307',
    # 'http://localhost:3306'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'dist' ], # BASE_DIR / 'templates' depends on frontend => build
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

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': config('NAME'),
#         'USER': config('USER'),
#         'PASSWORD': config('PASSWORD'),
#         'PORT':config('PORT', cast=int),
#         'HOST':config('HOST'),
#         #'SSL':
#     }
#}

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
# MIDDLEWARE_CLASSES += (
#     'whitenoise.middleware.WhiteNoiseMiddleware',
# )

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

STATIC_URL = '/static/'
# Place static in the same location as webpack build files
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'dist/static'
    ]


##########
# STATIC #
##########

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


#HTTPS Redirect
# settings.py
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

