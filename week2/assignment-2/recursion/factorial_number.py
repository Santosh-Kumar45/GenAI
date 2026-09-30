# PROBLEM 2
# Create a recursive function that calculates
# the factorial of a number.

def fact_calculate(number):
    if number==0:
        return 1
    return number * fact_calculate(number-1)


res=fact_calculate(5)
print(res)
    