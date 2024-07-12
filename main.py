import re
import sys
from itertools import combinations

def check_length(password):
    return len(password) >= 8

def check_complexity(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    return has_upper, has_lower, has_digit, has_special

def generate_username_parts(username):
    parts = username.split()
    combinations_list = []
    for r in range(1, len(parts) + 1):
        combinations_list.extend([''.join(combo) for combo in combinations(parts, r)])
    return combinations_list

def check_uniqueness(password, username):
    username_combinations = generate_username_parts(username.lower())
    for combo in username_combinations:
        if combo and re.search(re.escape(combo), password.lower()):
            return False
    return True

def assess_password_strength(password, username):
    strength_score = 0
    messages = []

    # Check length
    if check_length(password):
        strength_score += 1
    else:
        messages.append("The password must be at least 8 characters long.")
    
    # Check complexity
    has_upper, has_lower, has_digit, has_special = check_complexity(password)
    if has_upper and has_lower and has_digit and has_special:
        strength_score += 1
    else:
        messages.append("Inlcude at least one uppercase letter, one lowercase letter, one digit, and one special character to improve the strength.")
    
    # Check uniqueness
    if check_uniqueness(password, username):
        strength_score += 1
    else:
        messages.append("The password should not contain your username or parts of your name.")
    
    # Determine password strength
    if strength_score == 3:
        strength = "strong"
    elif strength_score == 2:
        strength = "moderate"
    elif strength_score == 1:
        strength = "weak"

    feedback = "Password Strength: {}. ".format(strength.capitalize())
    if messages:
        feedback += " ".join(messages)
    else:
        feedback += "Your password is strong."
    
    return feedback

def main():
    if len(sys.argv) == 3:
        password = sys.argv[1]
        username = sys.argv[2]
    else:
        password = input("Enter your password: ")
        username = input("Enter your username: ")

    strength = assess_password_strength(password, username)
    print(strength)

if __name__ == "__main__":
    main()
