password = input("Enter the password: ")
# Take password input from user

has_upper = False
# Flag to check if at least one uppercase letter exists

has_digit = False
# Flag to check if at least one digit exists

has_lower = False
# Flag to check if at least one lowercase letter exists

for ch in password:
    # Loop through each character in the password
    
    if ch.isupper():
        has_upper = True
        # If character is uppercase, set flag to True
        
    if ch.islower():
        has_lower = True
        # If character is lowercase, set flag to True
        
    if ch.isdigit():
        has_digit = True
        # If character is a digit, set flag to True

# After checking all characters, evaluate final condition

if len(password) >= 8 and has_upper and has_digit and has_lower:
    # Password must:
    # 1. Be at least 8 characters long
    # 2. Contain uppercase
    # 3. Contain lowercase
    # 4. Contain digit
    
    print("strong")
else:
    print("weak")