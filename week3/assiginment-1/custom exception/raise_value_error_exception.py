# PROBLEM 1
# Given:
#
# age = 15
#
# Raise a ValueError if age is below 18.
# Handle the exception using try/except.

age=15
try:
    if age < 18:
        raise ValueError("Age must be 18 or above.")
    print("Access allowed.")
except ValueError as error:
    print("Error:", error)