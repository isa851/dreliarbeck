from django.urls import path
from apps.cases.views import cases_page


urlpatterns = [
    path('cases/', cases_page, name='cases'),
]