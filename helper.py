from os import environ
import requests

def get_ingredients(ingredients):
    api_key = environ.get("SPOONACULAR_API_KEY", None)
    # print(api_key)
    if not api_key:
        raise Exception("API key is not found. Did you forget to export it?")

    url = f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={api_key}"
    # print(url)
    payload = {'number': 3, 'ingredients': ingredients}
    response = requests.request("GET", url, params=payload)
    recipes = response.json()

    for recipe in recipes:
        print(recipe['title'])
    
    return recipes