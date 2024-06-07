"""
Django settings for organizer project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
"Ruta base de la carpetas del proyecto"
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
"Llave de seguridad que brinda una encriptacion a usuarios para nuestro proyecto"
SECRET_KEY = '1op2m3o1 m2o3me-i!nli=dh5%sdl$vmpi%89#l1q)39gpdv#(rag-k$fc=wx1zrty'

# SECURITY WARNING: don't run with debug turned on in production!
"Variable para decirle a nuestra app si esta en produccion o desarrollo (DEBUG = False -> Desarrollo)"
DEBUG = True

"Dominios para tu aplicacion cuando este desplegada"
ALLOWED_HOSTS = []


# Application definition

"Todas las aplicaciones de tu proyecto DJANGO, ya viene un par pre instaladas"
"Aqui debes agregar tus aplicaciones creadas"
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo_app.apps.TodoAppConfig',
    'authenticate_app.apps.AuthenticateAppConfig'
]

"Configuracion de seguridad por defecto de Dajango para nuestros proyecto"
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

"Ruta prinicipal del proyecto donde indica las URLS permitidas"
ROOT_URLCONF = 'organizer.urls'

"Indica donde estan ubicados los templates/HTML para Django"
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

"Para realizar despliegues a produccion"
WSGI_APPLICATION = 'organizer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

"Configuracion de la base de datos"
"Por defecto es SQLite3, tu puedes cambiarlo para produccion a MySQL o Postgres"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

"Configuracion de validadores de passwords"
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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

"Idioma en como nos hablara Django"
LANGUAGE_CODE = 'es-pe'

"Zona horaria para tu pagina web"
TIME_ZONE = 'America/Lima'

"Sirve para adaptar contenido de forma internacional"
USE_I18N = True

"Uso de UTC para tu base de datos"
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

"Ruta para indicarle a Django donde estan los archivos estaticos"
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

"Si no agregas a tus modelos la columna de id/PK Django te lo agregara automaticamente y de manera autoincrementada"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
