numbers = [1,2,3,4,5,6,7,8,9]
# List of numbers to analyze

total = 0
# Accumulator for total sum

highest = numbers[0]
# Initialize highest with first element (safe for any list)

lowest = numbers[0]
# Initialize lowest with first element

even_count = 0
# Counter for even numbers

odd_count = 0
# Counter for odd numbers

even_sum = 0
# Accumulator for sum of even numbers

odd_sum = 0
# Accumulator for sum of odd numbers


for num in numbers:
    # Loop through each number in the list

    total = total + num
    # Add current number to total

    if num > highest:
        highest = num
        # Update highest if current number is greater

    if num < lowest:
        lowest = num
        # Update lowest if current number is smaller

    if num % 2 == 0:
        # Check if number is even using modulus operator
        
        even_count = even_count + 1
        # Increase even counter
        
        even_sum = even_sum + num
        # Add to even sum
    else:
        # If not even, it must be odd
        
        odd_count = odd_count + 1
        # Increase odd counter
        
        odd_sum = odd_sum + num
        # Add to odd sum


print("Total:", total)
# Display total sum

print("Highest:", highest)
# Display highest value

print("Lowest:", lowest)
# Display lowest value

print("Even Count:", even_count)
# Display number of even values

print("Odd Count:", odd_count)
# Display number of odd values

print("Even Sum:", even_sum)
# Display sum of even numbers

print("Odd Sum:", odd_sum)
# Display sum of odd numbers