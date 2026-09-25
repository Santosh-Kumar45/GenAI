#recursion way

"""def factorial(number):
    if number==0:
        return 1
    else:
      return  number * factorial(number-1)
    
print(factorial(6))
"""


def factorial(number):
    result=1
    for i in range(2,number):
        number*=i
    return number

output_result=factorial(5)
print(output_result)    

