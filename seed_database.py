"""Script to seed database."""
from helper import get_recipes_by_ingredients
import os
import json
from random import choice, randint
import crud
import model
import requests
import server


model.connect_to_db(server.app)
model.db.create_all()

with open("fake_users.json") as f:
    """Load user data from JSON file"""
    user_data = json.loads(f.read())


def create_fake_users(user_data):
    """Create users and store them in a list so we can use them
    to create fake accounts"""
    users_in_db = []
    for user in user_data:
        name, email, password = (
            user["name"],
            user["email"],
            user["password"],
        )

        db_user = crud.create_user(name, email, password)
        users_in_db.append(db_user)

    model.db.session.add_all(users_in_db)
    model.db.session.commit()


def get_recipes_from_api():
    """Create recipes from APIs and store them in a dict"""
    print("\033[36m█▓▒░ Getting recipes using API \033[0m")
    api_key = os.environ.get("SPOONACULAR_API_KEY", None)
    if not api_key:
        raise Exception("API key is not found. Did you forget to 'source secrets.sh'?")

    url = f"https://api.spoonacular.com/recipes/random?apiKey={api_key}"
    payload = {'number': 3}

    response = requests.request("GET", url, params=payload)
    recipes = response.json()['recipes']

    return recipes


def add_recipes_to_db(recipes):
    for recipe in recipes:
        ingredients = get_ingredients_from_recipe(recipe)
        image_url = get_image_url(recipe)
       
        print(f"\033[33m█▓▒░ Adding recipe '{recipe['title']}' to DB. \033[0m")
        record = crud.create_recipe(
            recipe["title"],
            recipe["summary"],
            recipe["instructions"],
            ingredients,
            image_url
        )

        model.db.session.add(record)
    model.db.session.commit()


def get_ingredients_from_recipe(recipe):
    ingr_html_str = ""
    for ingredient in recipe["extendedIngredients"]:
        ingr_html_str += ingredient["original"] + "<br>"
    return ingr_html_str


def get_image_url(recipe):
    image_url = None
    if recipe.get("image"):
        image_url = recipe["image"]
    return image_url
    

create_fake_users(user_data)
recipes = get_recipes_from_api()
add_recipes_to_db(recipes)