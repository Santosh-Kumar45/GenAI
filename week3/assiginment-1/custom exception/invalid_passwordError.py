
# PROBLEM 5
# Create a custom exception called InvalidPasswordError.
# Raise it if a password has fewer than 8 characters.
class InvalidPasswordError(Exception):
    pass

password = "python"
try:
    if len(password) < 8:
        raise InvalidPasswordError(
            "Password must contain at least 8 characters."
        )
    print("Password accepted.")
except InvalidPasswordError as error:
    print("Error:", error)