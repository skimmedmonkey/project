from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from.utils import fetch_monster_data, fetch_monster_info


# Create your views here.

def monster_page_view(request):
    return render(request, 'monsters/monster.html')

def monster_search_view(request):
    monster_search = request.GET.get('search_term','').replace(' ', '-')
    monster_data = fetch_monster_info(monster_search)
    if monster_data:
        return render(request, 'monsters/monster_search.html', {'monster_data': monster_data or None})
    else:
        return render(request, 'monsters/monster_search.html', {'error_message': 'Monster not found'})