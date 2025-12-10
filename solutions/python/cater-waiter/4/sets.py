"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)

def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))

def check_drinks(drink_name, drink_ingredients):
    tail = "Cocktail"
    if set(drink_ingredients).isdisjoint(ALCOHOLS):
        tail = "Mocktail"

    return drink_name + " " + tail

def categorize_dish(dish_name, dish_ingredients):
    
    type = ""
    if set(dish_ingredients) <= VEGAN:
        type = "VEGAN"
    elif set(dish_ingredients) <= VEGETARIAN:
        type = "VEGETARIAN"
    elif set(dish_ingredients) <= PALEO:
        type = "PALEO"
    elif set(dish_ingredients) <= KETO:
        type = "KETO"
    elif set(dish_ingredients) <= OMNIVORE:
        type = "OMNIVORE"

    return dish_name +  ": " + type

def tag_special_ingredients(dish):
    other = set(dish[1]) - SPECIAL_INGREDIENTS

    return (dish[0], set(dish[1]) - other)
    
def compile_ingredients(dishes):
    ingredients = set()
    for dish in dishes:
        ingredients = ingredients | dish

    return ingredients

def separate_appetizers(dishes, appetizers):
    return list(set(dishes) - set(appetizers))

def singleton_ingredients(dishes, intersection):
    ingradient = set()
    for dish in dishes :
        ingradient = ingradient | dish

    return ingradient - intersection