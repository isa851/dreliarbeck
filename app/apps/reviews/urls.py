from django.urls import path
from apps.reviews.views import review_page

urlpatterns = [
    path('review/', review_page, name='review'),
]