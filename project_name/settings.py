from {{project_name}}.environment_settings import *
#############################################################
# ENVIRONMENT SETTINGS TEMPLATE

# import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# location = lambda x: os.path.join(
#     os.path.dirname(os.path.realpath(__file__)), x)

# SECRET_KEY = '{{secret_key}}'

# DEBUG = True

# ALLOWED_HOSTS = []

# BASE_URL = 'localhost:8000'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# CONTACT_EMAIL="info@example.com"

# STATIC_ROOT = location('static')

# MEDIA_ROOT = location('media')

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = CONTACT_EMAIL
# EMAIL_HOST_PASSWORD = 'dfgd4r33r'
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = CONTACT_EMAIL
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
##################################################################

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

PLUGIN_APPS = (
    'compressor',
    # 'emailusernames',
)

PROJECT_APPS = tuple('{{project_name}}.'+app for app in [
    'dashboard',
    '#firstAppName#',
])

INSTALLED_APPS = DJANGO_APPS + PLUGIN_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '{{project_name}}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            location('templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug':DEBUG,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                '{{project_name}}.context_processors.string_resources',
                # 'emailusernames.context_processors.user_resources',
            ],
        },
    },
]

WSGI_APPLICATION = '{{project_name}}.wsgi.application'

FIXTURE_DIRS = (
    #project fixtures dir
    location('fixtures'),
)

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

CURRENCY = 'INR'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATE_FORMAT = 'N j, Y'
TIME_FORMAT = 'g : i A'
DATETIME_FORMAT = DATE_FORMAT + ' ' + TIME_FORMAT
# TIME_INPUT_FORMATS = ('%I:%M %p',)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    location('project-static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

DASHBOARD_HOME_URL = "/dashboard/#firstAppName#"

# AUTH_USER_MODEL = 'emailusernames.User'
# EMAILUSERNAMES_VERIFY = False
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/login-redirect'

ORG_NAME = 'Organisation name'
SITE_NAME = 'example.com'
