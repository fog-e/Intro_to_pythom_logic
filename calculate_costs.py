# Ingredient costs dictionary
ingredient_costs = {
    "flour": 2.5,  # per kg
    "sugar": 1.5,  # per kg
    "butter": 3.0,  # per kg
    "water": 0.01,  # per liter
    "salt": 1,  # per kg
    "yeast": 0.05,  # per oz
    "eggs": 0.2,  # per egg
    "milk": 0.8,  # per liter
    "chocolate_chips": 4.0,  # per kg
    "vanilla_extract": 20,  # per liter
    "baking_powder": 0.02,  # per gram
    "baking_soda": 0.015,  # per gram
    "cinnamon": 0.03,  # per gram
    "raisins": 5.0  # per kg
}

# Recipe dictionary
dinner_rolls_recipe = {
    "recipe_name": "Dinner Rolls",
    "flour": 1,  # kg
    "water": 0.3,  # liter
    "yeast": 0.02,  # oz
    "salt": 0.01,  # kg
    "butter": 0.1  # kg
}

# Function to calculate the total cost of a recipe
def calculate_recipe_cost(ingredients):
    total_cost = 0
    for ingredient, amount in ingredients.items():
        # Ignore the recipe_name key
        if ingredient == "recipe_name":
            continue
        # Get the cost per unit of the ingredient
        cost_per_unit = ingredient_costs.get(ingredient, 0)
        # Calculate the cost for the ingredient and add it to the total cost
        total_cost += cost_per_unit * amount
    return total_cost

# Calculate the cost for the dinner rolls recipe
dinner_rolls_cost = calculate_recipe_cost(dinner_rolls_recipe)
print(f"Total cost to make {dinner_rolls_recipe['recipe_name']}: ${dinner_rolls_cost:.2f}")

# Ingredient costs dictionary
ingredient_costs = {
    "flour": 2.5,  # per kg
    "sugar": 1.5,  # per kg
    "butter": 3.0,  # per kg
    "water": 0.01,  # per liter
    "salt": 1,  # per kg
    "yeast": 0.05,  # per oz
    "eggs": 0.2,  # per egg
    "milk": 0.8,  # per liter
    "chocolate_chips": 4.0,  # per kg
    "vanilla_extract": 20,  # per liter
    "baking_powder": 0.02,  # per gram
    "baking_soda": 0.015,  # per gram
    "cinnamon": 0.03,  # per gram
    "raisins": 5.0  # per kg
}

# Recipe dictionary
dinner_rolls_recipe = {
    "recipe_name": "Dinner Rolls",
    "flour": 1,  # kg
    "water": 0.3,  # liter
    "yeast": 0.02,  # oz
    "salt": 0.01,  # kg
    "butter": 0.1  # kg
}

# Function to calculate the total cost
def calculate_total_cost(recipe):
    recipe_name = recipe["recipe_name"]
    total_cost = 0

    for ingredient, amount in recipe.items():
        if ingredient != "recipe_name":
            ingredient_cost = ingredient_costs.get(ingredient, 0)
            total_cost += ingredient_cost * amount

    print(f"Total cost to make {recipe_name}: ${total_cost:.2f}")
    return total_cost

# Calculate the cost for dinner rolls
calculate_total_cost(dinner_rolls_recipe)