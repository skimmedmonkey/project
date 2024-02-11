from django.shortcuts import render
from .utils import fetch_item_info

# Create your views here.
def item_search(request):
    item_search = request.GET.get('search_term','').replace(' ', '-')
    item_data = fetch_item_info(item_search)
    if item_data:
        return render(request, 'items/item_search.html', {'item_data': item_data or None})
    else:
        return render(request, 'items/item_search.html', {'error_message': 'Item not found'})

