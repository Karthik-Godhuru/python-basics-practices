

num = int(input('Enter a number: '))
# Take integer input from the user.
# This number decides how many values we check.

for i in range(1, num):
    # Loop from 1 up to (but not including) num.
    # Example: if num = 6 → values will be 1,2,3,4,5

    if i % 2 == 0:
        # % is modulus operator.
        # i % 2 checks remainder when divided by 2.
        # If remainder is 0 → number is even.

        print(i, "even")
    else:
        # If remainder is not 0 → number is odd.

        print(i, "odd")