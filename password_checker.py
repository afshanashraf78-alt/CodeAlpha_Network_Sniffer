import re

def check_password_strength(password):
    strength = 0
    if len(password) >= 8: strength += 1
    if re.search("[a-z]", password): strength += 1
    if re.search("[A-Z]", password): strength += 1
    if re.search("[0-9]", password): strength += 1
    if re.search("[_@$#!%*?&]", password): strength += 1

    if strength == 5: remarks = "Very Strong"
    elif strength == 4: remarks = "Strong"
    elif strength == 3: remarks = "Average"
    else: remarks = "Weak"
        
    print(f"Password Strength Score: {strength}/5")
    print(f"Remarks: {remarks}")

user_password = input("Enter a password to check its strength: ")
check_password_strength(user_password)
