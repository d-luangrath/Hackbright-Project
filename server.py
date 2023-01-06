"""Server for recipes app."""
from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined
from api_handler import (
    get_recipes_by_ingredients_from_api, 
    get_recipe_by_id_from_api, 
    get_random_recipes_from_api
)

app = Flask(__name__)
app.app_context().push()
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage"""
    return render_template("homepage.html")


@app.route("/signup")
def create_acct():
    """View create an account for user"""
    return render_template("create_acct.html")


@app.route("/signup", methods=["POST"])
def register_user():
    """Create a new user"""
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)
    if user:
        flash("An account with that email already exists. Try again.")
    else:
        user = crud.create_user(name, email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")
    return redirect("/")


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login"""
    email = request.form.get("login-email")
    password = request.form.get("login-pass")
    # check if fields are not empty
    if not email or not password:
        flash("Please input required fields.")
        return redirect("/")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
        return redirect("/")
   
    session["user_id"] = user.user_id
    session["name"] = user.name
    session["user_email"] = user.email
    flash(f"Welcome back, {user.name.title()}!")
    return redirect("/mainpage")
    

@app.route("/mainpage")
def mainpage():
    """Display contents on the main page"""
    return render_template("mainpage.html")


@app.route("/profile/<user_id>")
def profile(user_id):
    """Show user profile"""
    user_id = session["user_id"]
    user = crud.get_user_by_id(user_id)
    return render_template("profile.html", user=user)


@app.route("/logout")
def logout():
    """Log out of user account"""
    flash("Successfully logged out.")
    return redirect("/")


@app.route("/recipes")
def all_recipes():
    """View all random recipes"""
    recipes = crud.get_all_recipes()
    if not recipes:
        return render_template("recipe_not_found.html")
    return render_template("all_recipes.html", recipes=recipes)


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    """View a specific recipe from random api"""
    recipe = crud.get_recipe_by_id(recipe_id)
    if not recipe:
        return render_template("recipe_not_found.html")
    return render_template("recipe_details.html", recipe=recipe)


# @app.route("/recipe/<recipe_id>")
# def recipe(recipe_id):
#     """View a specific recipe from random api"""
#     recipe = crud.get_recipe_by_id(recipe_id)
#     if not recipe:
#         recipe = request.args.get("data")
    
#     if not recipe:
#         # error message

#     # if not recipe:
#     #     return render_template("recipe_not_found.html")
#     return render_template("recipe_details.html", recipe=recipe)

### EXTRACT RECIPE INFO FROM API TO DISPLAY ONTO WEB PAGE -from crud create_recipe
# @app.route("/recipe/<recipe_id>")
# def recipe_from_api_by_id(recipe_id):
#     recipe = get_recipe_by_id_from_api(recipe_id)
#     print(f"\033[32m█▓▒░ {__name__} | {recipe =} \033[0m")
#     # import seed_database
#     # recipe["title"],
#     # recipe["summary"],
#     # recipe["instructions"],


    return render_template("recipe_details.html", recipe=recipe)


@app.route('/rec-by-ingre')
def recipe_by_ingredient():
    """Display recipes title from search query"""
    ingredients = request.args.get("ingredients")
    print(f"\033[36m█▓▒░ {__name__} | {ingredients=} \033[0m")
    recipes = get_recipes_by_ingredients_from_api(
        endpoint="findByIngredients",
        payload={"number": 3, "ingredients": ingredients},
    )

    recipe_names = []
    print(f"\033[36m█▓▒░ {__name__} | {recipes = } \033[0m")
    for recipe in recipes:  
        recipe_names.append(
            {"name": recipe["title"], "id": recipe["id"]}
        )

    print(f"\033[36m█▓▒░ {__name__} | {recipe_names=} \033[0m")
    return jsonify(recipe_names)


@app.route('/favorite/<recipe_id>')
def add_recipe_to_favorites(recipe_id):
    """Add recipe to user's favorites"""
    user_id = session["user_id"]

    result = crud.add_fav_recipe_to_db(user_id, recipe_id)

    if result == "Success":
        return jsonify(
            {
                "status": result,
                "msg": f"Added recipe '{recipe_id}' to user's '{user_id}' favorites",
            }
        )
    else:
        return jsonify(
            {
                "status": result,
                "msg": "Something went wrong",
            }
        )


def func():
    """Display favorites onto profile page, under favorite recipes"""


if __name__ == "__main__":
    connect_to_db(app)

    app.run(host="0.0.0.0", debug=True)
