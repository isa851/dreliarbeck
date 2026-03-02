from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_page, name="index"),
    path("reviews/", views.reviews_page, name="reviews"),
    path("results/", views.results_page, name="results"),
    path("doctor/", views.doctor_page, name="doctor"),
    path("api/chat-booking/", views.chat_booking_api, name="chat_booking_api"),
]
