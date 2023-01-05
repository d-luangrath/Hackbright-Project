def get_ingredients_from_recipe(recipe):
    """Extract ingredients element from recipe"""
    ingr_html_str = ""
    for ingredient in recipe["extendedIngredients"]:
        ingr_html_str += ingredient["original"] + "<br>"
    return ingr_html_str


def get_image_url(recipe):
    """Extract image URL element from recipe"""

    image_url = None
    if recipe.get("image"):
        image_url = recipe["image"]
    return image_url
    