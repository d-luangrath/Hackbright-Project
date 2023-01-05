"""Script to seed database."""
import os
import json

import crud
import model
import server

from utils import get_image_url, get_ingredients_from_recipe
from random import choice, randint
from api_handler import (
    get_recipes_by_ingredients_from_api,
    get_random_recipes_from_api,
)


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


def add_recipes_to_db(recipes) -> None:
    """Add recipes to database"""
    for recipe in recipes:
        ingredients = get_ingredients_from_recipe(recipe)
        image_url = get_image_url(recipe)
       
        print(f"\033[33m█▓▒░ Adding recipe '{recipe['title']}' to DB. \033[0m")
        record = crud.create_recipe(
            recipe["id"],
            recipe["title"],
            recipe["summary"],
            recipe["instructions"],
            ingredients,
            image_url,
        )

        model.db.session.add(record)
    model.db.session.commit()


create_fake_users(user_data)

random_recipes = get_random_recipes_from_api()
add_recipes_to_db(random_recipes)
crud.add_fav_recipe_to_db(1, 665257)

# recipes_by_ingredients = get_recipes_by_ingredients_from_api(
#     endpoint="findByIngredients",
#     payload={"number": 3, "ingredients": "milk"}
# )