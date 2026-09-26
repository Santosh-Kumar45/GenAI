
import time

def task(name):
    print(f"{name} started..")
#sleep(1) delay the time to print next line
    # time.sleep(1) 
    print(f"{name} finished..")

import threading

thread1=threading.Thread(
    target=task,
    args=("task1",)
)
thread2=threading.Thread(
    target=task,
    args=("task1",)
)
thread3=threading.Thread(
    target=task,
    args=("task1",)
)
thread4=threading.Thread(
    target=task,
    args=("task1",)
)
thread5=threading.Thread(
    target=task,
    args=("task1",)
)

start=time.time()

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()

end= time.time()
print("normal time taken : ",end-start)