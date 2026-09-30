# PROBLEM 4
# Use sorted() and a lambda function to sort:

students = [
    {"name": "Rahul", "marks": 80},
    {"name": "Priya", "marks": 95},
    {"name": "Amit", "marks": 70}
]
sorted_students = sorted(
    students,
    key=lambda student: student["marks"]
)
print(sorted_students)