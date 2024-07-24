from pathlib import Path
import os
import dj_database_url

# Load environment variables from env.py if it exists
if os.path.isfile('env.py'):
    import env

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key for the project
SECRET_KEY = os.getenv('SECRET_KEY')

# Debug mode - should be False in production
DEBUG = 'DEV' in os.environ

# Allowed hosts
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.herokuapp.com',
]

# CSRF trusted origins
CSRF_TRUSTED_ORIGINS = [
    'https://*.codeinstitute-ide.net',
    'https://*.herokuapp.com',
]

# CORS settings
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN'),
        os.environ.get('CLIENT_ORIGIN_DEV'),
    ]
else:
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r"^https://.*\.codeinstitute-ide\.net$",
    ]

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

# Cloudinary settings
CLOUDINARY_STORAGE = {'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')}
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Installed applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'corsheaders',
    'django_filters',
    'taggit',
    'cloudinary',
    'cloudinary_storage',
    'users',
    'posts',
    'reports',
    'comments',
    'contact',
    'likes',
    'news',
    'bookmarks',
    'followers',
]

SITE_ID = 1

# Middleware configuration
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

# Root URL configuration
ROOT_URLCONF = 'api_blog.urls'

# Template settings
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

# WSGI application
WSGI_APPLICATION = 'api_blog.wsgi.application'

# Database configuration
if 'DEV' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }

# Password validation
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

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Stockholm'
USE_I18N = True
USE_TZ = True

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django REST framework configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        (
            'rest_framework.authentication.SessionAuthentication'
            if 'DEV' in os.environ
            else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
        )
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12,
    'DATETIME_FORMAT': '%d %b %Y',
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
    ],
}

# Use JSON renderer in non-development environments
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]

# REST authentication settings
REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_SECURE': True,
    'JWT_AUTH_COOKIE': 'my-app-auth',
    'JWT_AUTH_REFRESH_COOKIE': 'my-refresh-token',
    'JWT_AUTH_SAMESITE': 'None',
    'USER_DETAILS_SERIALIZER': 'api_blog.serializers.CurrentUserSerializer',
}
