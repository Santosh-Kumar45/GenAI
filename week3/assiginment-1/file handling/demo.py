# PROBLEM 1
# Create a file called "notes.txt" with some text in it.
# Then read and print the complete file.

# PROBLEM 2
# Read only the first line from "notes.txt".

# PROBLEM 3
# Read all lines using readlines() and print the resulting list.

# PROBLEM 4
# Read a file line by line using a for loop.
# Remove the extra newline using strip().

# PROBLEM 5
# Create a file called "students.txt" containing:
#
# Rahul
# Priya
# Amit
#
# Read and print each student name.



# Solution 1
with open("notes.txt", "w") as file:
    file.write("Python is easy to learn.\n")
    file.write("Practice makes you better.\n")

with open("notes.txt", "r") as file:
    content = file.read()
print(content)

# Solution 2
with open("notes.txt", "r") as file:
    first_line = file.readline()
print(first_line)

# Solution 3
with open("notes.txt", "r") as file:
    lines = file.readlines()
print(lines)

# Solution 4
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

# Solution 5
with open("students.txt", "w") as file:
    file.write("Rahul\n")
    file.write("Priya\n")
    file.write("Amit\n")

with open("students.txt", "r") as file:
    for student in file:
        print(student.strip())