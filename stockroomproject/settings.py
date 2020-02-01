import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'za(p*itskh!a7!0ed=!&lod2hukc%2l_-q!s4_q$awjgqaw12('

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stockroom',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'stockroomproject.urls'

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

WSGI_APPLICATION = 'stockroomproject.wsgi.application'

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }

    # 'default': {
    #     'ENGINE': 'sql_server.pyodbc',
    #     'NAME': '<DB NAME>',
    #     'HOST': '<HOST IP>',
    #     'USER': '<SQL SERVER USERNAME',
    #     'PASSWORD': '<SQL SERVER PASSWORD>',

    #     'OPTIONS': {
    #         'driver': 'ODBC Driver 17 for SQL Server',
    #     }
    # }


    # 'default': { # sql server
    #     'ENGINE': 'sql_server.pyodbc',
    #     'NAME': 'stockroom',
    #     'HOST': '.',
    #     'OPTIONS': {
    #         'driver': 'ODBC Driver 14 for SQL Server',
    #     }
    # },



    # 'default': {
    #     'ENGINE': 'sql_server.pyodbc',
    #     'NAME': 'mydb',
    #     'USER': 'user@myserver',
    #     'PASSWORD': 'password',
    #     'HOST': 'myserver.database.windows.net',
    #     'PORT': '',

    #     'OPTIONS': {
    #         'driver': 'ODBC Driver 13 for SQL Server',
    #     },
    # },

    # 'default': {
    #     'NAME': 'stockroom',
    #     'ENGINE': 'sqlserver_ado',
    #     'HOST': '.',
    #     'USER': '',
    #     'PASSWORD': '',
    # }


    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'stockroom',
        'USER': 'root',
        'PASSWORD': 'qHMjQkqzc8tDlCxolwFaDsf1',
        'HOST': 's9.liara.ir',
        'PORT': '33872',
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
LOGIN_REDIRECT_URL = '/'
