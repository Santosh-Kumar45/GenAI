num=int("34")

try:
    print(num)
except ValueError:
    print("number is not int data type")
finally:
    print(f"output number is {num}")