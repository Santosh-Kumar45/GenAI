# PROBLEM 3
# Create a function calculate_discount(price, percentage)
# that returns the discount amount.

def calculate_discount(price,percentage):
    return price*percentage/100
final_amount=calculate_discount(10000,20)
print(final_amount)
