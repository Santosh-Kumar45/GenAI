# ============================================================
# PYTHON FOR BEGINNERS - CLASS 7
# PRACTICE PROBLEMS WITH SOLUTIONS
# ============================================================
# Topics:
# 1. Introduction to OOP
# 2. Classes and Objects
# 3. Attributes and Methods
# 4. Constructors
# 5. Magic (Dunder) Methods
# 6. Encapsulation
# 7. Static Methods
# 8. Inheritance
# 9. Types of Inheritance
# ============================================================


# ============================================================
# PART 1 - CLASSES AND OBJECTS
# ============================================================

# PROBLEM 1
# Create an empty class called Student.
# Create one object from it.


# PROBLEM 2
# Create a class called Car.
# Create two objects from the class.


# PROBLEM 3
# Create a class called Book.
# Create an object and add:
# title
# author
# price
# as attributes.


# PROBLEM 4
# Create a class called Laptop.
# Create two objects with different brand values.


# PROBLEM 5
# Explain the difference between a class and an object.


# ------------------------------------------------------------
# SOLUTIONS
# ------------------------------------------------------------

# Solution 1
class Student:
    pass


student = Student()

print(student)


# Solution 2
class Car:
    pass


car1 = Car()
car2 = Car()

print(car1)
print(car2)


# Solution 3
class Book:
    pass


book = Book()

book.title = "Python Basics"
book.author = "John"
book.price = 500

print(book.title)
print(book.author)
print(book.price)


# Solution 4
class Laptop:
    pass


laptop1 = Laptop()
laptop2 = Laptop()

laptop1.brand = "Dell"
laptop2.brand = "Lenovo"

print(laptop1.brand)
print(laptop2.brand)


# Solution 5
# A class is a blueprint.
# An object is an actual instance created from that blueprint.


# ============================================================
# PART 2 - ATTRIBUTES AND METHODS
# ============================================================

# PROBLEM 1
# Create a class Student with a method introduce().
# The method should print:
# "Hello, I am a student."


# PROBLEM 2
# Create a Student class with an attribute name.
# Create a method introduce() that uses self.name.


# PROBLEM 3
# Create a class Rectangle with:
# length
# width
#
# Create a method area() that prints the area.


# PROBLEM 4
# Create a class Employee with:
# name
# role
#
# Create a method show_info().


# PROBLEM 5
# Create a class BankAccount with:
# owner
# balance
#
# Create a method show_balance().


# ------------------------------------------------------------
# SOLUTIONS
# ------------------------------------------------------------

# Solution 1
class Student:

    def introduce(self):
        print("Hello, I am a student.")


student = Student()

student.introduce()


# Solution 2
class Student:

    def introduce(self):
        print(f"Hello, my name is {self.name}.")


student = Student()

student.name = "Rahul"

student.introduce()


# Solution 3
class Rectangle:

    def area(self):
        print(self.length * self.width)


rectangle = Rectangle()

rectangle.length = 10
rectangle.width = 5

rectangle.area()


# Solution 4
class Employee:

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")


employee = Employee()

employee.name = "Rahul"
employee.role = "AI Engineer"

employee.show_info()


# Solution 5
class BankAccount:

    def show_balance(self):
        print(f"Balance: ₹{self.balance}")


account = BankAccount()

account.owner = "Rahul"
account.balance = 5000

account.show_balance()


# ============================================================
# PART 3 - CONSTRUCTORS
# ============================================================

# PROBLEM 1
# Create a Student class with a constructor accepting:
# name
# age
# course
#
# Store them as attributes.


# PROBLEM 2
# Create a Book class with:
# title
# author
# price
#
# Use __init__() to initialize them.


# PROBLEM 3
# Create a Rectangle class with:
# length
# width
#
# Add an area() method.


# PROBLEM 4
# Create an Employee class with:
# name
# role
# salary
#
# Add a show_info() method.


# PROBLEM 5
# Create a Product class with:
# name
# price
# category
#
# Create two different objects.


# ------------------------------------------------------------
# SOLUTIONS
# ------------------------------------------------------------

# Solution 1
class Student:

    def __init__(self, name, age, course):

        self.name = name
        self.age = age
        self.course = course


student = Student("Rahul", 21, "GenAI")

print(student.name)
print(student.age)
print(student.course)


