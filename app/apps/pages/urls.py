from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_page, name="index"),
    path("services/", views.services_page, name="services"),
    path("cases/", views.cases_page, name="cases"),
    path("reviews/", views.reviews_page, name="reviews"),
    path("doctor/", views.doctor_page, name="doctor"),
    path("contacts/", views.contacts_page, name="contacts"),
    path("tour/", views.tour_page, name="tour"),
]