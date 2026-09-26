import time



def fun(my_list):
    print(my_list)
    time.sleep(3)
    print(my_list)

start=time.time()

my_list=["santosh","rahul","ashish","krish"]
fun(my_list)
fun(my_list)
fun(my_list)

end=time.time()

print("time taken : ",end-start)