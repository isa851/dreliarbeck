from django.urls import path
from .views import about_the_clinic_page

urlpatterns = [
    path("aboutTheClinic/", about_the_clinic_page, name="aboutTheClinic"),
]