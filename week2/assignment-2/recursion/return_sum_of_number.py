# PROBLEM 3
# Create a recursive function sum_to_n(number)
# that returns the sum from 1 to number.

def sum_to_n(number):
    if number == 0:
        return 0
    return number + sum_to_n(number - 1)

print(sum_to_n(5))