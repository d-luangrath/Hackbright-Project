"""Models for Recipes"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """A user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(20))

    recipes = db.relationship("Recipe", secondary="favorites", back_populates="user")

    def __repr__(self):
        return f"<User name={self.name} email={self.email}>"
    

class Recipe(db.Model):
    """A recipe"""

    __tablename__ = "recipes"

    recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    recipe_name = db.Column(db.String(200), unique=True)
    ingredients = db.Column(db.Text)
    description = db.Column(db.Text)
    direction = db.Column(db.Text)
    image_url = db.Column(db.String(200), nullable=True)

    user = db.relationship("User", secondary="favorites", back_populates="recipes")

    def __repr__(self):
        return f"<Recipe recipe_name={self.recipe_name}, description={self.description}, direction={self.direction}, ingredients={self.ingredients}>"


class Favorite(db.Model):
    """Users favorite recipe"""

    __tablename__ = "favorites"
    __table_args__ = (db.UniqueConstraint('user_id', 'recipe_id'), )
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    time_created = db.Column(db.DateTime, default=datetime.now, nullable=False)

    def __repr__(self):
        return f"<Favorite id={self.id}, recipe_id={self.recipe_id}, user_id={self.user_id}, time_created={self.time_created}>"

#A user can have many recipes, one to many. A recipe can have many ingredients, one to many

# user => recipes => ingredients


def connect_to_db(flask_app, db_uri="postgresql:///recipes"):
    """Connect to database."""

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = True
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    
    connect_to_db(app)
