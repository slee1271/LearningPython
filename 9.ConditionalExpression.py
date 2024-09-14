""" Conditional expression is a one-line shortcut for the if-else statement (ternary operator)
print or assign one of two values based on a condition 
x if condition else y """

num = 5
print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

a = 8
b = 5
max_num = a if a > b else b
min_num = a if a < b else b
print(max_num)
print(min_num)

age = 20
print("Adult" if age >= 18 else "Child")

temperature = 22
weather = "Hot" if temperature > 20 else "Cold"
print(weather)

user_role = "ADMIN"
access_level = "Full Access" if user_role.lower() == "admin" else "limited access"
print(access_level)