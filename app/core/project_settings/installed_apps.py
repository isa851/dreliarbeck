INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "jazzmin",

    # Third-party
    "rest_framework",
    "django_filters",
    "drf_spectacular",
    "corsheaders",

    # CKEditor
    "ckeditor",
    "ckeditor_uploader",

    # resized images
    "django_resized",

    # Local apps
    "apps.base",
    "apps.cms",
    "apps.contacts",
]