fruits=["mango","apple","orange","banana"]

# for i ,val in enumerate(fruits):
#     print(f"{i}. {val}")



for i, val in enumerate(fruits,start=1):
    if i%2==0:
      print(f"{i}. {val}")  
    
    