numbers = [1,2,3,4,5,6,7,8,9]

total = 0
highest = numbers[0]
lowest = numbers[0]
even_count = 0
odd_count = 0
even_sum = 0
odd_sum = 0

for num in numbers:
    total = total + num

    if num > highest:
        highest = num

    if num < lowest:
        lowest = num

    if num % 2 == 0:
        even_count = even_count + 1
        even_sum = even_sum + num
    else:
        odd_count = odd_count + 1
        odd_sum = odd_sum + num

print("total", total)
print("highest", highest)
print("lowest", lowest)
print("even_count", even_count)
print("odd_count", odd_count)
print("even_sum", even_sum)
print("odd_sum", odd_sum)