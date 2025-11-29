from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-pcu#gbaw8(7s#_^khsl*c0@6m@q8-qecetn5b5dw@v%dec#n4#'

# -------------------------------
# DEPLOY SETTINGS
# -------------------------------
DEBUG = False   # WAJIB: False kalau deploy
ALLOWED_HOSTS = ["*", ".onrender.com", "127.0.0.1", "localhost"]

# -------------------------------
# INSTALLED APPS
# -------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'kasir',
]

# -------------------------------
# MIDDLEWARE
# -------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # WAJIB untuk deploy
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'kasir.middleware.KasirAccessMiddleware',
]

ROOT_URLCONF = 'RajawaliKasir.urls'

# -------------------------------
# TEMPLATES
# -------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'kasir' / 'templates' ],
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

WSGI_APPLICATION = 'RajawaliKasir.wsgi.application'

# -------------------------------
# DATABASE
# -------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------------------
# PASSWORD VALIDATION
# -------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------------
# TIMEZONE
# -------------------------------
LANGUAGE_CODE = 'id'
TIME_ZONE = 'Asia/Jakarta'
USE_TZ = True

# -------------------------------
# STATIC FILES (WAJIB RENDER)
# -------------------------------
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'kasir' / 'static',
]

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# -------------------------------
# MEDIA FILES (FOTO PRODUK)
# -------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# -------------------------------
# QRIS STRING
# -------------------------------
QRIS_CONTENT = "00020101021126570011ID.DANA.WWW011893600915300002945402090000294540303UMI51440014ID.CO.QRIS.WWW0215ID20243643578790303UMI5204549953033605802ID5911Cv Rajawali6004740461058577263043EDF"

# -------------------------------
# LOGIN SETTINGS
# -------------------------------
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
