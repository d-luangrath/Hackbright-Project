"""Models for Recipes"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(20))

    recipes = db.relationship("Recipe", back_populates="user")

    def __repr__(self):
        return f"<User name={self.name} email={self.email}>"
    

class Recipe(db.Model):
    """A recipe."""

    __tablename__ = "recipes"

    recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    recipe_name = db.Column(db.String(200), unique=True)
    rec_ingredient = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text)
    direction = db.Column(db.Text)

    user = db.relationship("User", back_populates="recipes")
    # ingredients = db.relationship("Ingredient", back_populates="recipes")

    def __repr__(self):
        return f"<Recipe recipe_name={self.recipe_name}, description={self.description}, direction={self.direction}, ingredient={self.rec_ingredient}>"


class Ingredient(db.Model):
    """Individual ingredient."""

    __tablename__ = "ingredients"

    ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"))
    ingredient_name = db.Column(db.String(50))
    details = db.Column(db.String(100))
    amount = db.Column(db.Integer)
    measurement = db.Column(db.Integer)

    # recipes = db.relationship("Recipe", back_populates="ingredients")

    def __repr__(self):
        return f"<ingredient_name={self.ingredient_name}, details={self.details}, amount={self.amount}, measurement={self.measurement}>"


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
