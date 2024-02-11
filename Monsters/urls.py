from django.urls import path
from .views import monster_search_view, monster_page_view

urlpatterns = [
    path('monster_search/', monster_search_view, name='monster_search'),
    path('', monster_page_view, name='monster_page_view')
]  