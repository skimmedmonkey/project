from django.shortcuts import render, redirect
from .forms import CharacterForm
# Create your views here.
def create_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('character')
    else:
        form = CharacterForm()
    return render(request, 'character/create_character.html', {'form': form})