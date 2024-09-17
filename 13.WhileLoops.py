# while loops execute some code WHILE some condition remains true 

# Example 1
name = input("Enter your name: ")
while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ") # this line is necessary or else there will be an infinite loop
print(f"Hello {name}")


# Example 2
food = input("Enter a food you like (q to quit): ")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit): ")
print("Bye")

# Example 3
num = int(input("Enter a num between 1-10: "))
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a num between 1-10: "))
print(f"Your number is: {num}")

    
