valid_password = False

# until we get a valid password
while not valid_password:
    password = input("Please set a new password")
    
    length_valid = False
    special_character_valid = False
    
    if len(password) < 16 and len(password) > 5:
        print("password is the right length")
        length_valid = True
    elif len(password) <= 5:
        print("Password is too short")
    else:
        print("password must be between 5 and 16 characters")
    
    if "!" in password:
        print("special character found")
        special_character_valid = True
    else:
        print("This password needs an ! character somewhere")
    
    if special_character_valid and length_valid:
        print("Your password has been set")
        valid_password = True

print("Thank you for resetting your password")
