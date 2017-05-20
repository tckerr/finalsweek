import os

try:
    import finalsweek_auth as credentials
except:
    raise Exception("No 'finalsweek_auth' module defined in finalsweek root; Please define an authorization module.")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = credentials.secret_key

MONGO_CONNECTION_HOST = credentials.mongo_connection_host
MONGO_CONNECTION_PORT = credentials.mongo_connection_port

DEBUG = True
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'localhost:4200',
    'testserver'
]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CORS_ORIGIN_WHITELIST = ALLOWED_HOSTS

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_framework',
    'rest_framework.authtoken',
    'django_extensions',
    'rest_auth',
    'rest_auth.registration',
    'corsheaders',
    'game',
    'configuration',
    'api',
]
ACCOUNT_EMAIL_VERIFICATION = "none"

# FOR REST AUTH REGISTRATION
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND':  'django.template.backends.django.DjangoTemplates',
        'DIRS':     [],
        'APP_DIRS': True,
        'OPTIONS':  {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     credentials.app_db_name,
        'USER':     credentials.app_username,
        'PASSWORD': credentials.app_password,
        'HOST':     credentials.db_connection_host,
        'PORT':     credentials.db_connection_port,
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':     [],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

FINALSWEEK_LOG_DIR = BASE_DIR + "/log/games/"

LOGGING = {
    'version':  1,
    'filters':  {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level':   'DEBUG',
            'filters': ['require_debug_true'],
            'class':   'logging.StreamHandler',
        }
    },
    'loggers':  {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'django.db.backends': {
            'level':    'WARNING',
            'handlers': [
                'console',
            ],
        }
    }
}
