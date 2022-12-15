"""Server for recipes app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.app_context().push()
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(name, email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")
    
    return  redirect("/")

@app.route("/users/<user_id>")
def profile(user_id):
    """Show user profile."""

    pass


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        session["name"] = user.name
        flash(f"Welcome back, {user.name}!")
    
    return redirect("/")
    












if __name__ == "__main__":
    connect_to_db(app)

    app.run(host="0.0.0.0", debug=True)
