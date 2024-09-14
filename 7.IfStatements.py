# if statements do some cody only IF some condition is True
    # ELSE do something else 

age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
elif age > 100:
    print("You are too old to sign up") #this line will not run because check the order of the statements age >= 18 runs
else: #last resort
    print("You must be 18+ to sign up")



response = input("Would you like food? (Y/N): ")
if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")



name = input("Enter your name:")
if name == "":
    print("You did not type in your name")
else:
    print(f"Hello {name}")