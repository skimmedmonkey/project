from django import forms
from .models import DnDCharacter

class CharacterForm(forms.ModelForm):
    
    class Meta:
        model = DnDCharacter
        fields = ['name', 'race', 'class_name', 'alignment', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'armor', 'initiative', 'speed', 'equipment', 'equipment','attacks', 'spells' ]
    
    def __init__(self, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Enter character name'
        self.fields['class_type'].widget.attrs['placeholder'] = 'Bard'
        self.fields['race'].widget.attrs['placeholder'] = 'Human'
        self.fields['alignment'].widget.attrs['placeholder'] = 'True Neutral'    
        self.fields['strength'].widget.attrs['placeholder'] = '15'
        self.fields['dexterity'].widget.attrs['placeholder'] = '12'
        self.fields['constitution'].widget.attrs['placeholder'] = '14'
        self.fields['intelligence'].widget.attrs['placeholder'] = '10'
        self.fields['wisdom'].widget.attrs['placeholder'] = '8'
        self.fields['charisma'].widget.attrs['placeholder'] = '16'
        self.fields['armor'].widget.attrs['placeholder'] = '14'
        self.fields['initiative'].widget.attrs['placeholder'] = '12'
        self.fields['speed'].widget.attrs['placeholder'] = '20'
        self.fields['equipment'].widget.attrs['placeholder'] = 'Shortsword, Rations, 5 GP, Longbow, Lute'
        self.fields['attacks'].widget.attrs['placeholder'] = 'Shortsword: 1d6, Longbow: 1d8'
        self.fields['spells'].widget.attrs['placeholder'] = 'Mage Hand'        