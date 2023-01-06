def get_ingredients_from_recipe(recipe: dict) -> str:
    """Extract ingredients element from recipe"""
    ingr_html_str = ""
    print(f"\033[35m█▓▒░ {__name__} | {recipe = } \033[0m")
    if recipe.get("extendedIngredients"):  # means recipe came from random
        for ingredient in recipe["extendedIngredients"]:
            ingr_html_str += ingredient["original"] + "<br>"
    else:  # mean recipe came from search
        for ingredient in recipe["missedIngredients"]:
            ingr_html_str += ingredient["original"] + "<br>"
        for ingredient in recipe["usedIngredients"]:
            ingr_html_str += ingredient["original"] + "<br>"

    return ingr_html_str


def get_image_url(recipe):
    """Extract image URL element from recipe"""

    image_url = None
    if recipe.get("image"):
        image_url = recipe["image"]
    return image_url
    

# def add_recipes_to_db(recipes) -> None:
#     """Add recipes to database"""
#     for recipe in recipes:
#         ingredients = get_ingredients_from_recipe(recipe)
#         image_url = get_image_url(recipe)
       
#         print(f"\033[33m█▓▒░ Adding recipe '{recipe['title']}' to DB. \033[0m")
#         record = crud.create_recipe(
#             recipe["id"],
#             recipe["title"],
#             recipe["summary"],
#             recipe["instructions"],
#             ingredients,
#             image_url,
#         )

#         model.db.session.add(record)
#     model.db.session.commit()