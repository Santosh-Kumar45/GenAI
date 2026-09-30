# PROBLEM 1
# Create a function greet() that prints a greeting.
# Use if __name__ == "__main__" to call it.

# PROBLEM 2
# Create a function add(a, b) that returns the sum.
# Call it inside the main guard.

# PROBLEM 3
# Create a function show_message(message).
# Use the main guard to test the function.

# PROBLEM 4
# Create a function calculate_square(number).
# Return the square and print the result inside the main guard.

# PROBLEM 5
# Create a small program with:
#
# calculate_total(price, quantity)
# show_bill()
#
# Use if __name__ == "__main__" to run show_bill().

# ------------------------------------------------------------
# SOLUTIONS
# ------------------------------------------------------------
# Solution 1
def greet():
    print("Hello, Python learner!")

if __name__ == "__main__":
    greet()

# Solution 2
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(10, 20))

# Solution 3
def show_message(message):
    print(message)

if __name__ == "__main__":
    show_message("Learning Python is fun!")

# Solution 4
def calculate_square(number):
    return number * number

if __name__ == "__main__":
    result = calculate_square(8)
    print(result)

# Solution 5
def calculate_total(price, quantity):
    return price * quantity

def show_bill():
    total = calculate_total(500, 3)
    print(f"Total bill: ₹{total}")

if __name__ == "__main__":
    show_bill()

