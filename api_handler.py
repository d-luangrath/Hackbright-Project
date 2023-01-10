from os import environ
import requests

def get_random_recipes_from_api():
    """Create random recipes from APIs and store them in a dictionary"""
    print("\033[36m█▓▒░ Getting recipes using API \033[0m")
    api_key = environ.get("SPOONACULAR_API_KEY", None)
    if not api_key:
        raise Exception("API key is not found. Did you forget to 'source secrets.sh'?")

    url = f"https://api.spoonacular.com/recipes/random?apiKey={api_key}"
    payload = {'number': 3}

    response = requests.request("GET", url, params=payload)
    recipes = response.json()['recipes']

    return recipes


def get_recipes_by_ingredients_from_api(endpoint: str, payload: dict):
    """Search recipes by ingredients"""
    api_key = environ.get("SPOONACULAR_API_KEY", None)
    if not api_key:
        raise Exception("API key is not found. Did you forget to export it?")

    url = f"https://api.spoonacular.com/recipes/{endpoint}?apiKey={api_key}"
    response = requests.request("GET", url, params=payload)
    recipes = response.json()
    
    return recipes


def get_recipe_by_id_from_api(id):
    """Get recipe by ID"""
    api_key = environ.get("SPOONACULAR_API_KEY", None)
    if not api_key:
        raise Exception("API key is not found. Did you forget to export it?")

    url = f"https://api.spoonacular.com/recipes/{id}/information?apiKey={api_key}"
    response = requests.request("GET", url)
    recipe = response.json()
    
    return recipe



 