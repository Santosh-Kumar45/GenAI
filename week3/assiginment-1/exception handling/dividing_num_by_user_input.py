# PROBLEM 3
# Divide 100 by a user-provided number.
# Handle ZeroDivisionError.

try:
    n=int(input("enter number"))
    num=100/n
    print(num)
except ZeroDivisionError:
    print("zero not allowed")