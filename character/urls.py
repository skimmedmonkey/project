from django.urls import path
from .views import create_character

urlpatterns = [
    path('character/', create_character, name='character'),
    path('', create_character, name='create_character')
]