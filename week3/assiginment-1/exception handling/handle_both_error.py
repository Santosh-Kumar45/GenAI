# PROBLEM 4
# Create a program that handles both:
# - ValueError
# - ZeroDivisionError

try:
    number = int("100")
    divisor = 0
    result = number / divisor
    print(result)
except ValueError:
    print("Invalid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
    