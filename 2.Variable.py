# A variable is a container for a value. (string, integer, float, boolean)
# Variable behaves as if it was the value it contains

#strings
first_name = "Shawn"
print(first_name)
print(f"Hello {first_name}") # "f" stands for format

food = "Pizza"
print(f"I like to eat {food}")

email = "shawn123@python.ca"
print(f"Your email is: {email}")


#integers
age = 22
quantity = 2
num_of_people = 20 

print(f"You are {age} years old")
print("You bought", + quantity, "items" )
print(f"My class has {num_of_people} students")


#float 
price = 14.99
gpa = 3.98

print(f"The price is ${price}")
print(f"My GPA is: {gpa}")

#boolean 
is_student = True
print(f"Are you a student?: {is_student}")

if is_student:
    print("Yes!")
else: 
    print("No :()")