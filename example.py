def change_price(ingredient_cost, ingredient_name, percentage):
    """
    Change the price of a given ingredient by a specified percentage.

    Args:
        ingredient_cost (dict): A dictionary of ingredient names and their costs.
        ingredient_name (str): The name of the ingredient to change the price for.
        percentage (float): The percentage to change the price by (e.g., 0.20 for +20% or -0.20 for -20%).

    Returns:
        None
    """
    # Find the right place in the dictionary (ingredient_name)
    if ingredient_name in ingredient_cost:
        original_price = ingredient_cost[ingredient_name]
        
        # Add or subtract the percentage
        change_amount = original_price * percentage
        new_price = original_price + change_amount
        
        # Set the new details in the dictionary
        ingredient_cost[ingredient_name] = new_price
        
        print(f"Changed {ingredient_name} price from ${original_price:.2f} to ${new_price:.2f} ({percentage*100:.1f}%)")
    else:
        print(f"Ingredient {ingredient_name} not found in the cost dictionary.")

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

# Change the price of salt by +10%
change_price(ingredient_costs, 'salt', 0.10)

# Change the price of butter by -5%
change_price(ingredient_costs, 'butter', -0.05)

# Change the price of vanilla_syrup by +15%
change_price(ingredient_costs, 'vanilla_syrup', 0.15)
