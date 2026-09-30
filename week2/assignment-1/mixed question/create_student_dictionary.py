# PROBLEM 2
# Create a student dictionary with:
#
# name
# age
# course
# city
#
# Then update the age and add a new key:
#
# "experience": "Beginner"


student={
    "name":"santosh",
    "age":22,
    "course":"gen ai",
    "city":"ranchi"
}

student["age"]=21
student["experience"]="Beginner"
print(student)