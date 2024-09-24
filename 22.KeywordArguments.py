# keyword arguments preceded by an identifier. helps with readability, order doesn't matter 

def hello(greeting, title, first, last):
    print(f"{greeting} {title}.{first} {last}")

hello("Hello", "Mr", "Shawn", "Lee")

hello(title="Mr", first="Shawn", greeting="Hello", last="Lee") # changed so the order doesn't matter but we need to add a keyword argument
hello("Hello", first="Shawn", title="Mr", last="Lee") # once you use keyword arguements for the first argument then it must be done to the ones after

# example 
hello("Hello", "Mr", last="John", first="James") # which one is first name and last name? John or James?

for x in range(1,11):
    print(x, end=" ") # end is replacing \n. changing the end in the print function
print()

# can use sep="-" for other case like phone numbers

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=403, first=987, last=654) # would use in a case like here for easier readability
print(phone_num)
