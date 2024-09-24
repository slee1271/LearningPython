# *args = allows you to pass multiple non-key arguments. type is tuple
# **kwargs = allows you to pass multiple keyword arguments

# def add(a,b): can only pass in two numbers.
def add(*args): # can change *args to *nums or anything of your choice
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3,4,5))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Mr.","Shawn", "Shin", "Lee","III")