name="santosh"

def fun_name():
    print(name)

fun_name();
print("----------\n")
#global variable easily we can excess.......

name="santosh"

def new_fun():
    name="priya"
    print(f"my name is {name}")

new_fun()
print(f"my name is {name}")


print("----------\n")

def new_fun():
    global name
    name="priya"
    print(f"my name is {name}")

new_fun()
print(f"my name is {name}")