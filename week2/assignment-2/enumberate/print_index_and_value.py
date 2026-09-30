# PROBLEM 1
# Print both the index and value of:
#
# fruits = ["Apple", "Banana", "Mango"]

fruits = ["Apple", "Banana", "Mango"]
for index, fruit in enumerate(fruits):
    print(index, fruit)





# PROBLEM 2
# Print a numbered list starting from 1:
#
# students = ["Rahul", "Priya", "Amit"]

# PROBLEM 3
# Use enumerate() to print:
#
# 1. Python
# 2. SQL
# 3. Git
# 4. GenAI

# PROBLEM 4
# Use enumerate() to print the index and name of:
#
# employees = ["Rahul", "Priya", "Amit", "Neha"]

# PROBLEM 5
# Create a numbered shopping list using enumerate(),
# starting the numbering from 1.



    # Solution 2
students = ["Rahul", "Priya", "Amit"]
for number, student in enumerate(students, start=1):
    print(f"{number}. {student}")

# Solution 3
skills = ["Python", "SQL", "Git", "GenAI"]
for number, skill in enumerate(skills, start=1):
    print(f"{number}. {skill}")

# Solution 4
employees = ["Rahul", "Priya", "Amit", "Neha"]
for index, employee in enumerate(employees):
    print(index, employee)

# Solution 5
shopping_list = ["Laptop", "Mouse", "Keyboard", "Headphones"]
for number, item in enumerate(shopping_list, start=1):
    print(f"{number}. {item}")
