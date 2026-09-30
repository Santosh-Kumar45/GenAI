
# ============================================================
# PART 4 - MAGIC / DUNDER METHODS
# ============================================================

# PROBLEM 1
# Create a Student class with __init__().
# Add __str__() so printing the object displays the
# student's name.


# PROBLEM 2
# Create a Course class containing a list of topics.
# Implement __len__() so len(course) returns the number
# of topics.


# PROBLEM 3
# Create a Score class with a value.
# Implement __add__() so two Score objects can be added.


# PROBLEM 4
# Create a Product class with name and price.
# Implement __str__() to display both values.


# PROBLEM 5
# Explain what a dunder method is and give two examples.


# ------------------------------------------------------------
# SOLUTIONS
# ------------------------------------------------------------

# Solution 1
class Student:

    def __init__(self, name):

        self.name = name

    def __str__(self):

        return f"Student: {self.name}"


student = Student("Rahul")

print(student)


# Solution 2
class Course:

    def __init__(self, topics):

        self.topics = topics

    def __len__(self):

        return len(self.topics)


course = Course([
    "Python",
    "Functions",
    "OOP"
])

print(len(course))


# Solution 3
class Score:

    def __init__(self, value):

        self.value = value

    def __add__(self, other):

        return Score(self.value + other.value)

    def __str__(self):

        return str(self.value)


score1 = Score(80)
score2 = Score(15)

total = score1 + score2

print(total)


# Solution 4
class Product:

    def __init__(self, name, price):

        self.name = name
        self.price = price

    def __str__(self):

        return f"{self.name} - ₹{self.price}"


product = Product("Laptop", 60000)

print(product)


# Solution 5
# A dunder method is a special Python method with double
# underscores around its name.
#
# Examples:
# __init__
# __str__
# __len__
