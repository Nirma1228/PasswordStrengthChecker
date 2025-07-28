import re

def check_password_strength(password):
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_symbol = bool(re.search(r'[\W_]', password))

    score = sum([has_upper, has_lower, has_digit, has_symbol])
    if length < 6:
        return "Weak"
    elif length >= 6 and score >= 3:
        return "Medium "
    elif length >= 8 and score == 4:
        return "Strong "
    else:
        return "Weak "

# Get input from user
password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")
