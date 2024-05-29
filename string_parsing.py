def parse_ingredient_string(ingredient_str):
    """
    Parse an ingredient string and return the ingredient name and quantity.
    Example input: "2 cups of sugar"
    Returns: ("sugar", 2, "cups")
    """
    parts = ingredient_str.split(" ")
    quantity = float(parts[0])
    unit = parts[1]
    name = " ".join(parts[3:])
    return name, quantity, unit

def main():
    ingredient_strings = [
        "2 cups of sugar",
        "1.5 kg of flour",
        "3 liters of milk",
        "0.5 oz of yeast"
    ]

    parsed_ingredients = []
    for ingredient_str in ingredient_strings:
        parsed_ingredient = parse_ingredient_string(ingredient_str)
        parsed_ingredients.append(parsed_ingredient)
        print(parsed_ingredient)

if __name__ == "__main__":
    main()
