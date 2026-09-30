# PROBLEM 3
# A student has marks.
# Print:
# 90 or above -> "A"
# 75 to 89 -> "B"
# 60 to 74 -> "C"
# Below 60 -> "Needs improvement"

marks=int(input("Enter the number : "))
if marks>=90:
    print("A")
elif marks>=75:
    print("B")
elif marks>=60:
    print("C")
else:
    print("Needs improvement")