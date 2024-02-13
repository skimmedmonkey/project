from django import forms
from .models import DnDCharacter

class CharacterForm(forms.ModelForm):
    
    class Meta:
        model = DnDCharacter
        fields = ['name', 'race', 'class_name', 'alignment', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'armor', 'initiative', 'speed', 'equipment', 'equipment','attacks', 'spells' ]
    
    def __init__(self, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Enter character name'
        self.fields['class_name'].empty_label = 'Bard'
        self.fields['race'].widget.attrs['placeholder'] = 'Human'
        self.fields['alignment'].widget.attrs['placeholder'] = 'True Neutral'    
        self.fields['strength'].widget.attrs['placeholder'] = 'Choose between 1-20'
        self.fields['dexterity'].widget.attrs['placeholder'] = 'Choose between 1-20'
        self.fields['constitution'].widget.attrs['placeholder'] = 'Choose between 1-20'
        self.fields['intelligence'].widget.attrs['placeholder'] = 'Choose between 1-20'
        self.fields['wisdom'].widget.attrs['placeholder'] = 'Choose between 1-20'
        self.fields['charisma'].widget.attrs['placeholder'] = 'Choose between 1-20'
        self.fields['armor'].widget.attrs['placeholder'] = 'Choose between 1-20'
        self.fields['initiative'].widget.attrs['placeholder'] = 'Choose between 1-20'
        self.fields['speed'].widget.attrs['placeholder'] = 'Choose between 1-30'
        self.fields['equipment'].widget.attrs['placeholder'] = 'Example: Shortsword, Rations, 5 GP, Longbow, Lute'
        self.fields['attacks'].widget.attrs['placeholder'] = 'Example: Shortsword: 1d6, Longbow: 1d8'
        self.fields['spells'].widget.attrs['placeholder'] = 'Example: Mage Hand'        