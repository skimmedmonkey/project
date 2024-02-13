from django import forms
from .models import DnDCharacter

class CharacterForm(forms.ModelForm):
    
    class Meta:
        model = DnDCharacter
        fields = ['name', 'race', 'class_name', 'alignment', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'armor', 'initiative', 'speed', 'equipment', 'equipment','attacks', 'spells' ]