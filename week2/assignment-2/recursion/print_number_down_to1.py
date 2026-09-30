# PROBLEM 1
# Create a recursive function countdown(number)
# that prints numbers down to 1.

def countdown(number):
    if number == 0:
        return
    print(number)
    countdown(number - 1)

countdown(5)