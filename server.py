"""Server for recipes app."""
from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined
from api_handler import (
    get_recipes_by_ingredients_from_api, 
    get_recipe_by_id_from_api, 
    get_random_recipes_from_api,
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
   
    session["user_id"] = user.id
    session["name"] = user.name
    session["email"] = user.email
    flash(f"Welcome back, {user.name.title()}!")
    return redirect("/mainpage")
    

@app.route("/mainpage")
def mainpage():
    """Display contents on the main page"""
    return render_template("mainpage.html")


@app.route("/profile/")
def profile():
    """Show user profile"""
    id = session["user_id"]
    print(f"\033[36m█▓▒░ {__name__} | {id =} \033[0m")
    user = crud.get_user_by_id(id)
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


# @app.route("/recipe/<id>")
# def recipe(id):
#     """View a specific recipe from random api"""
#     recipe = crud.get_recipe_by_id(id)
#     if not recipe:
#         return render_template("recipe_not_found.html")
#     return render_template("recipe_details.html", recipe=recipe)


@app.route("/recipe/<id>")
def recipe_from_search_api(id):
    """View specific recipe from the search by ingredients api"""
    recipe_from_db = crud.get_recipe_by_id(id)  # check if recipe is in DB
    
    # if it was not found in DB (recipe == None), try to get recipe from API
    # and save to DB so we can reuse it later and save an API call
    if not recipe_from_db:
        recipe_from_api = get_recipe_by_id_from_api(id)
        crud.add_recipes_to_db([recipe_from_api])

    recipe_from_db = crud.get_recipe_by_id(id)  # check again if recipe is in DB cuz we just saved it to db

    return render_template("recipe_details.html", recipe=recipe_from_db)


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



if __name__ == "__main__":
    connect_to_db(app)

    app.run(host="0.0.0.0", debug=True)
