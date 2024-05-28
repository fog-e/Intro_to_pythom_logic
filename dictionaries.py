# Dictionary of pets with their counts
pets = {
    "cat": 1,
    "dog": 1,
    "fish": 37
}

# Print each key-value pair in the pets dictionary
for key, value in pets.items():
    print(key, value)

# User dictionary with nested customer details
user = {
    "username": "FogTheDeveloper",
    "email": "fog@whatever.com",
    "title": "IT CEO",
    "customer_details": {
        "Client": "Multiverse",
        "last_login": "May 23"
    }
}

# Update the user's title
user["title"] = "CTO"

# Print the client detail from the nested dictionary
print(user["customer_details"]["Client"])

# Print the entire user dictionary
print(user)
