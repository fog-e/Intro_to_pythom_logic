password = input("Please set a new password")

special_character_check = "!" in password

if len(password) < 16 and len(password) > 5:
    print("password is the right length")
elif len(password) < 5:
    print("Password is too short")
else:
    print("password must be between 5 and 16 characters")

if special_character_check:
    print("special character found")
else:
    print("This password needs an ! character somewhere")
