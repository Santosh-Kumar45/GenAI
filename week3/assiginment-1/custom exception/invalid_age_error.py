# PROBLEM 2
# Create a custom exception called InvalidAgeError.
# Raise it when age is below 18.


class InvalidAgeError(Exception):
    pass

age = 16
try:
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    print("Access allowed.")
except InvalidAgeError as error:
    print("Error:", error)