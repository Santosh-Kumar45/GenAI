student={
    "name":"santosh",
    "age":22,
    "city":"gomo"
}



# for i in student:
#     print(i)


# for i in student.values():
#     print(i)


# for i in student.items():
#     print(i)

for i in student.items():
    key, value= i
    print(f"{key}-->{value}")