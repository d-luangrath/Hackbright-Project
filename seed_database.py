"""Script to seed database."""
import os
import json

import crud
import model
from server import app

from crud import add_recipes_to_db, add_review_to_db
from random import choice, randint
from api_handler import get_random_recipes_from_api

model.connect_to_db(app)
with app.app_context():
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

create_fake_users(user_data)

random_recipes = get_random_recipes_from_api()
add_recipes_to_db(random_recipes)
crud.add_fav_recipe_to_db(1, 665257)
crud.add_review_to_db(1, 665257)
