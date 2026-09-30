# PROBLEM 1
# Convert the string "100" into an integer using try/except.
# Handle ValueError.

try:
    num=int("100")
    print(num)
except ValueError:
    print("invalid number")