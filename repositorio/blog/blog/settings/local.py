from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        # Motor de la base de datos
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_c',
        # Credenciales de acceso
        'USER': 'root',
        'PASSWORD': 'root',
        # Host y puerto
        'HOST': 'localhost',
        'PORT': '',
    }
}