from django.urls import path
from .views import create_character, character_sheet_detail

urlpatterns = [
    path('character/', create_character, name='create_character'),
    path('character-sheet/<int:pk>/', character_sheet_detail, name='character_sheet_detail'),
]