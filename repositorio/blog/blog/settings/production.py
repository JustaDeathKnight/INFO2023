from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['JaDK.pythonanywhere.com']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

DATABASES = {
    'default': {
        # Motor de la base de datos
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'JaDK$blog_cocina',
        # Credenciales de acceso
        'USER': 'JaDK',
        'PASSWORD': 'informatorio2023',
        # Host y puerto
        'HOST': 'JaDK.mysql.pythonanywhere-services.com',
        'PORT': '',
    }
}