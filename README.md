# Heart Beet

Heart Beet is a fullstack web development application that allows a user to search recipes by an ingredient.
A user will log in and/or create an account to access the features to favorite and write a review for a recipe.
When a user clicks on the recipe name, they are directed to the recipe information page, which displays the recipe
image, summary, ingredients, and instructions. Below that, there is an option for a user to write a review. 
A user's favorited and reviewed recipes are saved and displayed onto their favorite and reviews page, so they can go
back to referencing recipes they want to revisit. 

## Technologies
- Python 3
- Flask
- PostgreSQL
- SQLAlchemy
- Javascript
- Jinja 2
- Bootstrap
- CSS/ HTML
- Spoonacular API

## Features
Heart Beet's feature includes searching a recipe by ingredient, favoriting a recipe, and writing a review for a recipe.
Using Sponacular's API for searching a recipe by an ingredient, recipes are displayed to the user along with a 'favorite' button
on the card. The recipes are not yet saved to the database when the API request is made, so once the user clicks on 'favorite,'
a record of a recipe is added the database. If a user decides that they do not like that recipe anymore, they can simply click the button'unfavorite' which will delete the record of the recipe in the database. When the user reviews a recipe, it is saved to the database and displayed on the reviews page. Users can update their reviews by writing a review on the same recipe.

## How to use
1. **Login or create an account**

![Login page](/static/img/login.png)

2. **Type in the ingredient you want to make a recipe with**

![Search form](/static/img/search%20form.png)

3. **Review "Your Favorites" to see all of your favorite recipes**

![Your favorites](/static/img/favorites.png)

4. **Write a review for a recipe in the text box on the bottom of the recipe's page. A user can update their reviewed recipes by simply writing a new review on that recipe**

![Write review](/static/img/review-bg.jpg)

5. **A user can look at all of their reviews on "Your Reviews" page.**

![Your reviews](/static/img/review%20submission.png)