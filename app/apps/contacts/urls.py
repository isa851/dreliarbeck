from django.urls import path
from .views import contacts_page, booking_api

urlpatterns = [
    path("contacts/", contacts_page, name="contacts"),
    path("api/booking/", booking_api, name="booking_api"),
]