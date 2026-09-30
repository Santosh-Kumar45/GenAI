# PROBLEM 3
# Print numbers from 1 to 10 but skip 5.

for i in list(range(1,10,1)):
    if i==5:
        continue
    else:
        print(i)