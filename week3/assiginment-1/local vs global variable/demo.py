# PROBLEM 1
# Create a function show_city().
# Create a local variable city inside the function
# and print it.

# PROBLEM 2
# Create a global variable course = "GenAI".
# Create a function that prints course.

# PROBLEM 3
# Create a global variable name = "Rahul".
# Inside a function create a local variable with the same name
# and set it to "Priya".
# Print both values to observe the difference.

# PROBLEM 4
# Create a global variable score = 10.
# Create a function that uses the global keyword to increase
# score by 5.

# PROBLEM 5
# Create a function calculate_total(price, quantity)
# that returns the total instead of using a global variable.




# Solution 1
def show_city():
    city = "Delhi"
    print(city)

show_city()

# Solution 2
course = "GenAI"

def show_course():
    print(course)

show_course()

# Solution 3
name = "Rahul"

def show_names():
    name = "Priya"
    print("Inside function:", name)

show_names()
print("Outside function:", name)

# Solution 4
score = 10

def increase_score():
    global score
    score = score + 5

increase_score()
print(score)

# Solution 5
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(500, 3)
print(total)
