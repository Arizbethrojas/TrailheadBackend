import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import timedelta

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Add this to handle static files
STATIC_URL = '/static/'  # Keep only this definition
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'frontend')]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-!(=z%!^6nx%uw)8lmw&#^t*0z!95jlw6ba6alk&ba@c7vbx_qu"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

PORT = os.environ.get("PORT")

ALLOWED_HOSTS = ['trailheadbackend.onrender.com']

# Handle media 
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "rest_framework",
    "django.contrib.staticfiles",
    "webapp",
    "corsheaders",  # Added for CORS
]

# Rest framework configuration (JWT Authentication)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# JWT Settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),  
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,  
    'BLACKLIST_AFTER_ROTATION': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': os.getenv('JWT_SECRET', 'your-default-secret-key'),
    'VERIFYING_KEY': None,  
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# Middleware configuration
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # Added for CORS support
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",  # Ensures session handling
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",  # CSRF handling, if you're using it
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # Authentication middleware
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "trailhead.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'frontend')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "trailhead.wsgi.application"

# Database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization settings
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files settings
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'frontend')]  # Ensure this points to your React app

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CORS settings (allow access from frontend)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Allow React frontend
    "https://utrekfrontend.onrender.com", #On render
]

# Allow credentials in CORS requests
CORS_ALLOW_CREDENTIALS = True

# CSRF Settings (to allow cross-origin requests)
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",  # Allow React frontend
    "https://utrekfrontend.onrender.com", #On render
]

# CSRF Exemptions (for API Views that handle external requests, like registration)
CSRF_COOKIE_NAME = "csrftoken"
CSRF_COOKIE_HTTPONLY = False  # Allow to access the CSRF token in JS

# Redirect URLs after login/logout
LOGIN_REDIRECT_URL = '/'  # Where you want users to go after logging in
LOGOUT_REDIRECT_URL = '/'  # Redirect after logging out

