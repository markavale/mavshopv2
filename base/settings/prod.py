'''Use this for production'''
import os
import dj_database_url
from .base import *

DEBUG = True
ALLOWED_HOSTS += [ 'markvale15.herokuapp.com'] # PUT HERE YOUR DOMAIN NAME WHEN YOU DEPLOY YOUR WEB APP
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
# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.getenv('DATABASE_URL')
#     )
# }
CORS_ALLOWED_ORIGINS = [
    'http://markvale15.herokuapp.com'
    # 'http://localhost:8080',
    # 'http://localhost:8081',
    # 'http://localhost:3307',
    # 'http://localhost:3306'
]
CORS_ORIGIN_WHITELIST = [
    'http://markvale15.herokuapp.com'
    # 'http://localhost:8080',
    # 'http://localhost:8081',
    # 'http://localhost:3307',
    # 'http://localhost:3306'
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
    os.path.join(BASE_DIR / '../dist/static',)
    ]


##########
# STATIC #
##########

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

