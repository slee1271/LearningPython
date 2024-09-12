#input() is a function that allows users to enter data. returns the entered data as a string

name = input("What is your name?: ")
age = input("How old are you?: ")
age = int(age) #should change to int because cannot use for arithmetic
# can reduce lines by typing int(input("How old are you?: "))

print(f"Hello {name}")
print(f"You are {age} years old")
print(f"You are turning {age + 1} next!")

