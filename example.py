def change_price(ingredient_costs, ingredient_name, percentage):
    """
    Change the price of a given ingredient by a specified percentage.

    Args:
        ingredient_costs (dict): A dictionary of ingredient names and their costs.
        ingredient_name (str): The name of the ingredient to change the price for.
        percentage (float): The percentage to change the price by (e.g., 0.20 for +20% or -0.20 for -20%).

    Returns:
        dict: The updated ingredient costs dictionary.
    """
    ## find ingredient_name in the dictionary
    if ingredient_name in ingredient_costs:
        ## add or subtract the percentage
        ingredient_costs[ingredient_name] = ingredient_costs[ingredient_name] * (1 + percentage)
    else:
        print(f"Ingredient {ingredient_name} not found in the cost dictionary.")
    
    ## set the new details in the dictionary
    return ingredient_costs

# Example usage
ingredient_costs = {
    'flour': 2.5,  # per kg
    'sugar': 1.5,  # per kg
    'butter': 3.0,  # per kg
    'milk': 0.8,  # per liter
    'eggs': 0.2,  # per egg
    'yeast': 0.05,  # per oz
    'chocolate_chips': 4.0,  # per kg
    'vanilla_extract': 20.0,  # per liter
    'baking_powder': 0.02,  # per gram
    'baking_soda': 0.015,  # per gram
    'cinnamon': 0.03,  # per gram
    'raisins': 5.0,  # per kg
    'salt': 1.0,  # per kg
    'vanilla_syrup': 15.0  # per liter (added vanilla_syrup)
}

# Change the price of chocolate chips by +20%
print(change_price(ingredient_costs, 'chocolate_chips', 0.20))

# Change the price of salt by +10%
print(change_price(ingredient_costs, 'salt', 0.10))

# Change the price of butter by -5%
print(change_price(ingredient_costs, 'butter', -0.05))

# Try changing the price of an ingredient that doesn't exist
print(change_price(ingredient_costs, 'vanilla_syrup', 0.15))
