num=int(input("enter any number"))

try:
    result=10/num
    print("final val is",result)
except ZeroDivisionError:
    print("zero division error")
except ValueError:
    print("value error")