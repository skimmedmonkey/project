import requests

def fetch_monster_data():
    url = "https://www.dnd5eapi.co/api/monsters"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["count"]
    else:
        return None
    
def fetch_monster_info(monster_name):
    url = f"https://www.dnd5eapi.co/api/monsters/{monster_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return "Monster not found with that name. Please try again"