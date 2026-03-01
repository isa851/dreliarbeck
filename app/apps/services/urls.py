from django.urls import path
from . import views

urlpatterns = [
    path('services', views.services_page, name='services'),
]