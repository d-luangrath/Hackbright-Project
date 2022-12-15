"""Script to seed database."""

import os
import json
from random import choice, randint
import crud
import model
import requests
import server

os.system("dropdb recipes")
os.system("createdb recipes")

model.connect_to_db(server.app)
model.db.create_all()

# Load user data from JSON file
with open("fake_users.json") as f:
    user_data = json.loads(f.read())


# Create users and store them in a list so we can use them
# to create fake accounts
def create_fake_users(user_data):
    users_in_db = []
    for user in user_data:
        name, email, password = (
            user["name"],
            user["email"],
            user["password"]
        )

    db_user = crud.create_user(name, email, password)
    users_in_db.append(db_user)

    model.db.session.add_all(users_in_db)
    model.db.session.commit()


# Create recipes from APIs and store them in a dict
def get_recipes():
    print("Getting recipes using API")
    api_key = os.environ.get("SPOONACULAR_API_KEY", None)
    if not api_key:
        raise Exception("API key is not found. Did you forget to export it?")

    url = f"https://api.spoonacular.com/recipes/random?apiKey={api_key}"
    payload = {'number': 3}

    response = requests.request("GET", url, params=payload)
    recipes = response.json()['recipes']

    return recipes


def add_recipes_to_db():
    recipes = get_recipes()

    for recipe in recipes:
        print(f"\033[33m█▓▒░ Adding recipe '{recipe['title']}' to DB. \033[0m")
        record = crud.create_recipe(
            recipe["title"],
            recipe["summary"],
            recipe["instructions"]
        )
        breakpoint()
    
    model.db.session.add(record)
    model.db.session.commit()

create_fake_users(user_data)
add_recipes_to_db()