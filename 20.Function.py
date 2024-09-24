# function is a block of reusuable code. Place () after the function name to invoke it
# return is a statement used to end a function and send a result back to the caller

def happy_birthday(name, age):
    print(f"Happy birthday to {name}")
    print(f"You are now {age}")
    print("Happy birthday to you!")
    print()

happy_birthday("Shawn",20)


# functions with return statements
def add(x,y):
    z = x + y
    return z

def subtract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return round(z, 2)

print(add(8,3))
print(subtract(8,3))
print(multiply(8,3))
print(divide(8,3))






    