x = int(input("Enter a number: "))
# Take integer input from the user.
# Convert input (string) into integer using int().

if x > 0:
    # Check if number is greater than zero
    
    print("positive")
    # If condition is True, number is positive

elif x < 0:
    # This block runs only if the first condition was False
    # Check if number is less than zero
    
    print("negative")
    # If condition is True, number is negative

else:
    # This block runs if both above conditions are False
    # That means x is neither > 0 nor < 0
    
    print("zero")
    # So number must be  zero