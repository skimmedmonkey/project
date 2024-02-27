from django.urls import path
from .views import CompareNamesDatesView

urlpatterns = [
    path('compare/', CompareNamesDatesView.as_view(), name='compare'),
]