from django.urls import path
from .views import CompareDates

urlpatterns = [
    path('compare/', CompareDates.as_view()),
]