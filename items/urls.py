from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.item_search, name='item_search'),
]