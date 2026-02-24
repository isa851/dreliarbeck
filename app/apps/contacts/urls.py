from django.urls import path
from .views import booking_submit

urlpatterns = [
    path("booking/submit/", booking_submit, name="booking_submit"),
]