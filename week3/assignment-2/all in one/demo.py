# ============================================================
# PYTHON FOR BEGINNERS - CLASS 6
# PRACTICE PROBLEMS WITH SOLUTIONS
# ============================================================
# Topics:
# 1. Virtual Environments (venv)
# 2. Installing Packages using pip
# 3. Importing Modules
# 4. Creating Reusable Modules
# 5. Introduction to Multithreading
# 6. Best Practices for Organizing Python Projects
# ============================================================


# ============================================================
# PART 1 - VIRTUAL ENVIRONMENTS
# ============================================================

# PROBLEM 1
# Write the terminal command to create a virtual environment
# called .venv.


# PROBLEM 2
# Write the command to activate .venv on:
# 1. Windows Command Prompt
# 2. Windows PowerShell
# 3. macOS/Linux


# PROBLEM 3
# Write the command used to deactivate a virtual environment.


# PROBLEM 4
# Write the command used to check which Python executable
# is currently being used:
# 1. Windows
# 2. macOS/Linux


# PROBLEM 5
# In your own words, explain why virtual environments are
# useful when working on multiple Python projects.


# ------------------------------------------------------------
# SOLUTIONS
# ------------------------------------------------------------

# Solution 1
# python -m venv .venv


# Solution 2
# Windows Command Prompt:
# .venv\Scripts\activate
#
# Windows PowerShell:
# .venv\Scripts\Activate.ps1
#
# macOS/Linux:
# source .venv/bin/activate


# Solution 3
# deactivate


# Solution 4
# Windows:
# where python
#
# macOS/Linux:
# which python


# Solution 5
# Virtual environments keep each project's Python packages
# separate and help prevent dependency/version conflicts.


# ============================================================
# PART 2 - pip
# ============================================================

# PROBLEM 1
# Write the command to install the requests package.


# PROBLEM 2
# Write the command to display installed packages.


# PROBLEM 3
# Write the command to install a package from
# requirements.txt.


# PROBLEM 4
# Write the command to create requirements.txt from the
# currently installed packages.


# PROBLEM 5
# Write the command to uninstall requests.


# ------------------------------------------------------------
# SOLUTIONS
# ------------------------------------------------------------

# Solution 1
# pip install requests


# Solution 2
# pip list


# Solution 3
# pip install -r requirements.txt


# Solution 4
# pip freeze > requirements.txt


# Solution 5
# pip uninstall requests


# ============================================================
# PART 3 - IMPORTING MODULES
# ============================================================

# PROBLEM 1
# Import the math module and calculate sqrt(144).


# PROBLEM 2
# Import sqrt directly from math and calculate sqrt(81).


# PROBLEM 3
# Import random using the alias "rand".
# Generate a random number between 1 and 10.


# PROBLEM 4
# Import datetime as "dt" and print the current date and time.


# PROBLEM 5
# Import ceil and floor from math.
# Use both functions on 7.4.


# ------------------------------------------------------------
# SOLUTIONS
# ------------------------------------------------------------

# Solution 1
import math

print(math.sqrt(144))


# Solution 2
from math import sqrt

print(sqrt(81))


# Solution 3
import random as rand

print(rand.randint(1, 10))


# Solution 4
import datetime as dt

print(dt.datetime.now())


# Solution 5
from math import ceil, floor

print(ceil(7.4))
print(floor(7.4))


# ============================================================
# PART 4 - CREATING REUSABLE MODULES
# ============================================================

# PROBLEM 1
# Create a module called calculator.py containing:
#
# add(a, b)
# subtract(a, b)
#
# Each function should return its result.


# PROBLEM 2
# Import calculator.py and use add().


# PROBLEM 3
# Import only the subtract() function from calculator.py.


# PROBLEM 4
# Import calculator using the alias "calc".
# Use calc.add().


# PROBLEM 5
# Add a multiply(a, b) function to calculator.py
# and use it from another Python file.


# ------------------------------------------------------------
# SOLUTIONS
# ------------------------------------------------------------

# Solution 1
#calculator.py

def add(a, b):
     return a + b


def subtract(a, b):
     return a - b


# Solution 2
# main.py
#
# import calculator
#
# print(calculator.add(10, 20))


# Solution 3
# from calculator import subtract
#
# print(subtract(20, 5))


# Solution 4
# import calculator as calc
#
# print(calc.add(10, 20))


