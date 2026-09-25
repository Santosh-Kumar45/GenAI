students=[
    {
        "name":"santosh",
        "marks":88
    },
    {
        "name":"mukesh",
        "marks":83
    },
    {
        "name":"rohit",
        "marks":59
    }
]

result=sorted(
    students,
    key=lambda student:student["marks"]
)
print(result)