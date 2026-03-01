from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# Security / env
# -----------------------------
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "dev-secret-key")
DEBUG = os.getenv("DJANGO_DEBUG", "1") == "1"
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "*").split(",")

# -----------------------------
# Installed apps / middleware
# -----------------------------
from core.project_settings.installed_apps import INSTALLED_APPS
from core.project_settings.middleware import MIDDLEWARE
from core.project_settings.cors import *

ROOT_URLCONF = "core.urls"
WSGI_APPLICATION = "core.wsgi.application"

# -----------------------------
# Templates
# -----------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.pages.context_processors.global_settings",
            ],
        },
    },
]

# -----------------------------
# Database (PostgreSQL)
# -----------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "dreliar"),
        "USER": os.getenv("POSTGRES_USER", "postgres"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "postgres"),
        "HOST": os.getenv("POSTGRES_HOST", "db_dreliar"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}

# -----------------------------
# Password validation
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -----------------------------
# Internationalization
# -----------------------------
LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Asia/Bishkek"
USE_I18N = True
USE_TZ = True

# -----------------------------
# Static / Media
# -----------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# -----------------------------
# DRF + Swagger (drf-spectacular)
# -----------------------------
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Dreliar API",
    "DESCRIPTION": "API documentation",
    "VERSION": "1.0.0",
}

# -----------------------------
# CKEditor settings
# ВАЖНО: импорт ПОСЛЕ BASE_DIR чтобы не было NameError
# -----------------------------
from core.project_settings.ckeditor import *

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



# ===============================
# JAZZMIN ADMIN THEME
# ===============================
JAZZMIN_SETTINGS = {
    "site_title": "Dreliar Admin",
    "site_header": "Dr. Eliyar",
    "site_brand": "Dreliar",
    "welcome_sign": "Добро пожаловать в админку",
    "copyright": "© Dreliar",

    "show_sidebar": True,
    "navigation_expanded": True,

    "icons": {
        "cms.SiteSettings": "fas fa-cog",
        "cms.HomePage": "fas fa-home",
        "cms.Service": "fas fa-tooth",
        "cms.DoctorProfile": "fas fa-user-md",
        "cms.Case": "fas fa-briefcase-medical",
        "cms.Review": "fas fa-star",
    },
}

JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
    "navbar": "navbar-dark",
    "sidebar": "sidebar-dark-primary",
    "accent": "accent-primary",
}