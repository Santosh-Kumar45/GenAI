while True:
    user_input = input("ask to me ----> (name/city/profession/exit): ").strip().lower()

    if user_input == "name":
        print("my name is santosh")
    elif user_input == "city":
        print("my city is bangalore")
    elif user_input == "profession":
        print("i am ai eng")
    elif user_input == "exit":
        print("exit from my profile")
        break
    else:
        print("invalid option, try again")