from pathlib import Path
from decouple import config
from django.urls import reverse_lazy
from urllib.parse import urlparse

BASE_DIR = Path(__file__).resolve().parent.parent

# ── Seguridad ─────────────────────────────
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(",")])

# ── Apps y middleware ─────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.account',
    'apps.images',
    'apps.actions',

    'social_django',
    'easy_thumbnails',
]

if DEBUG:
    INSTALLED_APPS += ['django_extensions', 'debug_toolbar']


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE


ROOT_URLCONF = 'core.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates'],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'core.context_processors.site_settings',
        ],
    },
}]

WSGI_APPLICATION = 'core.wsgi.application'


# ── Base de datos ─────────────────────────
DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}


# ── Archivos estáticos y media ───────────
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ==============================
# AUTH
# ==============================
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'apps.account.authentication.EmailAuthBackend',
    'social_core.backends.google.GoogleOAuth2',
]


# ==============================
# COOKIES (IMPORTANTE PARA OAUTH)
# ==============================
SESSION_COOKIE_SAMESITE = config('SESSION_COOKIE_SAMESITE')
CSRF_COOKIE_SAMESITE = config('CSRF_COOKIE_SAMESITE')


# ==============================
# SOCIAL AUTH
# ==============================
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('GOOGLE_OAUTH2_SECRET')

SOCIAL_AUTH_PIPELINE = [
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'apps.account.authentication.create_profile',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
]


# ==============================
# EMAIL
# ==============================
EMAIL_BACKEND = config(
    "EMAIL_BACKEND",
    default='django.core.mail.backends.console.EmailBackend'
)


# ==============================
# REDIS
# ==============================
REDIS_URL = config("REDIS_URL", default="redis://localhost:6379/0")
parsed_redis = urlparse(REDIS_URL)

REDIS_HOST = parsed_redis.hostname
REDIS_PORT = parsed_redis.port
REDIS_DB = int(parsed_redis.path.lstrip("/"))


# ── Internacionalización ──────────────────
LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ==============================
# DEBUG TOOLBAR
# ==============================
if DEBUG:
    INTERNAL_IPS = ['127.0.0.1']


# ==============================
# SECURITY (PROD)
# ==============================
if not DEBUG:

    # Protección básica contra ataques XSS en el navegador
    SECURE_BROWSER_XSS_FILTER = config('SECURE_BROWSER_XSS_FILTER', cast=bool)

    # Evita que el navegador adivine tipos de archivos (seguridad)
    SECURE_CONTENT_TYPE_NOSNIFF = config('SECURE_CONTENT_TYPE_NOSNIFF', cast=bool)

    # Bloquea que el sitio se cargue en iframes (anti clickjacking)
    X_FRAME_OPTIONS = config('X_FRAME_OPTIONS')

    # Fuerza HTTPS por X segundos (HSTS)
    SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', cast=int)

    # Aplica HSTS también a subdominios
    SECURE_HSTS_INCLUDE_SUBDOMAINS = config('SECURE_HSTS_INCLUDE_SUBDOMAINS', cast=bool)

    # Permite incluir el dominio en listas HSTS de navegadores
    SECURE_HSTS_PRELOAD = config('SECURE_HSTS_PRELOAD', cast=bool)

    # Indica a Django que está detrás de un proxy (ej: Nginx con HTTPS)
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Usa el host enviado por el proxy
    USE_X_FORWARDED_HOST = config('USE_X_FORWARDED_HOST', cast=bool)

    # Redirige todo el tráfico a HTTPS
    SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', cast=bool)

    # Cookies de sesión solo por HTTPS
    SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', cast=bool)

    # Cookie CSRF solo por HTTPS
    CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', cast=bool)

    # Dominios permitidos para CORS (frontend que consume tu API)
    CORS_ALLOWED_ORIGINS = config(
        "CORS_ALLOWED_ORIGINS",
        cast=lambda v: [s.strip() for s in v.split(",")]
    )

    # Dominios confiables para protección CSRF
    CSRF_TRUSTED_ORIGINS = config(
        "CSRF_TRUSTED_ORIGINS",
        cast=lambda v: [s.strip() for s in v.split(",")]
    )


# ==============================
# OVERRIDES
# ==============================
ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('user_detail', args=[u.username])
}
