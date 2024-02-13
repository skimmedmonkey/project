from django.shortcuts import render, redirect
from .forms import CharacterForm
from .models import DnDCharacter
# Create your views here.
def create_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            saved_form = form.save()
            return redirect('character_sheet_detail', pk=saved_form.pk)
    else:
        form = CharacterForm()
    return render(request, 'character/create_character.html', {'form': form})

def character_sheet_detail(request, pk):
    character_sheet = DnDCharacter.objects.get(pk=pk)
    return render(request, 'character/character_sheet.html', {'character_sheet': character_sheet})