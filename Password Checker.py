def check_password_strength(password):
    length_score = 0
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"

    if len(password) >= 8:
        length_score = 1

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    score = length_score + has_upper + has_lower + has_digit + has_special

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"


password = input("Enter a password to test: ")
strength = check_password_strength(password)

print("Password Strength:", strength)