# Solution 2
class Book:

    def __init__(self, title, author, price):

        self.title = title
        self.author = author
        self.price = price


book = Book("Python Basics", "John", 500)

print(book.title)
print(book.author)
print(book.price)


# Solution 3
class Rectangle:

    def __init__(self, length, width):

        self.length = length
        self.width = width

    def area(self):

        return self.length * self.width


rectangle = Rectangle(10, 5)

print(rectangle.area())


# Solution 4
class Employee:

    def __init__(self, name, role, salary):

        self.name = name
        self.role = role
        self.salary = salary

    def show_info(self):

        print(self.name)
        print(self.role)
        print(self.salary)


employee = Employee(
    "Priya",
    "Developer",
    60000
)

employee.show_info()


# Solution 5
class Product:

    def __init__(self, name, price, category):

        self.name = name
        self.price = price
        self.category = category


product1 = Product("Laptop", 60000, "Electronics")
product2 = Product("Book", 500, "Education")

print(product1.name)
print(product2.name)


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


# ============================================================
# PART 5 - ENCAPSULATION
# ============================================================

# PROBLEM 1
# Create a BankAccount class with:
# owner
# _balance
#
# Add a show_balance() method.


# PROBLEM 2
# Create a User class with a __password attribute.
# Add a check_password() method.


# PROBLEM 3
# Create a Temperature class with a private-style
# __temperature attribute.
# Add a get_temperature() method.


# PROBLEM 4
# Explain the difference between:
# balance
# _balance
# __balance


# PROBLEM 5
# Create a simple Employee class where salary is stored
# using _salary and displayed through show_salary().


# ------------------------------------------------------------
# SOLUTIONS
# ------------------------------------------------------------

# Solution 1
class BankAccount:

    def __init__(self, owner, balance):

        self.owner = owner
        self._balance = balance

    def show_balance(self):

        print(f"Balance: ₹{self._balance}")


account = BankAccount("Rahul", 5000)

account.show_balance()


# Solution 2
class User:

    def __init__(self, password):

        self.__password = password

    def check_password(self, password):

        return self.__password == password


user = User("python123")

print(user.check_password("python123"))
print(user.check_password("wrong"))


# Solution 3
class Temperature:

    def __init__(self, temperature):

        self.__temperature = temperature

    def get_temperature(self):

        return self.__temperature


temperature = Temperature(25)

print(temperature.get_temperature())


# Solution 4
# balance:
# -> Normal attribute.
#
# _balance:
# -> Convention indicating internal/protected-style use.
#
# __balance:
# -> Triggers name mangling.


# Solution 5
class Employee:

    def __init__(self, salary):

        self._salary = salary

    def show_salary(self):

        print(f"Salary: ₹{self._salary}")


employee = Employee(60000)

employee.show_salary()


# ============================================================
# PART 6 - STATIC METHODS
# ============================================================

# PROBLEM 1
# Create a MathHelper class with a static method add(a, b).


# PROBLEM 2
# Add a static method is_even(number).


# PROBLEM 3
# Create a TemperatureConverter class with a static method
# celsius_to_fahrenheit(celsius).


# PROBLEM 4
# Create a StringHelper class with a static method
# count_characters(text).


# PROBLEM 5
# Explain why a static method does not need self.


# ------------------------------------------------------------
# SOLUTIONS
# ------------------------------------------------------------

# Solution 1
class MathHelper:

    @staticmethod
    def add(a, b):

        return a + b


print(MathHelper.add(10, 20))


# Solution 2
class MathHelper:

    @staticmethod
    def is_even(number):

        return number % 2 == 0


print(MathHelper.is_even(10))
print(MathHelper.is_even(7))


# Solution 3
class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(celsius):

        return (celsius * 9 / 5) + 32


print(TemperatureConverter.celsius_to_fahrenheit(25))


# Solution 4
class StringHelper:

    @staticmethod
    def count_characters(text):

        return len(text)


print(StringHelper.count_characters("Python"))


# Solution 5
# A static method does not need information from a specific
# object, so it does not need self.


# ============================================================
# PART 7 - INHERITANCE
# ============================================================

# PROBLEM 1
# Create an Animal parent class with eat().
# Create a Dog child class with bark().
# Demonstrate inheritance.


