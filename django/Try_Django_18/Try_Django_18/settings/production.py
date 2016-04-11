""" You can put prudction server info here.

-- server name:
-- ssh username:
-- ssh password:

-- database name:
-- db user:
-- db password:

And of course some additional info
"""
from django.conf import settings

if not settings.DEBUG:
    import os

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '(3jtd-fkzzb(*(5-rwk144j82xga8r^f&6gezto3a=om5m8ed2'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    # Uncomment line below and add admins
    # ADMINS = (("NAME", "EMAIL"),)

    ALLOWED_HOSTS = ['*']

    # Configured Email Host
    EMAIL_HOST = 'not-working.email.host'
    EMAIL_PORT = 25


    # Application definition

    INSTALLED_APPS = [
        'registration',  # 3rd party app
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'crispy_forms',  # 3rd party app
        'newsletter',
        'contact',
    ]

    MIDDLEWARE_CLASSES = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'Try_Django_18.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

    WSGI_APPLICATION = 'Try_Django_18.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/1.9/ref/settings/#databases

    """ Example of production database

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'mvpland',
            'USER': 'cfedeploy',
            'PASSWORD': 'super-duper-hard-password',
        }
    }


    """

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


    # Internationalization
    # https://docs.djangoproject.com/en/1.9/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.9/howto/static-files/

    STATIC_URL = '/static/'

    # Directory to serve static files after deploy (AKA when in production)
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

    # Directories where to look for 'global'/non-app static files
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )

    # ... and same for Media (not necessary needed)
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'mediafiles')

    # Crispy Form Template
    CRISPY_TEMPLATE_PACK = 'bootstrap3'

    # Django Registration Redux settings
    ACCOUNT_ACTIVATION_DAYS = 7
    REGISTRATION_AUTO_LOGIN = False
    SITE_ID = 1
    LOGIN_REDIRECT_URL = "/"
    REGISTRATION_DEFAULT_FROM_EMAIL = "trydjango18@no-good.com"
