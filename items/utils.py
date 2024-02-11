import requests


def fetch_item_info(item_name):
    url = f"https://www.dnd5eapi.co/api/item/{item_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return "Item not found with that name. Please try again"