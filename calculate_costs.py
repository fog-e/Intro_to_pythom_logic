import random

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

def calculate_total_cost(recipe, ingredient_costs):
    recipe_name = recipe["recipe_name"]
    total_cost = 0
    for ingredient, amount in recipe.items():
        if not ingredient == "recipe_name":
            ingredient_cost = ingredient_costs.get(ingredient, 0)
            total_cost += (ingredient_cost * amount)
    print(f"Total cost to make {recipe_name}: ${total_cost:.2f}")
    return total_cost

def change_price(ingredient_costs, ingredient_name, change_percent):
    ingredient_costs[ingredient_name] = ingredient_costs[ingredient_name] * (1 + change_percent)

def change_all_prices(ingredient_costs, change_percent):
    new_ingredient_costs = ingredient_costs.copy()
    for ingredient in new_ingredient_costs.items():
        change_price(new_ingredient_costs, ingredient[0], change_percent)
    return new_ingredient_costs

def random_fluctuations(ingredient_costs, max_rise, max_fall):
    new_ingredient_costs = ingredient_costs.copy()
    for ingredient in new_ingredient_costs.items():
        change_percent = random.uniform(max_fall, max_rise)
        change_price(new_ingredient_costs, ingredient[0], change_percent)
    return new_ingredient_costs

# Running the simulation for the dinner rolls recipe
markup_20 = change_all_prices(ingredient_costs, 0.20)
markdown_20 = change_all_prices(ingredient_costs, -0.20)

total_cost = calculate_total_cost(dinner_rolls_recipe, ingredient_costs)
markup_total_cost = calculate_total_cost(dinner_rolls_recipe, markup_20)
markdown_total_cost = calculate_total_cost(dinner_rolls_recipe, markdown_20)

def simulate_recipe_costs(recipe, ingredient_costs):
    base_cost = calculate_total_cost(recipe, ingredient_costs)
    min_cost = base_cost
    max_cost = base_cost
    for _ in range(10000):  # run 10,000 simulations
        current_simulation = random_fluctuations(ingredient_costs, 0.05, -0.05)
        for _ in range(20):  # for 20 "turns"
            current_simulation = random_fluctuations(current_simulation, 0.05, -0.05)
            current_cost = calculate_total_cost(recipe, current_simulation)
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

# Example of running the simulation for every recipe
recipes = [dinner_rolls_recipe]
for recipe in recipes:
    recipe_costs = simulate_recipe_costs(recipe, ingredient_costs)
    print(recipe_costs)
