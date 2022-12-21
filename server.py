"""Server for recipes app."""
from helper import  get_ingredients
from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
from random import choice

app = Flask(__name__)
app.app_context().push()
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""
    return render_template("homepage.html")


@app.route("/signup")
def create_acct():
    """View create an account for user."""
    return render_template("create_acct.html")


@app.route("/signup", methods=["POST"])
def register_user():
    """Create a new user."""
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
    """Process user login."""
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
    """Display contents on the main page."""
    return render_template("mainpage.html")


@app.route("/profile/<user_id>")
def profile(user_id):
    """Show user profile."""
    user_id = session["user_id"]
    user = crud.get_user_by_id(user_id)
    return render_template("profile.html", user=user)


# @app.route("/profile/<user_id>")
# def greet_person(user_id):
#     """Return customized greet pun along with person name."""

    # greetings = ["smart", "clever", "tenacious", "awesome", "Pythonic"]
    # person = request.args.get("name")
    # greet_pun = choice(greetings)
    # return render_template("profile.html", user=user,
    #                        name=person,
    #                        greetings=greet_pun)


@app.route("/recipes")
def all_recipes():
    """View all recipes."""
    recipes = crud.get_all_recipes()
    return render_template("all_recipes.html", recipes=recipes)


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    """View a specific recipe."""
    recipe = crud.get_recipe_by_id(recipe_id)
    return render_template("recipe_details.html", recipe=recipe)


@app.route('/rec-by-ingre')
def recipe_by_ingredient():

    ingredients = request.args.get("ingredients")
    recipes = get_ingredients(ingredients)
    return jsonify(recipes)



if __name__ == "__main__":
    connect_to_db(app)

    app.run(host="0.0.0.0", debug=True)