# Solution 5
# calculator.py
#
# def multiply(a, b):
#     return a * b
#
#
# main.py
#
# import calculator
#
# print(calculator.multiply(5, 4))


# ============================================================
# PART 5 - __name__ == "__main__"
# ============================================================

# PROBLEM 1
# Create a function greet() and call it only when the Python
# file is executed directly.


# PROBLEM 2
# Create:
#
# def add(a, b):
#     return a + b
#
# Print the result only inside the main guard.


# PROBLEM 3
# Explain what __name__ contains when a Python file is
# executed directly.


# PROBLEM 4
# Explain why a reusable module may use:
#
# if __name__ == "__main__":
#
# around testing code.


# PROBLEM 5
# Create a function main() and use the main guard to call it.


# ------------------------------------------------------------
# SOLUTIONS
# ------------------------------------------------------------

# Solution 1
def greet():
    print("Hello from Python!")


if __name__ == "__main__":
    greet()


# Solution 2
def add(a, b):
    return a + b


if __name__ == "__main__":
    print(add(10, 20))


# Solution 3
# When a Python file is executed directly,
# __name__ contains "__main__".


# Solution 4
# It prevents the testing code from running automatically
# when another Python file imports the module.


# Solution 5
def main():
    print("Program started.")


if __name__ == "__main__":
    main()


# ============================================================
# PART 6 - INTRODUCTION TO MULTITHREADING
# ============================================================

# PROBLEM 1
# Import threading and create a thread that runs:
#
# def greet():
#     print("Hello from a thread!")


# PROBLEM 2
# Start the thread and wait for it to finish using join().


# PROBLEM 3
# Create a function task(name) that:
# - prints that the task started
# - waits for 1 second using time.sleep()
# - prints that the task finished
#
# Run two tasks using two threads.


# PROBLEM 4
# Create three threads to process:
#
# ["File 1", "File 2", "File 3"]
#
# Use one function called process_file(file_name).


# PROBLEM 5
# Explain the difference between:
#
# thread.start()
# thread.join()


# ------------------------------------------------------------
# SOLUTIONS
# ------------------------------------------------------------

# Solution 1
import threading


def greet():
    print("Hello from a thread!")


thread = threading.Thread(target=greet)


# Solution 2
thread.start()
thread.join()


# Solution 3
import threading
import time


def task(name):

    print(f"{name} started")

    time.sleep(1)

    print(f"{name} finished")


thread1 = threading.Thread(
    target=task,
    args=("Task 1",)
)

thread2 = threading.Thread(
    target=task,
    args=("Task 2",)
)

thread1.start()
thread2.start()

thread1.join()
thread2.join()


# Solution 4
import threading
import time


def process_file(file_name):

    print(f"Processing {file_name}")

    time.sleep(1)

    print(f"Finished {file_name}")


files = ["File 1", "File 2", "File 3"]

threads = []

for file_name in files:

    thread = threading.Thread(
        target=process_file,
        args=(file_name,)
    )

    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()


# Solution 5
# start() begins execution of the thread.
#
# join() waits for the thread to finish.


# ============================================================
# PART 7 - PROJECT ORGANIZATION
# ============================================================

# PROBLEM 1
# Design a project structure for a simple Python calculator.
#
# Include:
# - source code
# - tests
# - requirements.txt
# - README.md
# - .gitignore


# PROBLEM 2
# Decide where these files should go:
#
# calculator.py
# input.txt
# test_calculator.py
# requirements.txt
# README.md


# PROBLEM 3
# Rename these poor variable/function names into better names:
#
# x
# a
# temp
# do()
# calc()


# PROBLEM 4
# Explain why it is better to separate:
#
# main.py
# calculator.py
#
# instead of putting every function in one very large file.


# PROBLEM 5
# Create a simple function that calculates a total.
# Keep the function separate from the main program flow.


# ------------------------------------------------------------
# SOLUTIONS
# ------------------------------------------------------------

# Solution 1
#
# calculator_project/
#
#     .venv/
#     src/
#         main.py
#         calculator.py
#     tests/
#         test_calculator.py
#     requirements.txt
#     README.md
#     .gitignore


# Solution 2
#
# calculator.py
# -> src/
#
# input.txt
# -> data/
#
# test_calculator.py
# -> tests/
#
# requirements.txt
# -> project root
#
# README.md
# -> project root


# Solution 3
#
# x -> student_name
# a -> total_amount
# temp -> temporary_value
# do() -> calculate_total()
# calc() -> calculate_bill()