# PROBLEM 2
# Create a Person class with a name and introduce().
# Create Student(Person) with study().


# PROBLEM 3
# Create a Vehicle class with move().
# Create Car(Vehicle) with drive().


# PROBLEM 4
# Override speak() in Dog and Cat classes inherited from Animal.


# PROBLEM 5
# Use super() to initialize a parent class attribute from
# a child class constructor.


# ------------------------------------------------------------
# SOLUTIONS
# ------------------------------------------------------------

# Solution 1
class Animal:

    def eat(self):

        print("Animal is eating.")


class Dog(Animal):

    def bark(self):

        print("Dog is barking.")


dog = Dog()

dog.eat()
dog.bark()


# Solution 2
class Person:

    def __init__(self, name):

        self.name = name

    def introduce(self):

        print(f"My name is {self.name}.")


class Student(Person):

    def study(self):

        print(f"{self.name} is studying.")


student = Student("Rahul")

student.introduce()
student.study()


# Solution 3
class Vehicle:

    def move(self):

        print("Vehicle is moving.")


class Car(Vehicle):

    def drive(self):

        print("Car is driving.")


car = Car()

car.move()
car.drive()


# Solution 4
class Animal:

    def speak(self):

        print("Animal makes a sound.")


class Dog(Animal):

    def speak(self):

        print("Dog says Woof!")


class Cat(Animal):

    def speak(self):

        print("Cat says Meow!")


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()


# Solution 5
class Person:

    def __init__(self, name):

        self.name = name


class Student(Person):

    def __init__(self, name, course):

        super().__init__(name)

        self.course = course


student = Student("Rahul", "GenAI")

print(student.name)
print(student.course)


# ============================================================
# PART 8 - TYPES OF INHERITANCE
# ============================================================

# PROBLEM 1
# Demonstrate single inheritance:
#
# Animal -> Dog


# PROBLEM 2
# Demonstrate multilevel inheritance:
#
# Grandparent -> Parent -> Child


# PROBLEM 3
# Demonstrate multiple inheritance:
#
# Camera + Phone -> Smartphone


# PROBLEM 4
# Demonstrate hierarchical inheritance:
#
# Employee -> Developer
# Employee -> Designer


# PROBLEM 5
# Explain hybrid inheritance using a simple class diagram.


# ------------------------------------------------------------
# SOLUTIONS
# ------------------------------------------------------------

# Solution 1 - Single inheritance
class Animal:

    def eat(self):

        print("Eating")


class Dog(Animal):

    def bark(self):

        print("Barking")


dog = Dog()

dog.eat()
dog.bark()


# Solution 2 - Multilevel inheritance
class Grandparent:

    def family_name(self):

        print("Family name")


class Parent(Grandparent):

    def parent_method(self):

        print("Parent method")


class Child(Parent):

    def child_method(self):

        print("Child method")


child = Child()

child.family_name()
child.parent_method()
child.child_method()


# Solution 3 - Multiple inheritance
class Camera:

    def take_photo(self):

        print("Photo taken")


class Phone:

    def make_call(self):

        print("Call made")


class Smartphone(Camera, Phone):

    pass


phone = Smartphone()

phone.take_photo()
phone.make_call()


# Solution 4 - Hierarchical inheritance
class Employee:

    def work(self):

        print("Working")


class Developer(Employee):

    def code(self):

        print("Coding")


class Designer(Employee):

    def design(self):

        print("Designing")


developer = Developer()
designer = Designer()

developer.work()
developer.code()

designer.work()
designer.design()


# Solution 5 - Hybrid inheritance
#
# Hybrid inheritance combines multiple inheritance patterns.
#
# Example:
#
#        Person
#        /    \
#   Student  Employee
#       \     /
#    WorkingStudent
#
# This combines hierarchical and multiple inheritance.


# ============================================================
# PART 9 - MIXED PRACTICAL PROBLEMS
# ============================================================

# PROBLEM 1 - STUDENT MANAGEMENT
#
# Create a Student class with:
# - name
# - age
# - course
# - introduce()
# - __str__()
#
# Create two students and display their information.


# PROBLEM 2 - BANK ACCOUNT
#
# Create a BankAccount class with:
# - owner
# - _balance
# - deposit(amount)
# - show_balance()
#
# Use methods to update and display the balance.


