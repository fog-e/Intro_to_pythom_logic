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
    new_costs = ingredient_costs.copy()
    for ingredient in new_costs:
        change_price(new_costs, ingredient, change_percent)
    return new_costs

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

# Running the simulation for every recipe
recipes = [dinner_rolls_recipe]  # Add more recipes if you have them
for recipe in recipes:
    recipe_costs = simulate_recipe_costs(recipe, ingredient_costs)
    print(recipe_costs)
