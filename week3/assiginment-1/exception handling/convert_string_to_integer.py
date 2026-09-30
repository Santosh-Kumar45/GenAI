# PROBLEM 2
# Try to convert "Python" into an integer.
# Handle the ValueError and print a friendly message.

try:
    name=int("santosh")
    print(name)
except ValueError:
    print("string not found")