username = "c4e"
password = "codethechange"

username_input = input("Username: ")

if username_input != username:
    print("Not found user")
else:
    password_input = input("Password: ")
    if password_input != password:
        print("Wrong password")
    else:
        print("Welcome!")