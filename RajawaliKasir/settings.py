from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-pcu#gbaw8(7s#_^khsl*c0@6m@q8-qecetn5b5dw@v%dec#n4#'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    # Django bawaan...
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # App kita
    'kasir',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Role access control
    'kasir.middleware.KasirAccessMiddleware',
]


ROOT_URLCONF = 'RajawaliKasir.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'kasir' / 'templates',   # <--- PENTING
        ],
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

QRIS_CONTENT = "00020101021126570011ID.DANA.WWW011893600915300002945402090000294540303UMI51440014ID.CO.QRIS.WWW0215ID20243643578790303UMI5204549953033605802ID5911Cv Rajawali6004740461058577263043EDF"


WSGI_APPLICATION = 'RajawaliKasir.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


LANGUAGE_CODE = 'id'
TIME_ZONE = 'Asia/Jakarta'
USE_TZ = True


# STATIC
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'kasir' / 'static',
]

# MEDIA → WAJIB untuk upload foto
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Login Setting
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
