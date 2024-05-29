import random

# Ingredient costs dictionary
ingredient_costs = {
    'flour': 2.5,  # per kg
    'sugar': 1.5,  # per kg
    'butter': 3.0,  # per kg
    'milk': 0.8,  # per liter
    'eggs': 0.2,  # per egg
    'baking_powder': 0.02,  # per gram
    'baking_soda': 0.015,  # per gram,
    'vanilla_extract': 20.0,  # per liter,
    'cinnamon': 0.03,  # per gram,
    'raisins': 5.0,  # per kg
    'water': 0.0,  # per liter
    'yeast': 0.05,  # per oz
    'salt': 1  # per kg
}

# Recipe dictionary
dinner_rolls_recipe = {
    'recipe_name': "Dinner Rolls",
    'flour': 1,  # kg
    'water': 0.3,  # liter
    'yeast': 0.02,  # oz
    'salt': 0.01,  # kg
    'butter': 0.1  # kg
}

def calculate_total_cost(recipe, ingredient_costs):
    recipe_name = recipe["recipe_name"]
    total_cost = 0
    for ingredient, amount in recipe.items():
        if ingredient != "recipe_name":
            if ingredient in ingredient_costs:
                ingredient_cost = ingredient_costs[ingredient]
                total_cost += (ingredient_cost * amount)
            else:
                print(f"Cost of {ingredient} not found.")
    print(f"Total cost to make {recipe_name}: ${total_cost:.2f}")
    return total_cost

def change_price(ingredient_costs, ingredient_name, percentage):
    if ingredient_name in ingredient_costs:
        original_price = ingredient_costs[ingredient_name]
        change_amount = original_price * percentage
        new_price = original_price + change_amount
        ingredient_costs[ingredient_name] = new_price
    else:
        print(f"Ingredient {ingredient_name} not found in the cost dictionary.")

def change_all_prices(ingredient_costs, change_percent):
    new_ingredient_costs = ingredient_costs.copy()
    for ingredient in new_ingredient_costs:
        change_price(new_ingredient_costs, ingredient, change_percent)
    return new_ingredient_costs

# Calculate markup and markdown
markup_20 = change_all_prices(ingredient_costs, 0.20)
markdown_20 = change_all_prices(ingredient_costs, -0.20)

# Print updated costs for verification
print("Original ingredient costs:", ingredient_costs)
print("Markup 20% ingredient costs:", markup_20)
print("Markdown 20% ingredient costs:", markdown_20)

# Calculate total costs
original_total_cost = calculate_total_cost(dinner_rolls_recipe, ingredient_costs)
markup_total_cost = calculate_total_cost(dinner_rolls_recipe, markup_20)
markdown_total_cost = calculate_total_cost(dinner_rolls_recipe, markdown_20)

print(f"Original total cost: ${original_total_cost:.2f}")
print(f"Markup 20% total cost: ${markup_total_cost:.2f}")
print(f"Markdown 20% total cost: ${markdown_total_cost:.2f}")

# Generate a random number
a_random_number = random.randint(1, 100)
print(f"A random number: {a_random_number}")
