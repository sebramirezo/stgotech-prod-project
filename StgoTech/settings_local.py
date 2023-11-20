from StgoTech.settings import *

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'inventario_stgotech', 
        'USER': 'postgres',
        'PASSWORD': '123asdzxc',
        'HOST': 'localhost', 
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')