# Solution 4
# Separating files makes the project easier to understand,
# maintain and reuse.
#
# calculator.py can contain calculation functions.
# main.py can control the overall program flow.


# Solution 5
def calculate_total(price, quantity):
    return price * quantity


if __name__ == "__main__":

    total = calculate_total(500, 3)

    print(total)


# ============================================================
# PART 8 - MIXED PRACTICAL PROBLEMS
# ============================================================

# PROBLEM 1 - REUSABLE CALCULATOR MODULE
#
# Create calculator.py with:
#
# add()
# subtract()
# multiply()
# divide()
#
# Create main.py that imports calculator and uses the
# functions.


# PROBLEM 2 - FILE UTILITY MODULE
#
# Create file_utils.py containing:
#
# save_text(filename, text)
# read_text(filename)
#
# Use these functions from main.py.


# PROBLEM 3 - MULTITHREADED FILE PROCESSOR
#
# Create a function process_file(file_name).
#
# It should:
# - print "Processing..."
# - wait for 1 second
# - print "Finished..."
#
# Use three threads to process three file names.


# PROBLEM 4 - PACKAGE MANAGEMENT
#
# Imagine your project uses:
#
# requests
# pandas
#
# Write the commands needed to:
# 1. Create a virtual environment
# 2. Activate it on Windows
# 3. Install the packages
# 4. Create requirements.txt


# PROBLEM 5 - PROJECT STRUCTURE
#
# Design a clean structure for a small student-management
# Python project containing:
# - main program
# - reusable student module
# - data file
# - tests
# - dependencies
# - documentation


# ------------------------------------------------------------
# SOLUTIONS
# ------------------------------------------------------------

# Solution 1
# calculator.py
#
# def add(a, b):
#     return a + b
#
#
# def subtract(a, b):
#     return a - b
#
#
# def multiply(a, b):
#     return a * b
#
#
# def divide(a, b):
#     return a / b
#
#
# main.py
#
# import calculator
#
# print(calculator.add(10, 20))
# print(calculator.subtract(20, 5))
# print(calculator.multiply(5, 4))
# print(calculator.divide(20, 4))


# Solution 2
# file_utils.py
#
# def save_text(filename, text):
#     with open(filename, "w") as file:
#         file.write(text)
#
#
# def read_text(filename):
#     with open(filename, "r") as file:
#         return file.read()
#
#
# main.py
#
# import file_utils
#
# file_utils.save_text("notes.txt", "Hello Python!")
#
# content = file_utils.read_text("notes.txt")
#
# print(content)


# Solution 3
import threading
import time


def process_file(file_name):

    print(f"Processing {file_name}")

    time.sleep(1)

    print(f"Finished {file_name}")


file_names = [
    "file1.txt",
    "file2.txt",
    "file3.txt"
]

threads = []

for file_name in file_names:

    thread = threading.Thread(
        target=process_file,
        args=(file_name,)
    )

    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()


# Solution 4
#
# 1. Create environment:
#    python -m venv .venv
#
# 2. Activate on Windows Command Prompt:
#    .venv\Scripts\activate
#
# 3. Install packages:
#    pip install requests pandas
#
# 4. Create requirements.txt:
#    pip freeze > requirements.txt


# Solution 5
#
# student_project/
#
#     .venv/
#     src/
#         main.py
#         student.py
#     data/
#         students.txt
#     tests/
#         test_student.py
#     requirements.txt
#     README.md
#     .gitignore


# ============================================================
# FINAL CHALLENGES
# ============================================================

# CHALLENGE 1
# Build a reusable "text_utils.py" module containing:
#
# clean_text(text)
# count_characters(text)
#
# Import it into main.py and use both functions.


# CHALLENGE 2
# Build a "file_logger.py" module containing:
#
# log_message(message)
#
# It should append messages to "app.log".
# Import the module from main.py.


# CHALLENGE 3
# Build a simple multithreaded task runner.
#
# Create a function run_task(task_name).
# Use three threads to run three tasks.
# Use start() and join() correctly.


# CHALLENGE 4
# Create a clean project structure for a small
# expense-tracking application.
#
# Include:
# - reusable modules
# - data
# - tests
# - requirements.txt
# - README.md
# - .gitignore
# - .venv


# ============================================================
# END OF PRACTICE SCRIPT
# ============================================================
