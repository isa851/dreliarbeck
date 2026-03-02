from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("apps.pages.urls")),
    path("", include("apps.aboutTheClinic.urls")),
    path("", include("apps.services.urls")),
    path("", include("apps.tur.urls")),
    path("", include("apps.cases.urls")),
    path("", include("apps.reviews.urls")),
    path("", include("apps.contacts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)