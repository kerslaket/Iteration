password = ""
while password != "secret":
    password = input("Please enter your password")
    if password == "secret":
        print("You have access to the system")
    else:
        print("Password incorrect! Try again")
