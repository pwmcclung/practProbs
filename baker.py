import math
def get_missing_ingredients(recipe, added):
    missing = {}
    if not added:
        return recipe
    
    max_cakes = 1
    
    for ingredient, amount_needed in recipe.items():
        if ingredient in added and added[ingredient] > 0:
            num_cakes = math.ceil(added[ingredient] / amount_needed)
            if num_cakes > max_cakes:
                max_cakes = num_cakes

    
    for ingredient, amount_needed in recipe.items():
        if ingredient in added:
            missing_amount = (max_cakes * amount_needed) - added[ingredient]
            if missing_amount > 0:
                missing[ingredient] = missing_amount
        else:
            missing[ingredient] = amount_needed * max_cakes

    return missing