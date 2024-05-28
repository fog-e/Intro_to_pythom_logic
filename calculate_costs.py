import random

def calculate_unit_cost(recipe, ingredient_costs):
    total_cost = 0
    for ingredient, amount in recipe.items():
        if ingredient != "recipe_name":
            ingredient_cost = ingredient_costs.get(ingredient, 0)
            total_cost += ingredient_cost * amount
    return total_cost

def change_price(ingredient_costs, ingredient_name, change_percent):
    if ingredient_name in ingredient_costs:
        ingredient_costs[ingredient_name] += ingredient_costs[ingredient_name] * change_percent

def change_all_prices(ingredient_costs, change_percent):
    new_ingredient_costs = ingredient_costs.copy()
    for ingredient in new_ingredient_costs:
        change_price(new_ingredient_costs, ingredient, change_percent)
    return new_ingredient_costs

def random_fluctuations(ingredient_costs, max_rise, max_fall):
    new_costs = ingredient_costs.copy()
    for ingredient in new_costs:
        change_percent = random.uniform(max_fall, max_rise)
        change_price(new_costs, ingredient, change_percent)
    return new_costs

def simulate_recipe_costs(recipe, ingredient_costs):
    base_cost = calculate_unit_cost(recipe, ingredient_costs)
    min_cost = base_cost
    max_cost = base_cost

    for _ in range(10000):  # run 10,000 simulations
        current_simulation = random_fluctuations(ingredient_costs, 0.05, -0.05)
        for _ in range(20):  # for 20 "turns"
            current_simulation = random_fluctuations(current_simulation, 0.05, -0.05)
            current_cost = calculate_unit_cost(recipe, current_simulation)
            if current_cost > max_cost:
                max_cost = current_cost
            if current_cost < min_cost:
                min_cost = current_cost

    return {
        "recipe_name": recipe["recipe_name"],
        "starting_cost": base_cost,
        "min_cost": min_cost,
        "max_cost": max_cost
    }

# Define ingredient costs
ingredient_costs = {
    "flour": 2.5,
    "sugar": 1.5,
    "butter": 3.0,
    "water": 0.01,
    "salt": 1,
    "yeast": 0.05,
    "eggs": 0.2,
    "milk": 0.8,
    "chocolate_chips": 4.0,
    "vanilla_extract": 20,
    "baking_powder": 0.02,
    "baking_soda": 0.015,
    "cinnamon": 0.03,
    "raisins": 5.0
}

# Define a sample recipe
dinner_rolls_recipe = {
    "recipe_name": "Dinner Rolls",
    "flour": 1,
    "water": 0.3,
    "yeast": 0.02,
    "salt": 0.01,
    "butter": 0.1
}

# Calculate cost for dinner rolls with 20% price increase and decrease
markup_20 = change_all_prices(ingredient_costs, 0.20)
markdown_20 = change_all_prices(ingredient_costs, -0.20)

# Print the costs
print(f"Cost with 20% increase: ${calculate_unit_cost(dinner_rolls_recipe, markup_20):.2f}")
print(f"Cost with 20% decrease: ${calculate_unit_cost(dinner_rolls_recipe, markdown_20):.2f}")

# Example of running the simulation for every recipe
recipes = [dinner_rolls_recipe]
for recipe in recipes:
    recipe_costs = simulate_recipe_costs(recipe, ingredient_costs)
    print(recipe_costs)
