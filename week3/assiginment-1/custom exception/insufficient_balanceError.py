
# PROBLEM 3
# Create a custom exception called InsufficientBalanceError.
# Raise it when withdrawal amount is greater than balance.

class InsufficientBalanceError(Exception):
    pass

balance = 500
withdrawal = 800
try:
    if withdrawal > balance:
        raise InsufficientBalanceError(
            "Insufficient balance."
        )
    print("Withdrawal successful.")
except InsufficientBalanceError as error:
    print("Error:", error)