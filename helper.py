from os import environ
import requests

def get_recipes_by_ingredients(ingredients):
    """Search recipes by ingredients"""
    api_key = environ.get("SPOONACULAR_API_KEY", None)
    if not api_key:
        raise Exception("API key is not found. Did you forget to export it?")

    url = f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={api_key}"
    payload = {'number': 3, 'ingredients': ingredients}
    response = requests.request("GET", url, params=payload)
    recipes = response.json()
    
    return recipes