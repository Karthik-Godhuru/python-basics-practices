for num in range(1, 21):
    # Outer loop runs from 1 to 20
    # 'num' represents the number whose table we are printing
    
    print()
    # Print a blank line for better formatting between tables
    
    print("Table of", num)
    # Print the heading for the current multiplication table
    
    for i in range(1, 11):
        # Inner loop runs from 1 to 10
        # 'i' represents the multiplier
        
        print(num, "x", i, "=", num * i)
        # Print the multiplication result
        # Example: 5 x 3 = 15