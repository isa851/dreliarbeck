from django.urls import path
from .views import (
    index_page,
    services_page,
    cases_page,
    reviews_page,
    doctor_page,
    contacts_page,
    tour_page,
)

urlpatterns = [
    path("", index_page, name="index"),
    path("services/", services_page, name="services"),
    path("cases/", cases_page, name="cases"),
    path("reviews/", reviews_page, name="reviews"),
    path("doctor/", doctor_page, name="doctor"),
    path("contacts/", contacts_page, name="contacts"),
    path("tour/", tour_page, name="tour"),
]