# username is no more than 12 characters
# username must not contain spaces 
# usernmae must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username cannot be more than 12 characters")
elif username.find(" ") != -1:
    print("Your username cannot contain spaces")
elif not username.isalpha():
    print("Your username cannot contain numbers")
else: 
    print(f"Welcome {username}!")