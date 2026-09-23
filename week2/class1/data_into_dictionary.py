
mylav={
    "name":"santosh",
    "age":20,
    "city":"mumbai"
}
#print obj
print(mylav)


#access value
print(mylav["name"])


#add value
mylav["language"]="python"
print(mylav)


#editing value
mylav["city"]="banglore"
print(mylav)


print(mylav.get("city","NA"))