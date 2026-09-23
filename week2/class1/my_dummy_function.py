def my_dummy_fun():
    name=input("Enter your name : ")
    age=int(input("Enter your age : "))
    city=input("Enter your city : ")

    return (name,age,city)

yout_name,your_age,your_city=my_dummy_fun()
print(f"hi {your_name},nice to meet you!!")