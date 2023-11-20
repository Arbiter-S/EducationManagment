import os
from datetime import timedelta
from pathlib import Path

from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-+!h#t6&-pasj8$l2tvhlri7g1%^n-y72d0yth(nnw0jv7wq125"

DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = "user.User"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Local
    "user.apps.UserConfig",
    "university.apps.UniversityConfig",
    "department.apps.DepartmentConfig",
    "course.apps.CourseConfig",
    "course_selection.apps.CourseSelectionConfig",
    # third Party
    "rest_framework",
    "django_filters",
    "drf_spectacular",
    "minio_storage",
    "rosetta",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "edu.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "edu.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# MINIO

# DEFAULT_FILE_STORAGE = "minio_storage.storage.MinioMediaStorage"
# STATICFILES_STORAGE = "minio_storage.storage.MinioStaticStorage"
# MINIO_STORAGE_ENDPOINT = os.getenv("MINIO_STORAGE_ENDPOINT")
# MINIO_EXTERNAL_STORAGE_ENDPOINT = os.getenv("MINIO_EXTERNAL_STORAGE_ENDPOINT")
# MINIO_STORAGE_ACCESS_KEY = os.getenv("MINIO_STORAGE_ACCESS_KEY")
# MINIO_STORAGE_SECRET_KEY = os.getenv("MINIO_STORAGE_SECRET_KEY")
# MINIO_STORAGE_USE_HTTPS = False
# MINIO_STORAGE_MEDIA_BUCKET_NAME = os.getenv("MINIO_STORAGE_MEDIA_BUCKET_NAME", default="media")
# MINIO_STORAGE_MEDIA_USE_PRESIGNED = True
# MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True
# MINIO_STORAGE_MEDIA_URL = os.getenv(
#     "MINIO_STORAGE_MEDIA_URL", default=f"{MINIO_EXTERNAL_STORAGE_ENDPOINT}/{MINIO_STORAGE_MEDIA_BUCKET_NAME}"
# )
# MINIO_STORAGE_STATIC_BUCKET_NAME = os.getenv("MINIO_STORAGE_STATIC_BUCKET_NAME", default="static")
# MINIO_STORAGE_STATIC_USE_PRESIGNED = True
# MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = True
# MINIO_STORAGE_STATIC_URL = os.getenv(
#     "MINIO_STORAGE_STATIC_URL", default=f"{MINIO_EXTERNAL_STORAGE_ENDPOINT}/{MINIO_STORAGE_STATIC_BUCKET_NAME}"
# )

# CACHES

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv("CACHE_LOCATION"),
        "TIMEOUT": 600,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
    },
}

# CELERY

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_TIMEZONE = os.getenv("TIME_ZONE", default="Asia/Tehran")

# SMTP

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")

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

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
]

# REST_FRAMEWORK

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "60/minute",
        "user": "1000/minute",
    },
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_METADATA_CLASS": "metadata.CustomMetaData",
}

if os.getenv("DISABLE_BROWSEABLE_API", default=False):
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = ["rest_framework.renderers.JSONRenderer"]
else:
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = ["rest_framework.renderers.BrowsableAPIRenderer"]

# DRF SPECTACULAR

SPECTACULAR_SETTINGS = {
    "TITLE": "Quera University",
    "DESCRIPTION": "APIs Document For The Quera University's Django Application",
    "VERSION": "1.0.0",
}

# LOGGING

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "general.log",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console", "file"],
            "level": os.getenv("DJANGO_LOG_LEVEL", default="INFO"),
        },
    },
    "formatters": {
        "verbose": {
            "format": "{asctime} ({levelname}) - {name} - {message}",
            "style": "{",
        },
    },
}

# ROSETTA

LANGUAGES = [
    ("en", _("English")),
    ("fa", _("Persian")),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": os.getenv("JWT_ACCESS_TOKEN_LIFETIME", default=900),
    "REFRESH_TOKEN_LIFETIME": os.getenv("JWT_REFRESH_TOKEN_LIFETIME", default=259200),
    "ROTATE_REFRESH_TOKENS": os.getenv("JWT_ROTATE_REFRESH_TOKENS", default=True),
    "BLACKLIST_AFTER_ROTATION": os.getenv("JWT_BLACKLIST_AFTER_ROTATION", default=True),
    "UPDATE_LAST_LOGIN": os.getenv("JWT_UPDATE_LAST_LOGIN", default=False),
    "ALGORITHM": os.getenv("JWT_ALGORITHM", default="HS256"),
    "SIGNING_KEY": os.getenv("JWT_SIGNING_KEY"),
    "VERIFYING_KEY": os.getenv("JWT_VERIFYING_KEY", default=""),
    "AUDIENCE": os.getenv("JWT_AUDIENCE", default=None),
    "ISSUER": os.getenv("JWT_ISSUER", default=None),
    "JSON_ENCODER": os.getenv("JWT_JSON_ENCODER", default=None),
    "JWK_URL": os.getenv("JWT_JWK_URL", default=None),
    "LEEWAY": os.getenv("JWT_LEEWAY", default=0),
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = os.getenv("TIME_ZONE", default="Asia/Tehran")

USE_I18N = True

USE_TZ = True

STATIC_URL = os.getenv("STATIC_URL", default="/static/")

MEDIA_URL = os.getenv("MEDIA_URL", default="/media/")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
