"""Models for Recipes"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """A user"""

    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(20))

    recipes = db.relationship("Recipe", secondary="favorites", back_populates="user")

    def __repr__(self):
        return f"<User name={self.name} email={self.email}>"
    

class Recipe(db.Model):
    """A recipe"""

    __tablename__ = "recipes"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(200), unique=True)
    ingredients = db.Column(db.Text)
    summary = db.Column(db.Text)
    instructions = db.Column(db.Text)
    image_url = db.Column(db.String(200), nullable=True)

    user = db.relationship("User", secondary="favorites", back_populates="recipes")

    def __repr__(self):
        return f"<Recipe title={self.title}, summary={self.summary}, instructions={self.instructions}, ingredients={self.ingredients}>"


class Favorite(db.Model):
    """Users favorite recipe"""

    __tablename__ = "favorites"
    __table_args__ = (db.UniqueConstraint('user_id', 'recipe_id'), )
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    time_created = db.Column(db.DateTime, default=datetime.now, nullable=False)

    def __repr__(self):
        return f"<Favorite id={self.id}, recipe_id={self.recipe_id}, user_id={self.user_id}, time_created={self.time_created}>"


class Review(db.Model):
    """Reviews on a recipe by a user"""

    __tablename__ = "reviews"
    __table_args__ = (db.UniqueConstraint('user_id', 'recipe_id'), )
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    review = db.Column(db.Text)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    time_created = db.Column(db.DateTime, default=datetime.now, nullable=False)

    def __repr__(self):
        return f"<Review id={self.id}, review={self.review[:100]} recipe_id={self.recipe_id}, user_id={self.user_id}, time_created={self.time_created}>"


#A user can have many recipes, one to many. A recipe can have many ingredients, one to many

# user => recipes => ingredients

# db_uri="postgresql:///recipes"
def connect_to_db(flask_app):
    """Connect to database."""

    # flask_app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:5437/recipes"
    # flask_app.config["SQLALCHEMY_ECHO"] = True
    # flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # db.app = flask_app
    db.init_app(flask_app)

    print("DB configured for the Flask app")


# if __name__ == "__main__":
#     from server import app
    
#     connect_to_db(app)
