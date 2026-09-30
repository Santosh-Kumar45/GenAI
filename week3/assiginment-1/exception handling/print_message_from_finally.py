
# PROBLEM 5
# Use try, except and finally.
# Print a message from finally.

try:
    number = int("50")
    print(number)
except ValueError:
    print("Invalid number.")
finally:
    print("Program finished.")