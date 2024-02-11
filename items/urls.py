from django.urls import path
from .views import item_search

urlpatterns = [
    path('search/', item_search, name='item_search'),
]