from model import db, User, Recipe, connect_to_db, Favorite
from api_handler import get_recipe_by_id_from_api
from utils import get_image_url, get_ingredients_from_recipe
from sqlalchemy.exc import IntegrityError

def create_user(name, email, password):
    """Create and return a new user"""
    user = User(name=name, email=email, password=password)
    return user


def get_user():
    """Return all users"""
    return User.query.all()


def get_user_by_id(id):
    """Return a user by primary key"""
    return User.query.get(id)


def get_user_by_email(email):
    """Return a user by email"""
    return User.query.filter(User.email == email).first()


def get_user_by_name(name):
    """Return a user by name"""
    return User.query.filter(User.name == name).first()


def create_recipe(id, title, summary, instructions, ingredients, image_url):
    """Create and return a new recipe"""
    recipe = Recipe(
        id=id,
        title=title,
        summary=summary,
        instructions=instructions,
        ingredients=ingredients,
        image_url=image_url,
    )

    return recipe


def add_fav_recipe_to_db(user_id, recipe_id):
    """Add user favorite recipe to database"""
    if not Recipe.query.get(recipe_id):
        print(f"\033[35m█▓▒░ {__name__} | {recipe_id} is not found in DB. Creating a new record... \033[0m")
        recipe = get_recipe_by_id_from_api(recipe_id)
        ingredients = get_ingredients_from_recipe(recipe)
        image_url = get_image_url(recipe)
       
        record = create_recipe(
            recipe_id,
            recipe["title"],
            recipe["summary"],
            recipe["instructions"],
            ingredients,
            image_url,
        )
        print(f"\033[36m█▓▒░ {__name__} | Created recipe - {record = } \033[0m")
        db.session.add(record)
        db.session.commit()
    
    # add this recipe to user favorites - create a record in table Favorites
    favorite_record = Favorite(recipe_id=recipe_id, user_id=user_id)
    print(f"\033[32m█▓▒░ {__name__} | {favorite_record =} \033[0m")
    db.session.add(favorite_record)
    try:
        db.session.commit()
    except IntegrityError as e:
        print(f"\033[31m█▓▒░ {__name__} | Exception was caught - {e.orig} \033[0m")
        return "Fail"
    return "Success"


def get_all_recipes():
    """Return all recipes"""
    return Recipe.query.all()


def get_recipe_by_title(title):
    """Return all recipe by title"""
    return Recipe.query.filter(Recipe.title).all()


def get_recipe_by_id(id):
    """Return a recipe by primary key"""
    return Recipe.query.get(id)


def get_recipe_by_instructions(instructions):
    """Return all recipes by instructions"""
    return Recipe.query.get(instructions)



if __name__ == "__main__":
    from server import app

    connect_to_db(app)