from StgoTech.settings import *

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('NAME_DB_LOCAL'), 
        'USER': os.getenv('USER_DB_LOCAL'),
        'PASSWORD': os.getenv('PASS_DB_LOCAL'),
        'HOST': os.getenv('HOST_DB_LOCAL'), 
        'PORT': os.getenv('PORT_DB_LOCAL'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')