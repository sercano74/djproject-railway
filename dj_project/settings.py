# En CMD
# .\venv\Scripts\activate
# python manage.py runserver
# admin 123

import os
from dotenv import load_dotenv
load_dotenv()
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$cr-b)z8n*@egl-98+a^a4fifvzqud)9iz3^c$d!(te9g9(21%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1','web-production-4b4d6.up.railway.app',]

# CSRF_TRUSTED_ORIGINS=['https://web-production-4b4d6.up.railway.app/','http://*']
CSRF_TRUSTED_ORIGINS=['https://web-production-4b4d6.up.railway.app', 'http://*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'home',
    'blog',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dj_project.urls'

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

WSGI_APPLICATION = 'dj_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES ={
'default':dj_database_url.config(default=os.getenv('DATABASE_URL'))
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'     # Ruta para acceder desde web
# MEDIA_URL = 'https://tu-dominio.com/media/'  # Para producción

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')   # Ruta en el pc
# MEDIA_ROOT = '/var/www/tu-proyecto/media/'  # Ruta en el servidor

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS=[
                os.path.join(BASE_DIR,'blog/static'),
                os.path.join(BASE_DIR,'home/static'),
                ]

STATIC_ROOT =os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Configuración de correo electrónico
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Ejemplo para Gmail
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ordered.dev.01@gmail.com'  # Tu dirección de correo electrónico
EMAIL_HOST_PASSWORD = 'bedwoujjjskxbvod'  # Tu contraseña de correo electrónico
DEFAULT_FROM_EMAIL = 'ordered.dev.01@gmail.com'  # Dirección de correo electrónico remitente por defecto
EMAIL_DESTINATARIO = 'sergio.cannobbio@gmail.com'  # La dirección a la que se enviarán los mensajes

