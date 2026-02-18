import random   # Import random module to generate random numbers

secret = random.randint(1,10)  
# Generate a random secret number between 1 and 10

for attempt in range(3):  
    # Allow the user 3 attempts to guess
    
    guess = int(input("Enter the guess number bro: "))  
    # Take user input and convert it to integer
    
    if secret == guess:  
        # If guess matches the secret number
        
        print("You win bro")  
        break  
        # Stop the loop because the user guessed correctly
    
    elif secret > guess:  
        # If guess is smaller than the secret number
        
        print("You are very close")  
        # Tell the user they guessed lower
    
    else:  
        # If guess is greater than the secret number
        
        print("You are so far")  
        # Tell the user they guessed higher

else:
    # This else belongs to the for loop
    # It runs only if the loop completes without hitting break
    
    print("Game over bro")