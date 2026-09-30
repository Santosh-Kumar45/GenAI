# PROBLEM 4
# Check whether a person can enter an event.
#
# Conditions:
# age must be 18 or above
# AND has_id must be True

person_age=int(input("enter your age : "))
has_id=input("enter your id (True/False) : ")

if person_age>=18 and has_id=="True":
    print("You can go ")
else:
    print("you are not eligible")