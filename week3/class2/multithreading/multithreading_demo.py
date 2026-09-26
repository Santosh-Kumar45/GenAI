
import time

def task(name):
    print(f"{name} started..")
    time.sleep(1)  #sleep(1) delay the time to print next line
    print(f"{name} finished..")

start=time.time()    

task("santosh")    
task("santosh")    
task("santosh")    
task("santosh")    

end=time.time()

print("normal time taken : ",end-start)