from os import environ
import requests
import crud

def get_random_recipes_from_api():
    """Create recipes from APIs and store them in a dict"""
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


def get_recipes_by_id(id):
    """Get recipes by ID"""
    api_key = environ.get("SPOONACULAR_API_KEY", None)
    if not api_key:
        raise Exception("API key is not found. Did you forget to export it?")

    url = f"https://api.spoonacular.com/recipes/{id}/information?apiKey={api_key}"
    response = requests.request("GET", url)
    recipes = response.json()
    
    return recipes


# def get_rec_info_by_search(ingredients):
#     """Get recipe information from search query"""
#     recipes = get_recipes_by_ingredients()
    
#     for recipe in recipes: 
#         ingr_search_res = recipe["title"]
#         print(ingr_search_res)


 