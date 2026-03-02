from django.urls import path
from .views import tur_view

urlpatterns = [
    path('tour/', tur_view, name='tour'),
]