# PROBLEM 3 - EMPLOYEE SYSTEM
#
# Create:
#
# Employee
# Developer(Employee)
# Designer(Employee)
#
# Employee should have:
# - name
# - work()
#
# Developer should have:
# - code()
#
# Designer should have:
# - design()


# PROBLEM 4 - COURSE SYSTEM
#
# Create a Course class with:
# - name
# - instructor
# - students list
# - add_student()
# - show_course()
# - static method course_type()
#
# Create a course and add three students.


# PROBLEM 5 - OOP + DUNDER
#
# Create a ShoppingCart class.
#
# It should contain:
# - items list
# - add_item()
# - __len__()
# - __str__()
#
# Add three items and use len(cart) and print(cart).


# ------------------------------------------------------------
# SOLUTIONS
# ------------------------------------------------------------

# Solution 1
class Student:

    def __init__(self, name, age, course):

        self.name = name
        self.age = age
        self.course = course

    def introduce(self):

        print(
            f"My name is {self.name}. "
            f"I am {self.age} years old and "
            f"I am learning {self.course}."
        )

    def __str__(self):

        return f"{self.name} - {self.course}"


student1 = Student("Rahul", 21, "GenAI")
student2 = Student("Priya", 22, "Python")

student1.introduce()
student2.introduce()

print(student1)
print(student2)


# Solution 2
class BankAccount:

    def __init__(self, owner, balance):

        self.owner = owner
        self._balance = balance

    def deposit(self, amount):

        self._balance = self._balance + amount

    def show_balance(self):

        print(f"{self.owner}'s balance: ₹{self._balance}")


account = BankAccount("Rahul", 5000)

account.show_balance()

account.deposit(2000)

account.show_balance()


# Solution 3
class Employee:

    def __init__(self, name):

        self.name = name

    def work(self):

        print(f"{self.name} is working.")


class Developer(Employee):

    def code(self):

        print(f"{self.name} is coding.")


class Designer(Employee):

    def design(self):

        print(f"{self.name} is designing.")


developer = Developer("Rahul")
designer = Designer("Priya")

developer.work()
developer.code()

designer.work()
designer.design()


# Solution 4
class Course:

    def __init__(self, name, instructor):

        self.name = name
        self.instructor = instructor
        self.students = []

    def add_student(self, student):

        self.students.append(student)

    def show_course(self):

        print(f"Course: {self.name}")
        print(f"Instructor: {self.instructor}")
        print(f"Students: {self.students}")

    @staticmethod
    def course_type():

        return "Programming Course"


course = Course(
    "Python for Beginners",
    "Instructor"
)

course.add_student("Rahul")
course.add_student("Priya")
course.add_student("Amit")

course.show_course()

print(Course.course_type())


# Solution 5
class ShoppingCart:

    def __init__(self):

        self.items = []

    def add_item(self, item):

        self.items.append(item)

    def __len__(self):

        return len(self.items)

    def __str__(self):

        return f"Shopping Cart: {self.items}"


cart = ShoppingCart()

cart.add_item("Laptop")
cart.add_item("Mouse")
cart.add_item("Keyboard")

print(cart)
print("Number of items:", len(cart))


# ============================================================
# FINAL CHALLENGES
# ============================================================

# CHALLENGE 1
# Build a Library Management class.
#
# Requirements:
# - Library name
# - books list
# - add_book()
# - show_books()
# - __len__()
# - __str__()


# CHALLENGE 2
# Build:
#
# Person
# Student(Person)
# Teacher(Person)
#
# Person should have name and introduce().
# Student should have study().
# Teacher should have teach().
#
# Demonstrate hierarchical inheritance.


# CHALLENGE 3
# Create a Vehicle parent class.
#
# Create:
# Car(Vehicle)
# Bike(Vehicle)
#
# Override the move() method in both child classes.


# CHALLENGE 4
# Create a Calculator class containing static methods:
#
# add()
# subtract()
# multiply()
# divide()
#
# Use the class without creating an object.


# CHALLENGE 5
# Build a simple Online Course System combining:
#
# - Class
# - Constructor
# - Attributes
# - Methods
# - Encapsulation
# - Static method
# - Inheritance
# - __str__()
#
# Keep the project simple and focus on applying the concepts.


# ============================================================
# END OF PRACTICE SCRIPT
# ============================================================
