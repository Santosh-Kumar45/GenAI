# PROBLEM 4
# Create a custom exception called InvalidMarksError.
# Raise it when marks are below 0 or above 100.
class InvalidMarksError(Exception):
    pass

marks = 105
try:
    if marks < 0 or marks > 100:
        raise InvalidMarksError(
            "Marks must be between 0 and 100."
        )
    print("Valid marks.")
except InvalidMarksError as error:
    print("Error:", error)