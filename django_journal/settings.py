import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('SECRET_KEY', 'unsafe-secret-key')

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS = [
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'journal',
    'people',
    'mailing',
    'rest_framework',
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_journal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'django_journal.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'journal',
        'USER': 'root',
        'PASSWORD': '2341',
        'HOST': 'localhost',
        'PORT': '3306',
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

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# REDIS settings
REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'

# CELERY settings
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_BROKER_TRANSPORT_OPTION = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

TEACHER = 'teacher'
STUDENT = 'student'
USER_STATUS_CHOICES = [(TEACHER, 'Викладач'), (STUDENT, 'Студент')]
SCORE_CHOICES = [(60, '60'), (61, '61'), (62, '62'), (63, '63'), (64, '64'), (65, '65'), (66, '66'), (67, '67'),
                 (68, '68'),
                 (69, '69'), (70, '70'), (71, '71'), (72, '72'), (73, '73'), (74, '74'), (75, '75'), (76, '76'),
                 (77, '77'),
                 (78, '78'), (79, '79'), (80, '80'), (81, '81'), (82, '82'), (83, '83'), (84, '84'), (85, '85'),
                 (86, '86'),
                 (87, '87'), (88, '88'), (89, '89'), (90, '90'), (91, '91'), (92, '92'), (93, '93'), (94, '94'),
                 (95, '95'),
                 (96, '96'), (97, '97'), (98, '98'), (99, '99'), (100, '100'), ]
GENDER_CHOICES = [('М', 'М'), ('Ж', 'Ж')]
STUDY_CHOICES = [('Бюджет', 'Бюджет'), ('Контракт', 'Контракт')]
STUDY_DEGREE_CHOICES = [('Бакалавр', 'Бакалавр'), ('Магістр', 'Магістр')]

AUTH_USER_MODEL = 'people.User'

STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'login'
